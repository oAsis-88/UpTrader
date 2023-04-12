# Generated by Django 4.1.7 on 2023-04-12 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='TreeView.paragraph')),
            ],
            options={
                'verbose_name': 'Пункт',
                'verbose_name_plural': 'Пункты',
            },
        ),
    ]
