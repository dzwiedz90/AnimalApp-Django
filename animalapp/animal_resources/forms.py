from django.forms import ModelForm
from .models import Animal, AnimalDeworming, AnimalTreatmentAndDisease, AnimalRemedyForTicks, AnimalVaccine, \
    AnimalWeight, AnimalGeneralInformation


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['animal_name', 'species', 'breed', 'gender', 'date_born', 'current_weight', 'fur_ointment',
                  'is_archived', 'photo']


class AnimalDewormingForm(ModelForm):
    class Meta:
        model = AnimalDeworming
        fields = ['animal', 'id', 'deworming_date', 'deworming_expiration_date', 'deworming_remedy']


class AnimalTreatmentAndDiseaseForm(ModelForm):
    class Meta:
        model = AnimalTreatmentAndDisease
        fields = ['animal', 'treatment_and_disease', 'vet_clinic', 'date_occurred', 'date_treated', 'meds_given',
                  'treatment_cost', 'description', 'satisfaction', 'doctor']


class AnimalRemedyForTicksForm(ModelForm):
    class Meta:
        model = AnimalRemedyForTicks
        fields = ['animal', 'remedy_for_ticks', 'application_date', 'expiration_date']


class AnimalVaccineForm(ModelForm):
    class Meta:
        model = AnimalVaccine
        fields = ['animal', 'vaccine', 'date_of_vaccination', 'date_of_expiration']


class AnimalWeightForm(ModelForm):
    class Meta:
        model = AnimalWeight
        fields = ['animal', 'date_of_measurement', 'weight']


class AnimalGeneralInformationForm(ModelForm):
    class Meta:
        model = AnimalGeneralInformation
        fields = ['animal', 'content']
