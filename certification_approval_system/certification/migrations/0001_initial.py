# Generated by Django 4.2.4 on 2023-08-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.CharField(choices=[('HR', 'HR'), ('Marketing', 'Marketing & Sales'), ('Software Development', 'Software Development'), ('Cyber Security', 'Cyber Security'), ('Networking', 'Networking'), ('Finance', 'Finance'), ('Data Analysis', 'Data Analysis')], max_length=50)),
                ('request_date', models.DateField(auto_now_add=True)),
                ('reason_for_request', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=20)),
            ],
        ),
    ]
