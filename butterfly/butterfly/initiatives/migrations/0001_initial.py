# Generated by Django 4.2.3 on 2023-07-31 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('participation_reason', models.TextField()),
                ('equipment', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('image', models.URLField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Animals', 'Animals'), ('Environment', 'Environment'), ('Healthcare', 'Healthcare'), ('Social', 'Social'), ('Society', 'Society')])),
                ('suitable_for', models.CharField(choices=[('Kids', 'Kids'), ('Teenagers', 'Teenagers'), ('Adults', 'Adults'), ('Elderly', 'Elderly'), ('Disabled people', 'Disabled people')])),
                ('region', models.CharField(choices=[('Bulgaria', 'Bulgaria'), ('Blagoevgrad', 'Blagoevgrad'), ('Burgas', 'Burgas'), ('Varna', 'Varna'), ('Veliko Turnovo', 'Veliko Turnovo'), ('Vidin', 'Vidin'), ('Vratsa', 'Vratsa'), ('Gabrovo', 'Gabrovo'), ('Dobrich', 'Dobrich'), ('Kurdzhali', 'Kurdzhali'), ('Kyustendil', 'Kyustendil'), ('Lovech', 'Lovech'), ('Montana', 'Montana'), ('Pazardzhik', 'Pazardzhik'), ('Pernik', 'Pernik'), ('Pleven', 'Pleven'), ('Plovdiv', 'Plovdiv'), ('Razgrad', 'Razgrad'), ('Ruse', 'Ruse'), ('Silistra', 'Silistra'), ('Sliven', 'Sliven'), ('Smolyan', 'Smolyan'), ('Sofia - city', 'Sofia - city'), ('Sofia - region', 'Sofia - region'), ('Stara Zagora', 'Stara Zagora'), ('Turgovishte', 'Turgovishte'), ('Haskovo', 'Haskovo'), ('Shumen', 'Shumen'), ('Yambol', 'Yambol')])),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('date_of_publication', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]