# Generated by Django 4.0.6 on 2024-02-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularioInstituicoes', '0002_remove_pergunta_tema_alter_questionario_perguntas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionario',
            name='perguntas',
        ),
        migrations.AddField(
            model_name='questionario',
            name='temas',
            field=models.ManyToManyField(blank=True, null=True, related_name='questionarios', to='formularioInstituicoes.tema'),
        ),
    ]