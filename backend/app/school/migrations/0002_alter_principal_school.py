# Generated by Django 3.2.4 on 2021-06-23 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='school',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='school_principal', to='school.school'),
        ),
    ]
