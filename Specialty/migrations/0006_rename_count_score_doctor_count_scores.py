# Generated by Django 4.2 on 2023-12-20 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Specialty', '0005_remove_doctor_count_scores_doctor_count_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='Count_Score',
            new_name='Count_Scores',
        ),
    ]
