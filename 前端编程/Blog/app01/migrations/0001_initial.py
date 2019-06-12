# Generated by Django 2.2 on 2018-09-17 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ansible_Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(blank=True, default='', max_length=50)),
                ('name', models.CharField(blank=True, default='', max_length=50)),
                ('ssh_host', models.CharField(blank=True, default='', max_length=50)),
                ('ssh_user', models.CharField(blank=True, default='', max_length=50)),
                ('ssh_port', models.CharField(blank=True, default='', max_length=50)),
                ('server_type', models.CharField(blank=True, default='', max_length=100)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ansible_Yml_Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yml_file', models.CharField(blank=True, default='', max_length=200)),
                ('yml_maintenancer', models.CharField(blank=True, default='', max_length=50)),
                ('yml_parameter', models.TextField(blank=True, null=True)),
                ('accept_host_group', models.CharField(blank=True, default='', max_length=200)),
                ('comment', models.CharField(blank=True, default='', max_length=200)),
                ('register_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Demo2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
