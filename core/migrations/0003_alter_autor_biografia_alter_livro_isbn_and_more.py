# Generated by Django 5.1.2 on 2024-10-08 23:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_livro_categoria_livro_publicado_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='isbn',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='publicado_em',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
