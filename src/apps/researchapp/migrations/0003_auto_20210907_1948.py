# Generated by Django 2.1.3 on 2021-09-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchapp', '0002_auto_20210830_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='url1',
            field=models.URLField(blank=True, help_text='For blogs, this field should contain the local MD file location.', null=True, verbose_name='url1'),
        ),
    ]
