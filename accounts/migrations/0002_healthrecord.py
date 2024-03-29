# Generated by Django 4.2.6 on 2023-10-05 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.PositiveIntegerField()),
                ('age', models.PositiveIntegerField()),
                ('glucose', models.PositiveIntegerField()),
                ('skin_thickness', models.PositiveIntegerField()),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
