# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-19 15:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.IntegerField()),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('is_closed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemConhecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Problema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField(max_length=300)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto_id', models.IntegerField()),
                ('nome', models.CharField(max_length=200)),
                ('permalink', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Solucao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('issue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taiga.Issue')),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.IntegerField()),
                ('nome', models.CharField(max_length=200)),
                ('dataInicio', models.DateTimeField(blank=True, null=True)),
                ('dataFim', models.DateTimeField(blank=True, null=True)),
                ('is_closed', models.CharField(max_length=200)),
                ('projeto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taiga.Projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.IntegerField()),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('is_closed', models.BooleanField()),
                ('numeroSolucoes', models.IntegerField(null=True)),
                ('user', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.IntegerField()),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200)),
                ('tags', models.CharField(max_length=200)),
                ('sprint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taiga.Sprint')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taiga.Team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('itemconhecimento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='taiga.ItemConhecimento')),
                ('url', models.CharField(max_length=200)),
            ],
            bases=('taiga.itemconhecimento',),
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('itemconhecimento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='taiga.ItemConhecimento')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('editora', models.CharField(max_length=200)),
                ('edicao', models.CharField(max_length=200)),
            ],
            bases=('taiga.itemconhecimento',),
        ),
        migrations.CreateModel(
            name='PessoaConhecimento',
            fields=[
                ('itemconhecimento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='taiga.ItemConhecimento')),
                ('pessoa', models.CharField(max_length=200)),
            ],
            bases=('taiga.itemconhecimento',),
        ),
        migrations.AddField(
            model_name='task',
            name='userStory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taiga.UserStory'),
        ),
        migrations.AddField(
            model_name='solucao',
            name='tarefa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taiga.Task'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taiga.Team'),
        ),
        migrations.AddField(
            model_name='issue',
            name='projeto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taiga.Projeto'),
        ),
    ]