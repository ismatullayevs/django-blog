# Generated by Django 3.2.9 on 2021-12-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_tag_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='for_navbar',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
