from django.forms import ModelForm

from .models import DewormingRemedy, RemedyForTicks, TreatmentAndDisease, Vaccine, VetClinic


class DewormingRemedyForm(ModelForm):
    class Meta:
        model = DewormingRemedy
        fields = ['deworming_remedy_name', 'description']


class RemedyForTicksForm(ModelForm):
    class Meta:
        model = RemedyForTicks
        fields = ['remedy_for_ticks_name', 'description']


class TreatmentAndDiseaseForm(ModelForm):
    class Meta:
        model = TreatmentAndDisease
        fields = ['treatment_and_disease_name', 'description']


class VaccineForm(ModelForm):
    class Meta:
        model = Vaccine
        fields = ['vaccine_name', 'description']


class VetClinicForm(ModelForm):
    class Meta:
        model = VetClinic
        fields = ['vet_clinic_name', 'address', 'phone_number', 'opening_hours']
