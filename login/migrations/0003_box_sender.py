# Generated by Django 4.1.2 on 2022-10-31 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_box_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.user', to_field='fake_name'),
            preserve_default=False,
        ),
    ]