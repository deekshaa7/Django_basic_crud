# Generated by Django 5.0.2 on 2024-03-17 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_student_details_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='phone',
            field=models.IntegerField(blank=True, max_length=13, null=True),
        ),
    ]