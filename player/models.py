from django.db import models

class Player(models.Model):
    GENDER_CHOICES={
        "male": "Masculino",
        "female": "Feminino", 
    }

    POSITION_CHOICES={
        "GK": "Goleiro",
        "CB": "Zagueiro",
        "LB": "Lateral Esquerdo",
        "RB": "Lateral Direito",
        "LWB": "Lateral Esquerdo Ofensivo",
        "RWB": "Lateral Direito Ofensivo",
        "CDM": "Volante",
        "CM": "Meio Campo",
        "CAM": "Meia Atacante",
        "LM": "Meia Lateral Esquerdo",
        "RM": "Meia Lateral Direito",
        "LW": "Ponta Esquerda",
        "RW": "Ponta Direita",
        "ST": "Atacante",
        "CA": "Centroavante",
    }

    FOOT_CHOICES={
    "left": "Esquerdo",
    "right": "Direito",
    }

    WORKRATE_CHOICES={
        "low": "Baixo",
        "medium": "Médio",
        "high": "Alto",
    }

    firstName = models.CharField(max_length=255, verbose_name="Nome", default="Fulano",)
    lastName = models.CharField(max_length=255, verbose_name="Sobrenome", default="de Tal",)
    name = models.CharField(max_length=255, verbose_name="Nome Completo", default="Fulano de Tal",)
    height = models.IntegerField(verbose_name="Altura", default="150",)
    weight = models.IntegerField(verbose_name="Peso", default="50")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name="Gênero", default="M")
    birthDate = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento",)
    league = models.CharField(max_length=255, verbose_name="Liga", default="Liga ABC")
    nation = models.CharField(max_length=255, verbose_name="Nacionalidade", default="Desconhecido",)
    club = models.CharField(max_length=255, verbose_name="Time", default="Sem Time")
    position = models.CharField(max_length=3, choices=POSITION_CHOICES, verbose_name="Posição", default="GOL")
    foot = models.CharField(max_length=5, choices=FOOT_CHOICES, verbose_name="Pé Dominante", default="D")
    attackWorkRate = models.CharField(max_length=6, choices=WORKRATE_CHOICES, verbose_name="Dedicação Ofensiva", default="M")
    defenseWorkRate = models.CharField(max_length=6, choices=WORKRATE_CHOICES, verbose_name="Dedicação Defensiva", default="M")
    rating = models.IntegerField(verbose_name="Overall", default="50",)
    pace = models.IntegerField(verbose_name="Ritmo", default="50",)
    shooting = models.IntegerField(verbose_name="Chute", default="50",)
    passing = models.IntegerField(verbose_name="Passe", default="50",)
    dribbling = models.IntegerField(verbose_name="Drible", default="50",)
    defending = models.IntegerField(verbose_name="Marcação", default="50",)
    physicality = models.IntegerField(verbose_name="Físico", default="50",)



