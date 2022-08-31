# Generated by Django 4.1 on 2022-08-23 13:10

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_resumo_post_summary_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='img_summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
