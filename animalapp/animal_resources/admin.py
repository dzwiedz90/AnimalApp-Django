from django.contrib import admin

from .models import Animal, AnimalDeworming, AnimalTreatmentAndDisease, AnimalRemedyForTicks, AnimalVaccine, \
    AnimalWeight, AnimalGeneralInformation


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('pk', 'animal_name')
    search_fields = ['animal_name']
    fieldsets = [
        (None, {'fields': ['animal_name']}),
        ('Species and gender', {'fields': ['species', 'breed', 'gender']}),
        ('Life dates', {'fields': ['date_born', 'date_died']}),
        ('Biological data ', {'fields': ['current_weight', 'fur_ointment']}),
        ('Other', {'fields': ['is_archived']}),
        (None, {'fields': ['photo']})
    ]


class AnimalVaccineAdmin(admin.ModelAdmin):
    list_display = ('pk', 'animal_name', 'vaccine_name')


class AnimalDewormingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'animal_name', 'deworming_remedy_name')


class AnimalGeneralInformationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'animal_name')


class AnimalRemedyForTicksAdmin(admin.ModelAdmin):
    list_display = ('pk', 'animal_name', 'remedy_for_ticks_name')


class AnimalTreatmentAndDiseaseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'animal_name', 'treatment_and_disease_name')


class AnimalWeightAdmin(admin.ModelAdmin):
    list_display = ('pk', 'animal_name')


admin.site.register(Animal, AnimalAdmin)
admin.site.register(AnimalDeworming, AnimalDewormingAdmin)
admin.site.register(AnimalTreatmentAndDisease, AnimalTreatmentAndDiseaseAdmin)
admin.site.register(AnimalRemedyForTicks, AnimalRemedyForTicksAdmin)
admin.site.register(AnimalVaccine, AnimalVaccineAdmin)
admin.site.register(AnimalWeight, AnimalWeightAdmin)
admin.site.register(AnimalGeneralInformation, AnimalGeneralInformationAdmin)
