# Generated by Django 4.0.4 on 2022-06-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_jobdetail_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetail',
            name='experience',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
