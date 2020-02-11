# Generated by Django 2.2.8 on 2020-01-12 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletag',
            options={'ordering': ['-is_main', '-tag'], 'verbose_name': 'тематика статьи', 'verbose_name_plural': 'тематики статьи'},
        ),
        migrations.AlterField(
            model_name='articletag',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='статья'),
        ),
    ]