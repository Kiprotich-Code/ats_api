# Generated by Django 4.2.16 on 2025-02-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('applied_on', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('interview', 'Interview'), ('rejected', 'Rejected'), ('accepted', 'Accepted')], default='pending', max_length=10)),
                ('result', models.TextField(blank=True, null=True)),
                ('application_deadline', models.DateField()),
            ],
        ),
    ]
