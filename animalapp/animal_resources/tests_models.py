import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

import resources.tests

from .models import Animal, AnimalDeworming, AnimalTreatmentAndDisease, AnimalRemedyForTicks, AnimalVaccine, \
    AnimalWeight, AnimalGeneralInformation


def create_animal(date_born):
    return Animal.objects.create(animal_name='Kitten', species='kot', breed='europejski', gender='ML',
                                 date_born=date_born, current_weight='10', fur_ointment='bialy', is_archived=False)


class AnimalModelTests(TestCase):

    def test_animal_with_future_born_date(self):
        """
            Animal with future date born cannot be created
        """
        animal = create_animal(timezone.now()+datetime.timedelta(days=90))
        print(animal.date_born)
        self.assertEqual(u'Animal with future date born cannot be created', create_animal(timezone.now()+datetime.timedelta(days=90)))


class AnimalDewormingModelTests(TestCase):

    def create_animal_deworming(self, days):
        return AnimalDeworming.objects.create(animal=create_animal(), deworming_date=timezone.now(),
                                              deworming_expiration_date=timezone.now() + datetime.timedelta(days=days),
                                              deworming_remedy=resources.tests.create_deworming_remedy())


class AnimalTreatmentAndDiseaseModelTests(TestCase):

    def create_animal_treatment_and_disease(self):
        return AnimalTreatmentAndDisease.objects.create(animal=create_animal(),
                                                        treatment_and_disease=resources.tests.create_treatment_and_disease(),
                                                        vet_clinic=resources.tests.create_vet_clinic(),
                                                        date_occuredd=timezone.now(),
                                                        date_treated=timezone.now() + datetime.timedelta(days=14),
                                                        meds_given='meds given', treatment_cost=150.35,
                                                        description='glowka obcieta', satisfaction=7,
                                                        doctor='Doctore Dottore')


class AnimalRemedyForTicksModelTests(TestCase):

    def create_animal_remedy_for_ticks(self):
        return AnimalRemedyForTicks.objects.create(animal=create_animal(),
                                                   remedy_for_ticks=resources.tests.create_remedy_for_ticks(),
                                                   application_date=timezone.now(),
                                                   expiration_date=timezone.now() + datetime.timedelta(days=90))


class AnimalVaccineModelTests(TestCase):

    def create_animal_vaccine(self):
        return AnimalVaccine.objects.create(animal=create_animal(), vaccine=resources.tests.create_vaccine(),
                                            date_of_vaccination=timezone.now(),
                                            date_of_expiration=timezone.now() + datetime.timedelta(days=90))


class AnimalWeightModelTests(TestCase):

    def create_animal_weight(self):
        return AnimalWeight.objects.create(animal=create_animal(), date_of_measurement=timezone.now(), weight=12.0)


class AnimalGeneralInformationModelTests(TestCase):

    def create_animal_general_information(self):
        return AnimalGeneralInformation.objects.create(animal=create_animal(), content='genereal information')
