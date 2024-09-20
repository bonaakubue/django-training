# Generated by Django 5.1.1 on 2024-09-13 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='transactiontype',
            new_name='transaction_type',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='Transaction_date',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='destination',
        ),
        migrations.AddField(
            model_name='transaction',
            name='destination_account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='received_transactions', to='payment.paymentaccount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender_account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sent_transactions', to='payment.paymentaccount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paymentaccount',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('dormant', 'Dormant'), ('suspended', 'Suspended')], max_length=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='reference',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
