# Generated by Django 3.1 on 2020-08-12 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicoDois',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_impar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicoQuatro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_publicado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicoTres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_multiplicado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicoUm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_par', models.IntegerField()),
            ],
        ),
    ]
