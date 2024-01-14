# Generated by Django 4.2.8 on 2024-01-14 09:52

from django.db import migrations, models
import django.db.models.deletion
import utils.Enums
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management_panel', '0005_alter_sundayservices_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchVisitors',
            fields=[
                ('primary_key', models.AutoField(primary_key=True, serialize=False)),
                ('visitor_unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('visitor_name', models.CharField(max_length=9000)),
                ('visitor_gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=9000)),
                ('visitor_phone', models.CharField(max_length=9000)),
                ('visitor_email', models.CharField(blank=True, default='', max_length=9000, null=True)),
                ('visitor_resident', models.CharField(blank=True, default='', max_length=9000, null=True)),
                ('visitor_visit_reasons', models.CharField(blank=True, choices=[('VISITING', 'VISITING'), ('JOINING', 'JOINING')], default=utils.Enums.VisitReasonsInum['VISITING'], max_length=9000, null=True)),
                ('visitor_spiritual_asistance', models.CharField(blank=True, choices=[('PRAYER', 'PRAYER'), ('SALVATION', 'SALVATION'), ('COUNCELING', 'COUNCELING')], default=utils.Enums.SpiritualAsistanceInum['PRAYER'], max_length=9000, null=True)),
                ('visitor_comments', models.CharField(blank=True, default='', max_length=9000, null=True)),
                ('visitor_registered_date', models.DateTimeField(auto_now_add=True)),
                ('visitor_sunday_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visitor_sunday_service', to='management_panel.sundayservices')),
            ],
            options={
                'verbose_name_plural': 'Visitors',
                'db_table': 'church_visitors_tbl',
                'db_table_comment': 'Church Visitors',
                'ordering': ['-primary_key'],
            },
        ),
    ]
