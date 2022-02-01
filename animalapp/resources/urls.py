from django.urls import path

from . import views

app_name = 'resources'

urlpatterns = [
    path('', views.index, name='index'),
    path('dewormings/', views.DewormingRemediesIndexView.as_view(), name='dewormings_index'),
    path('ticks/', views.RemedyForTicksIndexView.as_view(), name='ticks_index'),
    path('treatments/', views.TreatmentAndDiseaseIndexView.as_view(), name='treatments_index'),
    path('vaccines/', views.VaccineIndexView.as_view(), name='vaccines_index'),
    path('clinics/', views.VetClinicIndexView.as_view(), name='clinics_index'),

    path('dewormings/<int:pk>/', views.DewormingRemediesDetailView.as_view(), name='dewormings_detail'),
    path('ticks/<int:pk>/', views.RemedyForTicksDetailView.as_view(), name='ticks_detail'),
    path('treatments/<int:pk>/', views.TreatmentAndDiseaseDetailView.as_view(), name='treatments_detail'),
    path('vaccines/<int:pk>/', views.VaccineDetailView.as_view(), name='vaccines_detail'),
    path('clinics/<int:pk>/', views.VetClinicDetailView.as_view(), name='clinics_detail'),

    path('dewormings/add/', views.create_deworming, name='add_deworming'),
    path('ticks/add/', views.create_tick, name='add_tick'),
    path('treatments/add/', views.create_treatment, name='add_treatment'),
    path('vaccines/add/', views.create_vaccine, name='add_vaccine'),
    path('clinics/add/', views.create_clinic, name='add_clinic'),

    path('dewormings/modify/', views.update_deworming, name='modify_deworming'),
    path('ticks/modify/', views.update_tick, name='modify_tick'),
    path('treatments/modify/', views.update_treatment, name='modify_treatment'),
    path('vaccines/modify/', views.update_vaccine, name='modify_vaccine'),
    path('clinics/modify/', views.update_clinic, name='modify_clinic'),
]
