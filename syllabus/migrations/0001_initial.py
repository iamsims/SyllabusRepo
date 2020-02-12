# Generated by Django 3.0.2 on 2020-02-07 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('11', 'I/I'), ('12', 'I/II')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Levels',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('BE', 'Bachelors'), ('ME', 'Masters')], max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.Faculty')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.Level')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.Program')),
            ],
            options={
                'verbose_name_plural': 'Specifications',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_type', models.CharField(choices=[('Compulsory', 'Compulsory'), ('Elective I', 'Elective I'), ('Elective II', 'Elective II'), ('Elective III', 'Elective III')], default='COMPULSORY', max_length=20)),
                ('lecture_hours', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('tutorial_hours', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('practical_hours', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('Total_no_of_hours', models.DecimalField(decimal_places=1, max_digits=2)),
                ('practical_assessment_total', models.IntegerField(blank=True, null=True)),
                ('practical_final_total', models.IntegerField(blank=True, null=True)),
                ('theory_assessment_total', models.IntegerField(blank=True, null=True)),
                ('theory_final_total', models.IntegerField(blank=True, null=True)),
                ('marks_final_total', models.IntegerField(blank=True, null=True)),
                ('theory_duration_hours', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('practical_duration_hours', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('exam_type', models.CharField(choices=[('T', 'THEORY'), ('P', 'PRACTICAL'), ('B', 'BOTH')], default='Theory', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_final_marks', models.IntegerField()),
                ('Subject', models.ManyToManyField(to='syllabus.Subject')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.Specification')),
            ],
            options={
                'verbose_name_plural': 'Syllabus',
            },
        ),
    ]
