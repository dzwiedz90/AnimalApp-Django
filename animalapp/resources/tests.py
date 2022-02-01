from django.test import TestCase

from .models import RemedyForTicks, TreatmentAndDisease, Vaccine, VetClinic, DewormingRemedy


def create_remedy_for_ticks():
    return RemedyForTicks.objects.create(remedy_for_ticks_name=' remedy for ticks name',
                                         description='remedy for ticks description')


class RemedyForTicksTests(TestCase):
    pass


def create_treatment_and_disease():
    return TreatmentAndDisease.objects.create(treatment_and_disease_name='treatment and disease name',
                                              description='treatment and disease description')


class TreatmentAndDiseasesTests(TestCase):
    pass


def create_vaccine():
    return Vaccine.objects.create(vaccine_name='vaccine name', description='vaccine description')


class VaccineTests(TestCase):
    pass


def create_vet_clinic():
    return VetClinic.objects.create(vet_clinic_name='vet clinic name', address='vet clinic address',
                                    phone_number='vet clinic phone number',
                                    opening_hours='vet clinic opening hours')


class VetClinicTests(TestCase):
    pass


def create_deworming_remedy():
    return DewormingRemedy.objects.create(deworming_remedy_name='deworming remedy name',
                                          description='deworming remedy description')


class DewormingRemedyTests(TestCase):
    pass
