# Generated by Django 4.0.3 on 2022-10-03 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_exercise_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='sex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.sex'),
        ),
    ]