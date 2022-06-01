# Generated by Django 3.0.5 on 2020-05-06 14:20

from django.db import migrations
from django.contrib.auth.models import User

def default_site_config(apps, schema_editor):
    """ Default site configurations """

    User.objects.create_superuser('admin', 'admin@schoolapp.com', 'admin123')

    Config = apps.get_model('corecode', 'SiteConfig')
    Config.objects.bulk_create([
        Config(key='school_name', value='SUDO High School'),
        Config(key='school_slogan', value='A great school'),
        Config(key='school_address', value='Thu Duc, Ho Chi Minh'),
    ])

    Session = apps.get_model('corecode', 'AcademicSession')
    Session.objects.bulk_create([
        Session(name='2021/2022', current=True),
    ])

    Term = apps.get_model('corecode', 'AcademicTerm')
    Term.objects.bulk_create([
        Term(name='1st Term', current=True),
        Term(name='2nd Term', current=False),
        Term(name='3rd Term', current=False),
    ])

    Subject = apps.get_model('corecode', 'Subject')
    Subject.objects.bulk_create([
        Subject(name='Mathematics'),
        Subject(name='English'),
        Subject(name='Biology'),

    ])

    StudentClass = apps.get_model('corecode', 'StudentClass')
    StudentClass.objects.bulk_create([
        StudentClass(name='10A1'),
        StudentClass(name='10A2'),
        StudentClass(name='10A3'),
        StudentClass(name='10A4'),
        StudentClass(name='11A1'),
        StudentClass(name='11A2'),
        StudentClass(name='11A3'),
        StudentClass(name='12A1'),
        StudentClass(name='12A2'),
    ])
    


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(default_site_config),
    ]
