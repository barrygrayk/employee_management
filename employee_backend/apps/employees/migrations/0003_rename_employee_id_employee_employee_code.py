# Generated by Django 5.0.4 on 2024-05-02 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_skill_options_employee_employee_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employee_id',
            new_name='employee_code',
        ),
    ]
