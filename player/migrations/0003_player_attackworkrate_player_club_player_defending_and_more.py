# Generated by Django 5.1.1 on 2024-09-22 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_player_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='attackWorkRate',
            field=models.CharField(choices=[('B', 'Baixo'), ('M', 'Médio'), ('A', 'Alto')], default='M', max_length=1, verbose_name='Dedicação Ofensiva'),
        ),
        migrations.AddField(
            model_name='player',
            name='club',
            field=models.CharField(default='Sem Time', max_length=255, verbose_name='Time'),
        ),
        migrations.AddField(
            model_name='player',
            name='defending',
            field=models.IntegerField(default='50', verbose_name='Marcação'),
        ),
        migrations.AddField(
            model_name='player',
            name='defenseWorkRate',
            field=models.CharField(choices=[('B', 'Baixo'), ('M', 'Médio'), ('A', 'Alto')], default='M', max_length=1, verbose_name='Dedicação Defensiva'),
        ),
        migrations.AddField(
            model_name='player',
            name='dribbling',
            field=models.IntegerField(default='50', verbose_name='Drible'),
        ),
        migrations.AddField(
            model_name='player',
            name='firstName',
            field=models.CharField(default='Fulano', max_length=255, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='player',
            name='foot',
            field=models.CharField(choices=[('E', 'Esquerdo'), ('D', 'Direito')], default='D', max_length=1, verbose_name='Pé Dominante'),
        ),
        migrations.AddField(
            model_name='player',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1, verbose_name='Gênero'),
        ),
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.IntegerField(default='150', verbose_name='Altura'),
        ),
        migrations.AddField(
            model_name='player',
            name='lastName',
            field=models.CharField(default='de Tal', max_length=255, verbose_name='Sobrenome'),
        ),
        migrations.AddField(
            model_name='player',
            name='league',
            field=models.CharField(default='Liga ABC', max_length=255, verbose_name='Liga'),
        ),
        migrations.AddField(
            model_name='player',
            name='nation',
            field=models.CharField(default='Desconhecido', max_length=255, verbose_name='Nacionalidade'),
        ),
        migrations.AddField(
            model_name='player',
            name='pace',
            field=models.IntegerField(default='50', verbose_name='Ritmo'),
        ),
        migrations.AddField(
            model_name='player',
            name='passing',
            field=models.IntegerField(default='50', verbose_name='Passe'),
        ),
        migrations.AddField(
            model_name='player',
            name='physicality',
            field=models.IntegerField(default='50', verbose_name='Físico'),
        ),
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('GOL', 'Goleiro'), ('ZC', 'Zagueiro'), ('LE', 'Lateral Esquerdo'), ('LD', 'Lateral Direito'), ('VOL', 'Volante'), ('MC', 'Meio Campo'), ('MAT', 'Meia Atacante'), ('PE', 'Ponta Esquerda'), ('PD', 'Ponta Direita'), ('CA', 'Centroavante')], default='GOL', max_length=3, verbose_name='Posição'),
        ),
        migrations.AddField(
            model_name='player',
            name='shooting',
            field=models.IntegerField(default='50', verbose_name='Chute'),
        ),
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.IntegerField(default='50', verbose_name='Peso'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(default='Fulano de Tal', max_length=255, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='player',
            name='rating',
            field=models.IntegerField(default='50', verbose_name='Overall'),
        ),
    ]
