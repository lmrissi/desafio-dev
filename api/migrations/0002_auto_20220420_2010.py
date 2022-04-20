# Generated by Django 3.2.13 on 2022-04-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cnab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cpf', models.CharField(max_length=11)),
                ('card', models.CharField(max_length=12)),
                ('hour', models.TimeField()),
                ('store_owner', models.CharField(max_length=14)),
                ('store_name', models.CharField(max_length=19)),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
