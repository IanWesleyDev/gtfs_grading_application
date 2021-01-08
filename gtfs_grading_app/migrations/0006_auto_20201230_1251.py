# Generated by Django 3.1.3 on 2020-12-30 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs_grading_app', '0005_auto_20201228_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(max_length=150)),
                ('mode', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='gtfs_grading_app.review'),
            preserve_default=False,
        ),
    ]