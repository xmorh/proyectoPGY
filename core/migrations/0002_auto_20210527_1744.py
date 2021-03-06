# Generated by Django 3.2.2 on 2021-05-27 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fecha_fabrica',
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha_ingreso',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('f_nacimiento', models.DateField()),
                ('comuna', models.CharField(max_length=20)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]
