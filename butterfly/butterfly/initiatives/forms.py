from django import forms

from butterfly.initiatives.models import Initiative


class CreateInitiativeForm(forms.ModelForm):

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

    # title = forms.CharField()
    # description = forms.TextInput()
    # participation_reason = forms.TextInput()
    # equipment = forms.CharField()
    # skills = forms.CharField()
    # image = forms.URLInput()
    # category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CATEGORIES)
    # suitable_for = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=GROUPS)
    # region = forms.ChoiceField(choices=REGIONS)
    # from_date = forms.DateInput()
    # to_date = forms.DateInput()

    class Meta:
        model = Initiative
        exclude = ['date_of_publication', 'user']

        widgets = {
            'from_date': forms.DateInput(
                attrs={
                    'placeholder': 'When the initiative starts?',
                    'type': 'date'
                }
            ),
            'to_date': forms.DateInput(
                attrs={
                    'placeholder': 'When the initiative ends?',
                    'type': 'date'
                }
            ),
        }


class EditInitiativeForm(forms.ModelForm):
    class Meta:
        model = Initiative
        exclude = ['date_of_publication', 'user']
