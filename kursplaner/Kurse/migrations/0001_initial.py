# Generated by Django 3.2.9 on 2022-03-12 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lehrer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurs_typ', models.CharField(choices=[('SG', 'Ski Gruppe'), ('SP', 'Ski Privat'), ('SBG', 'Snowboard Gruppe'), ('SBP', 'Snowboard Privat'), ('LL', 'Langlauf'), ('TM', 'Telemark')], max_length=3)),
                ('skill_level', models.CharField(choices=[('0', 'KEINE VORKENTINISSE'), ('1', 'Schneepflug'), ('2', 'Kurven'), ('3', 'MUSS LIFTFAHREN ÜBEN'), ('4', 'Parallelschwung üben'), ('5', ''), ('6', ''), ('7', '')], default='0', max_length=2)),
                ('time', models.CharField(choices=[('0900', '09:00 - 10:00'), ('1000', '10:00 - 12:00'), ('1200', '12:00 - 13:00'), ('1330', '13:30 - 15:30')], max_length=4)),
                ('datum', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am:')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Geändert am:')),
            ],
        ),
        migrations.CreateModel(
            name='Tagesplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('lehrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lehrer.lehrer')),
                ('nine_to_ten', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='9-10+', to='Kurse.kurs')),
                ('ten_to_twelve', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='10-12+', to='Kurse.kurs')),
                ('thirteen_thirty_to_fifteen_thirty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='13:30-15:30+', to='Kurse.kurs')),
                ('twelve_to_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='12-13+', to='Kurse.kurs')),
            ],
        ),
    ]
