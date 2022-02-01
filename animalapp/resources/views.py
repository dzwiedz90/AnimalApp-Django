from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from .models import DewormingRemedy, RemedyForTicks, TreatmentAndDisease, Vaccine, VetClinic
from .forms import DewormingRemedyForm, RemedyForTicksForm, TreatmentAndDiseaseForm, VaccineForm, VetClinicForm


def index(request):
    return HttpResponseRedirect('/resources/dewormings/')


class DewormingRemediesIndexView(generic.ListView):
    template_name = 'resources/deworming_remedy_index.html'
    context_object_name = 'deworming_remedies_list'

    def get_queryset(self):
        return DewormingRemedy.objects.all()


class RemedyForTicksIndexView(generic.ListView):
    template_name = 'resources/remedy_for_ticks_index.html'
    context_object_name = 'remedy_for_ticks_list'

    def get_queryset(self):
        return RemedyForTicks.objects.all()


class TreatmentAndDiseaseIndexView(generic.ListView):
    template_name = 'resources/treatment_and_disease_index.html'
    context_object_name = 'treatments_list'

    def get_queryset(self):
        return TreatmentAndDisease.objects.all()


class VaccineIndexView(generic.ListView):
    template_name = 'resources/vaccine_index.html'
    context_object_name = 'vaccines_list'

    def get_queryset(self):
        return Vaccine.objects.all()


class VetClinicIndexView(generic.ListView):
    template_name = 'resources/vet_clinic_index.html'
    context_object_name = 'vet_clinic_list'

    def get_queryset(self):
        return VetClinic.objects.all()


class DewormingRemediesDetailView(generic.DetailView):
    model = DewormingRemedy
    template_name = 'resources/deworming_remedy_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dewormings_list'] = DewormingRemedy.objects.filter(id=self.kwargs['pk'])
        return context


class RemedyForTicksDetailView(generic.DetailView):
    model = RemedyForTicks
    template_name = 'resources/remedy_for_ticks_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticks_list'] = RemedyForTicks.objects.filter(id=self.kwargs['pk'])
        return context


class TreatmentAndDiseaseDetailView(generic.DetailView):
    model = TreatmentAndDisease
    template_name = 'resources/treatment_and_disease_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['treatments_list'] = TreatmentAndDisease.objects.filter(id=self.kwargs['pk'])
        return context


class VaccineDetailView(generic.DetailView):
    model = Vaccine
    template_name = 'resources/vaccine_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vaccines_list'] = Vaccine.objects.filter(id=self.kwargs['pk'])
        return context


class VetClinicDetailView(generic.DetailView):
    model = VetClinic
    template_name = 'resources/vet_clinic_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vet_clinics_list'] = VetClinic.objects.filter(id=self.kwargs['pk'])
        return context


def create_deworming(request):
    if request.method == 'POST':
        form = DewormingRemedyForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/resources/dewormings/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = DewormingRemedyForm()
    return render(request, 'resources/create/create_deworming_remedy.html', {'form': form})


def create_tick(request):
    if request.method == 'POST':
        form = RemedyForTicksForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/resources/ticks/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = RemedyForTicksForm()
    return render(request, 'resources/create/create_remedy_for_ticks.html', {'form': form})


def create_treatment(request):
    if request.method == 'POST':
        form = TreatmentAndDiseaseForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/resources/treatments/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = TreatmentAndDiseaseForm()
    return render(request, 'resources/create/create_treatment_and_disease.html', {'form': form})


def create_vaccine(request):
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/resources/vaccines/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = VaccineForm()
    return render(request, 'resources/create/create_vaccine.html', {'form': form})


def create_clinic(request):
    if request.method == 'POST':
        form = VetClinicForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/resources/clinics/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = VetClinicForm()
    return render(request, 'resources/create/create_vet_clinic.html', {'form': form})


def update_deworming(request):
    if request.method == 'POST':
        form = DewormingRemedyForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/resources/dewormings/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = DewormingRemedyForm()
    return render(request, 'resources/create/create_deworming_remedy.html', {'form': form})


def update_tick(request):
    if request.method == 'POST':
        form = RemedyForTicksForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/resources/ticks/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = RemedyForTicksForm()
    return render(request, 'resources/create/create_remedy_for_ticks.html', {'form': form})


def update_treatment(request):
    if request.method == 'POST':
        form = TreatmentAndDiseaseForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/resources/treatments/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = TreatmentAndDiseaseForm()
    return render(request, 'resources/create/create_treatment_and_disease.html', {'form': form})


def update_vaccine(request):
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/resources/vaccines/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = VaccineForm()
    return render(request, 'resources/create/create_vaccine.html', {'form': form})


def update_clinic(request):
    if request.method == 'POST':
        form = VetClinicForm(request.POST)
        if form.is_valid():
            form.save(request.POST)
            return HttpResponseRedirect('/resources/clinics/')
        else:
            return HttpResponse(content='Niepoprawne dane', status=400)
    else:
        form = VetClinicForm()
    return render(request, 'resources/create/create_vet_clinic.html', {'form': form})
