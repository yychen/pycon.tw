# Generated by Django 3.0.2 on 2020-02-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0040_auto_20190915_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalspeaker',
            name='conference',
            field=models.SlugField(choices=[('pycontw-2016', 'PyCon Taiwan 2016'), ('pycontw-2017', 'PyCon Taiwan 2017'), ('pycontw-2018', 'PyCon Taiwan 2018'), ('pycontw-2019', 'PyCon Taiwan 2019'), ('pycontw-2020', 'PyCon Taiwan 2020')], default='pycontw-2020', verbose_name='conference'),
        ),
        migrations.AlterField(
            model_name='talkproposal',
            name='conference',
            field=models.SlugField(choices=[('pycontw-2016', 'PyCon Taiwan 2016'), ('pycontw-2017', 'PyCon Taiwan 2017'), ('pycontw-2018', 'PyCon Taiwan 2018'), ('pycontw-2019', 'PyCon Taiwan 2019'), ('pycontw-2020', 'PyCon Taiwan 2020')], default='pycontw-2020', verbose_name='conference'),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='conference',
            field=models.SlugField(choices=[('pycontw-2016', 'PyCon Taiwan 2016'), ('pycontw-2017', 'PyCon Taiwan 2017'), ('pycontw-2018', 'PyCon Taiwan 2018'), ('pycontw-2019', 'PyCon Taiwan 2019'), ('pycontw-2020', 'PyCon Taiwan 2020')], default='pycontw-2020', verbose_name='conference'),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='duration',
            field=models.CharField(choices=[('1.5hr', '1.5hr')], default='1.5hr', max_length=7, verbose_name='duration'),
        ),
    ]