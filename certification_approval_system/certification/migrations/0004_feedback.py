# Generated by Django 4.2.4 on 2023-08-03 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification', '0003_remove_employeerequest_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('recipient_name', models.CharField(max_length=100)),
                ('recipient_email', models.EmailField(max_length=254)),
                ('sent_date', models.DateField()),
                ('department', models.CharField(max_length=100)),
                ('feedback_text', models.TextField()),
            ],
        ),
    ]
