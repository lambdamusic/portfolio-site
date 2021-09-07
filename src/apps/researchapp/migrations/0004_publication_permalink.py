# Generated by Django 2.1.3 on 2021-09-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchapp', '0003_auto_20210907_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='permalink',
            field=models.CharField(blank=True, help_text='If not provided, automatically set from title and date', max_length=255, null=True, verbose_name='permalink'),
        ),
    ]