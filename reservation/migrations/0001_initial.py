# Generated by Django 3.2.6 on 2021-08-14 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0002_dieter_gym'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('inquiry', '예약대기'), ('confirmed', '예약확정'), ('rejection', '예약취소')], max_length=100)),
                ('reason', models.TextField(blank=True, null=True)),
                ('reserved_date', models.DateTimeField()),
                ('dieter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.dieter')),
                ('gym', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.gym')),
            ],
        ),
    ]