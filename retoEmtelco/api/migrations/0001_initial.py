# Generated by Django 4.1.7 on 2023-03-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vuln_id', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('severity', models.CharField(max_length=20)),
            ],
        ),
    ]
