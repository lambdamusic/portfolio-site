# Generated by Django 2.1.3 on 2021-09-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchapp', '0004_publication_permalink'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='md_file',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='For blogs, this field should contain the local MD file location (without path)'),
        ),
        migrations.AddField(
            model_name='publication',
            name='pdf_url',
            field=models.URLField(blank=True, help_text='The main PDF version of the publication.', null=True, verbose_name='pdf'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='url1',
            field=models.URLField(blank=True, null=True, verbose_name='url1'),
        ),
    ]
