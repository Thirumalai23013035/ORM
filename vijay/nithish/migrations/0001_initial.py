# Generated by Django 5.0.2 on 2024-03-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_DB',
            fields=[
                ('serialno', models.IntegerField(primary_key='serialno', serialize=False)),
                ('bookname', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=20)),
                ('Dop', models.DateField()),
                ('totalpg', models.IntegerField()),
            ],
        ),
    ]
