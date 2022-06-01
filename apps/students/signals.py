import os
import csv
from io import StringIO
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.corecode.models import StudentClass
from .models import Student, StudentBulkUpload

@receiver(post_save, sender=StudentBulkUpload)
def create_bulk_student(sender, created, instance, *args, **kwargs):
  if created:
    opened = StringIO(instance.csv_file.read().decode())
    reading = csv.DictReader(opened, delimiter=',')
    students = []
    for row in reading:
      if 'registration_number' in row and row['registration_number']:
        surname = row['surname'] if 'surname' in row and row['surname'] else ''
        firstname = row['firstname'] if 'firstname' in row and row['firstname'] else ''
        name = f"{surname.strip()} {firstname.strip()}"
        gender = (row['gender']) if 'gender' in row and row['gender'] else ''
        phone = row['parent_number'] if 'parent_number' in row and row['parent_number'] else ''
        address = row['address'] if 'address' in row and row['address'] else ''
        current_class = row['current_class'] if 'current_class' in row and row['current_class'] else ''
        email=row['email'] if 'email' in row and row['email'] else ''
        if current_class:
          theclass, kind = StudentClass.objects.get_or_create(name=current_class)
        if gender not in ["Nam", "Nữ"]:
          print("gender is invalid")
          continue
        if name == "":
          print("name is invalid")
          continue
        if current_class not in ["10A1", "10A2", "10A3", "10A4", "10A5", "11A1", "11A2", "11A3", "12A1", "12A2"]:
          print("class is invalid")
          continue
        print(Student().current_class)
        students.append(
        Student(
                name=name,
                # firstname=firstname,
                # other_name=other_names,

                gender=gender,
                current_class=theclass,
                parent_mobile_number=phone,
                address=address,
                email=email,
            )
          )

    Student.objects.bulk_create(students)
    instance.csv_file.close()
    instance.delete()


def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)

@receiver(post_delete, sender=StudentBulkUpload)
def delete_csv_file(sender, instance, *args, **kwargs):
  if instance.csv_file:
    _delete_file(instance.csv_file.path)


@receiver(post_delete, sender=Student)
def delete_passport_on_delete(sender, instance, *args, **kwargs):
  if instance.passport:
    _delete_file(instance.passport.path)
