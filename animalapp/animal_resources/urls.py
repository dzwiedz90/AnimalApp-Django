from django.urls import path

from . import views

app_name = 'animals'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/animal/', views.AnimalDetailView.as_view(), name='animal_detail'),
    path('<int:pk>/dewormings/', views.AnimalDewormingDetailView.as_view(), name='animal_deworming_detail'),
    path('<int:pk>/treatments/', views.AnimalDiseaseAndTreatmentDetailView.as_view(),
         name='animal_disease_and_treatment_detail'),
    path('<int:pk>/ticks/', views.AnimalRemediesForTicksDetailView.as_view(), name='animal_remedies_for_ticks_detail'),
    path('<int:pk>/vaccines/', views.AnimalVaccineDetailView.as_view(), name='animal_vaccine_detail'),
    path('<int:pk>/weight/', views.AnimalWeightDetailView.as_view(), name='animal_weight_detail'),
    path('<int:pk>/information/', views.AnimalGeneralInformationDetailView.as_view(),
         name='animal_general_information_detail'),

    path('add/', views.create_animal, name='animal_form'),
    path('<int:pk>/dewormings/add/', views.create_animal_deworming, name='add_animal_deworming'),
    path('<int:pk>/treatments/add/', views.create_animal_treatment,
         name='add_animal_disease_and_treatment'),
    path('<int:pk>/ticks/add/', views.create_animal_remedy_for_ticks,
         name='add_animal_remedies_for_ticks'),
    path('<int:pk>/vaccines/add/', views.create_animal_vaccine, name='add_animal_vaccine'),
    path('<int:pk>/weight/add/', views.create_animal_weight, name='add_animal_weight'),
    path('<int:pk>/information/add/', views.create_animal_general_information,
         name='add_animal_general_information'),

    path('<int:pk>/animal/modify/', views.update_animal, name='animal_detail'),
    path('<int:pk>/dewormings/modify/', views.update_animal_deworming, name='modify_animal_deworming'),
    path('<int:pk>/treatments/modify/', views.update_animal_treatment, name='modify_animal_disease_and_treatment'),
    path('<int:pk>/ticks/modify/', views.update_animal_remedy_for_ticks, name='modify_animal_remedies_for_ticks'),
    path('<int:pk>/vaccines/modify/', views.update_animal_vaccine, name='modify_animal_vaccine'),
    path('<int:pk>/weight/modify/', views.update_animal_weight, name='modify_animal_weight'),
    path('<int:pk>/information/modify/', views.update_animal_general_information,
         name='modify_animal_general_information'),
]
