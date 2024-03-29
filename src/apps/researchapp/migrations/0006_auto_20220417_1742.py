# Generated by Django 2.1.3 on 2022-04-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchapp', '0005_auto_20210907_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='publications', to='researchapp.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, help_text='Feel free to use https://html-online.com/editor', null=True, verbose_name='description (markdown/html welcome!)'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='md_file',
            field=models.CharField(blank=True, help_text='Only for blogs: the local MD file name (without path)', max_length=200, null=True, verbose_name='Markdown file name'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='permalink',
            field=models.CharField(blank=True, help_text='If not provided, automatically set from title (or md_file) and date', max_length=255, null=True, verbose_name='permalink'),
        ),
    ]
