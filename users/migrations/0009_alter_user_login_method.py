# Generated by Django 3.2.7 on 2021-09-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('gmail', 'Google'), ('naver', 'Naver'), ('kakao', 'Kakao')], default='email', max_length=50),
        ),
    ]
