# Generated by Django 3.2.7 on 2021-09-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('averagescore', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
