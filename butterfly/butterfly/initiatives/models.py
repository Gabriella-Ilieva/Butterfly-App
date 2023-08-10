from datetime import date
from enum import Enum
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Groups(Enum):
    KIDS = 'Kids'
    TEENAGERS = 'Teenagers'
    ADULTS = 'Adults'
    ELDERLY = 'Elderly'
    DISABLED_PEOPLE = 'Disabled people'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class Regions(Enum):
    BULGARIA = "Bulgaria"
    BLAGOEVGRAD = "Blagoevgrad"
    BURGAS = "Burgas"
    VARNA = "Varna"
    VELIKO_TARNOVO = "Veliko Turnovo"
    VIDIN = "Vidin"
    VRATSA = "Vratsa"
    GABROVO = "Gabrovo"
    DOBRICH = "Dobrich"
    KARDZHALI = "Kurdzhali"
    KYUSTENDIL = "Kyustendil"
    LOVECH = "Lovech"
    MONTANA = "Montana"
    PAZARDZHIK = "Pazardzhik"
    PERNIK = "Pernik"
    PLEVEN = "Pleven"
    PLOVDIV = "Plovdiv"
    RAZGRAD = "Razgrad"
    RUSSE = "Ruse"
    SILISTRA = "Silistra"
    SLIVEN = "Sliven"
    SMOLYAN = "Smolyan"
    SOFIA = "Sofia - city"
    SOFIA_OBLAST = "Sofia - region"
    STARA_ZAGORA = "Stara Zagora"
    TARGOVISHTE = "Turgovishte"
    HASKOVO = "Haskovo"
    SHUMEN = "Shumen"
    YAMBOL = "Yambol"

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class Categories(Enum):
    ANIMALS = 'Animals'
    ENVIRONMENT = 'Environment'
    HEALTHCARE = 'Healthcare'
    SOCIETY = 'Society'
    OTHER = 'Other'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class Initiative(models.Model):

    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    participation_reason = models.TextField(
        null=False,
        blank=False,
    )

    equipment = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    skills = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=True,
        blank=True,
    )

    category = models.CharField(
        choices=Categories.choices(),
        null=False,
        blank=False,
    )

    suitable_for = models.CharField(
        choices=Groups.choices(),
        null=False,
        blank=False,
    )

    region = models.CharField(
        choices=Regions.choices(),
        null=False,
        blank=False,
    )

    from_date = models.DateField(
        null=False,
        blank=False,
    )

    to_date = models.DateField(
        null=False,
        blank=False,
    )

    date_of_publication = models.DateField(auto_now=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-date_of_publication',)

    @property
    def view_count(self):
        return Participation.objects.filter(to_initiative=self).count()

    @property
    def is_expired(self):
        return self.to_date < date.today()


class Participation(models.Model):
    to_initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('user',)
