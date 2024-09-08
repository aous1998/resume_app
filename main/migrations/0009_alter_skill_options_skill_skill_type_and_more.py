# Generated by Django 5.1 on 2024-09-05 20:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_portfolio_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={},
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_type',
            field=models.CharField(choices=[('key', 'Key Skill'), ('coding', 'Coding Skill')], default='coding', max_length=10),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='quote',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
