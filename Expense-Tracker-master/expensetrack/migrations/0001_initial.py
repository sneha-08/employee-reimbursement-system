# Generated by Django 2.2.12 on 2020-04-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('item', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50,default = "ON PROCESS")),
                ('date', models.DateField()),
            ],
        ),
    ]
