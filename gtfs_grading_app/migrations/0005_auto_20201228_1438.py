# Generated by Django 3.1.3 on 2020-12-28 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs_grading_app', '0004_review_category_data_selector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consistency_widget',
            name='other_text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='score_reason',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='score',
            name='help_text',
            field=models.TextField(),
        ),
    ]