# Generated by Django 3.2.2 on 2021-05-27 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha_fabrica', models.DateField()),
                ('dimensiones', models.CharField(max_length=15)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.material')),
            ],
        ),
    ]
