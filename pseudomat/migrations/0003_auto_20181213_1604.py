# Generated by Django 2.1.4 on 2018-12-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pseudomat', '0002_project_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='upload_dir',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='vao_ip',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='secret',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
