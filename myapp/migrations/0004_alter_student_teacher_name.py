# Generated by Django 4.2.6 on 2023-10-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_teacher_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher_name',
            field=models.ManyToManyField(blank=True, related_name='student_teacher', to='myapp.teacher'),
        ),
    ]
