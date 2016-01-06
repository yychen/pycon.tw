# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0017_auto_20160104_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talkproposal',
            name='objective',
            field=models.TextField(help_text='Who is the intended audience for your talk? (Be specific, "Python users" is not a good answer). And what will the attendees get out of your talk? When they leave the room, what will they learn that they didn\'t know before? This is NOT made public and for REVIEW ONLY.', max_length=500, verbose_name='objective'),
        ),
        migrations.AlterField(
            model_name='talkproposal',
            name='outline',
            field=models.TextField(blank=True, help_text='How the talk will be arranged. It is highly recommended to attach the estimated time length for each sections in the talk. Talks in favor of 45min should have a fallback plan about how to shrink the content into a 25min one. This is NOT made public and for REVIEW ONLY.', verbose_name='outline'),
        ),
        migrations.AlterField(
            model_name='talkproposal',
            name='supplementary',
            field=models.TextField(blank=True, default='', help_text="Anything else you'd like the program committee to know when making their selection: your past speaking experience, community experience, etc. This is NOT made public and for REVIEW ONLY. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='supplementary'),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='objective',
            field=models.TextField(help_text='Who is the intended audience for your talk? (Be specific, "Python users" is not a good answer). And what will the attendees get out of your talk? When they leave the room, what will they learn that they didn\'t know before? This is NOT made public and for REVIEW ONLY.', max_length=500, verbose_name='objective'),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='outline',
            field=models.TextField(blank=True, help_text='How the tutorial will be arranged. You should enumerate over each section in your talk and attach each section with the estimated time length. This is NOT made public and for REVIEW ONLY.', verbose_name='outline'),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='supplementary',
            field=models.TextField(blank=True, default='', help_text="Anything else you'd like the program committee to know when making their selection: your past speaking experience, community experience, etc. This is NOT made public and for REVIEW ONLY. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='supplementary'),
        ),
    ]
