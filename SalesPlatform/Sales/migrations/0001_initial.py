# Generated by Django 3.0.5 on 2020-08-02 08:50

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=15)),
            ],
            managers=[
                ('users', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('contact_details', models.CharField(max_length=300)),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Sales.Users')),
            ],
            managers=[
                ('contacts', django.db.models.manager.Manager()),
            ],
        ),
    ]
