from datetime import date

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Initiative(models.Model):

    KIDS = 'Kids'
    TEENAGERS = 'Teenagers'
    ADULTS = 'Adults'
    ELDERLY = 'Elderly'
    DISABLED_PEOPLE = 'Disabled people'

    GROUPS = (
        (KIDS, KIDS),
        (TEENAGERS, TEENAGERS),
        (ADULTS, ADULTS),
        (ELDERLY, ELDERLY),
        (DISABLED_PEOPLE, DISABLED_PEOPLE)
    )

    ANIMALS = 'Animals'
    ENVIRONMENT = 'Environment'
    HEALTHCARE = 'Healthcare'
    SOCIAL = 'Social'
    SOCIETY = 'Society'

    CATEGORIES = (
        (ANIMALS, ANIMALS),
        (ENVIRONMENT, ENVIRONMENT),
        (HEALTHCARE, HEALTHCARE),
        (SOCIAL, SOCIAL),
        (SOCIETY, SOCIETY),
    )


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

    REGIONS = (
        (BULGARIA, BULGARIA),
        (BLAGOEVGRAD, BLAGOEVGRAD),
        (BURGAS, BURGAS),
        (VARNA, VARNA),
        (VELIKO_TARNOVO, VELIKO_TARNOVO),
        (VIDIN, VIDIN),
        (VRATSA, VRATSA),
        (GABROVO, GABROVO),
        (DOBRICH, DOBRICH),
        (KARDZHALI, KARDZHALI),
        (KYUSTENDIL, KYUSTENDIL),
        (LOVECH, LOVECH),
        (MONTANA, MONTANA),
        (PAZARDZHIK, PAZARDZHIK),
        (PERNIK, PERNIK),
        (PLEVEN, PLEVEN),
        (PLOVDIV, PLOVDIV),
        (RAZGRAD, RAZGRAD),
        (RUSSE, RUSSE),
        (SILISTRA, SILISTRA),
        (SLIVEN, SLIVEN),
        (SMOLYAN, SMOLYAN),
        (SOFIA, SOFIA),
        (SOFIA_OBLAST, SOFIA_OBLAST),
        (STARA_ZAGORA, STARA_ZAGORA),
        (TARGOVISHTE, TARGOVISHTE),
        (HASKOVO, HASKOVO),
        (SHUMEN, SHUMEN),
        (YAMBOL, YAMBOL),
    )

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
        choices=CATEGORIES,
        null=False,
        blank=False,
    )

    suitable_for = models.CharField(
        choices=GROUPS,
        null=False,
        blank=False,
    )

    region = models.CharField(
        choices=REGIONS,
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
        on_delete=models.DO_NOTHING,
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
        on_delete=models.DO_NOTHING,
    )
