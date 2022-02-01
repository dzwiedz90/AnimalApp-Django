import pdb

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Animal, AnimalDeworming, AnimalTreatmentAndDisease, AnimalRemedyForTicks, AnimalVaccine, \
    AnimalWeight, AnimalGeneralInformation
from .forms import AnimalForm, AnimalDewormingForm, AnimalTreatmentAndDiseaseForm, AnimalRemedyForTicksForm, \
    AnimalVaccineForm, AnimalWeightForm, AnimalGeneralInformationForm


class IndexView(generic.ListView):
    template_name = 'animal_resources/index.html'
    context_object_name = 'animals_list'

    def get_queryset(self):
        return Animal.objects.all()


class AnimalDetailView(generic.DetailView):
    model = Animal
    template_name = 'animal_resources/animal_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['animals_list'] = Animal.objects.all()
        return context


class AnimalDewormingDetailView(generic.DetailView):
    model = AnimalDeworming
    template_name = 'animal_resources/animal_deworming_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dewormings_list'] = AnimalDeworming.objects.filter(animal_id=self.kwargs['pk'])
        return context


class AnimalDiseaseAndTreatmentDetailView(generic.DetailView):
    model = AnimalTreatmentAndDisease
    template_name = 'animal_resources/animal_disease_and_treatment_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['treatments_list'] = AnimalTreatmentAndDisease.objects.filter(animal_id=self.kwargs['pk'])
        return context


class AnimalRemediesForTicksDetailView(generic.DetailView):
    model = AnimalRemedyForTicks
    template_name = 'animal_resources/animal_remedies_for_ticks_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticks_list'] = AnimalRemedyForTicks.objects.filter(animal_id=self.kwargs['pk'])
        return context


class AnimalVaccineDetailView(generic.DetailView):
    model = AnimalVaccine
    template_name = 'animal_resources/animal_vaccine_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vaccines_list'] = AnimalVaccine.objects.filter(animal_id=self.kwargs['pk'])
        return context


class AnimalWeightDetailView(generic.DetailView):
    model = AnimalWeight
    template_name = 'animal_resources/animal_weight_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weight_list'] = AnimalWeight.objects.filter(animal_id=self.kwargs['pk'])
        return context


class AnimalGeneralInformationDetailView(generic.DetailView):
    model = AnimalGeneralInformation
    template_name = 'animal_resources/animal_general_information_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['information_list'] = AnimalGeneralInformation.objects.filter(animal_id=self.kwargs['pk'])
        return context


def create_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalForm()
    return render(request, 'animal_resources/create/create_animal.html', {'form': form})


def create_animal_deworming(request, pk):
    if request.method == 'POST':
        form = AnimalDewormingForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/dewormings/')
        else:
            # return HttpResponseRedirect('/animals/' + str(pk) + '/dewormings/')
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalDewormingForm()
    return render(request, 'animal_resources/create/create_animal_deworming.html', {'form': form, 'pk': pk})


def create_animal_treatment(request, pk):
    if request.method == 'POST':
        form = AnimalTreatmentAndDiseaseForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/treatments/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalTreatmentAndDiseaseForm()
    return render(request, 'animal_resources/create/create_animal_treatment.html', {'form': form, 'pk': pk})


def create_animal_remedy_for_ticks(request, pk):
    if request.method == 'POST':
        form = AnimalRemedyForTicksForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/ticks/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalRemedyForTicksForm()
    return render(request, 'animal_resources/create/create_animal_remedy_for_ticks.html', {'form': form, 'pk': pk})


def create_animal_vaccine(request, pk):
    if request.method == 'POST':
        form = AnimalVaccineForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/vaccines/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalVaccineForm()
    return render(request, 'animal_resources/create/create_animal_vaccine.html', {'form': form, 'pk': pk})


def create_animal_weight(request, pk):
    if request.method == 'POST':
        form = AnimalWeightForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/weight/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalWeightForm()
    return render(request, 'animal_resources/create/create_animal_weight.html', {'form': form, 'pk': pk})


def create_animal_general_information(request, pk):
    if request.method == 'POST':
        form = AnimalGeneralInformationForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/information/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalGeneralInformationForm()
    return render(request, 'animal_resources/create/create_animal_information.html', {'form': form, 'pk': pk})


def update_animal(request, pk):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/animal/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalForm()
    return render(request, 'animal_resources/modify/modify_animal.html', {'form': form, 'pk': pk})


def update_animal_deworming(request, pk):
    if request.method == 'POST':
        form = AnimalDewormingForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/dewormings/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalDewormingForm()
    return render(request, 'animal_resources/modify/modify_animal_deworming.html', {'form': form, 'pk': pk})


def update_animal_treatment(request, pk):
    if request.method == 'POST':
        form = AnimalTreatmentAndDiseaseForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/treatments/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalTreatmentAndDiseaseForm()
    return render(request, 'animal_resources/modify/modify_animal_treatment.html', {'form': form, 'pk': pk})


def update_animal_remedy_for_ticks(request, pk):
    if request.method == 'POST':
        form = AnimalRemedyForTicksForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/ticks/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalRemedyForTicksForm()
    return render(request, 'animal_resources/modify/modify_animal_remedy_for_ticks.html', {'form': form, 'pk': pk})


def update_animal_vaccine(request, pk):
    if request.method == 'POST':
        form = AnimalVaccineForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/vaccines/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalVaccineForm()
    return render(request, 'animal_resources/modify/modify_animal_vaccine.html', {'form': form, 'pk': pk})


def update_animal_weight(request, pk):
    if request.method == 'POST':
        form = AnimalWeightForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/weight/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalWeightForm()
    return render(request, 'animal_resources/modify/modify_animal_weight.html', {'form': form, 'pk': pk})


def update_animal_general_information(request, pk):
    if request.method == 'POST':
        form = AnimalGeneralInformationForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/animals/' + str(pk) + '/information/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = AnimalGeneralInformationForm()
    return render(request, 'animal_resources/modify/modify_animal_information.html', {'form': form, 'pk': pk})
