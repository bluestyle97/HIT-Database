# Generated by Django 2.0.4 on 2018-06-02 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('result', models.CharField(choices=[('S', 'Success'), ('F', 'Fail'), ('U', 'Unfinished')], default='U', max_length=1)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('leader', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('homepage', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('homepage', models.URLField()),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp3.Institute')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('publish_date', models.DateField()),
                ('journal', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('pass_date', models.DateField()),
                ('valid_time', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp3.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('M', 'Man'), ('W', 'Woman'), ('U', 'Unknown')], default='U', max_length=1)),
                ('age', models.PositiveSmallIntegerField()),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('M', 'Man'), ('W', 'Woman'), ('U', 'Unknown')], default='U', max_length=1)),
                ('age', models.PositiveSmallIntegerField()),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp3.Group')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp3.Teacher'),
        ),
        migrations.AddField(
            model_name='patent',
            name='students',
            field=models.ManyToManyField(to='exp3.Student'),
        ),
        migrations.AddField(
            model_name='patent',
            name='teachers',
            field=models.ManyToManyField(to='exp3.Teacher'),
        ),
        migrations.AddField(
            model_name='paper',
            name='students',
            field=models.ManyToManyField(to='exp3.Student'),
        ),
        migrations.AddField(
            model_name='paper',
            name='teachers',
            field=models.ManyToManyField(to='exp3.Teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='laboratory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp3.Laboratory'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='exp3.Project'),
        ),
    ]
