# Generated by Django 4.0.5 on 2022-07-05 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShoesFactory', '0004_balance_debton_zpeople'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zpeople',
            name='balance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShoesFactory.balance', verbose_name='Остаток:'),
        ),
        migrations.AlterField(
            model_name='zpeople',
            name='debt_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShoesFactory.debton', verbose_name='Задолжность:'),
        ),
        migrations.AlterField(
            model_name='zpeople',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShoesFactory.employee', verbose_name='Сотрудник:'),
        ),
    ]
