# Generated by Django 2.0 on 2018-09-01 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('course', models.CharField(choices=[('BTech', 'B.Tech'), ('MTech', 'M.Tech'), ('MCA', 'MCA'), ('MBA', 'MBA'), ('PHD', 'Phd')], default='BTech', max_length=10)),
                ('regNum', models.CharField(max_length=10)),
                ('branch', models.CharField(choices=[('-', '---SELECT---'), ('CSE', 'Computer Science & Engineering'), ('ECE', 'Electronics and Communication Engineering'), ('MECH', 'Mechanical Engineering'), ('MME', 'Metallurgy Engineering'), ('CHE', 'Chemical Engineering'), ('CIVIL', 'Civil Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('BIO', 'Biotechnology')], max_length=10)),
                ('contact', models.CharField(max_length=20)),
            ],
        ),
    ]