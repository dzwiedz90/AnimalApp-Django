from django.contrib import admin

from .models import RemedyForTicks, TreatmentAndDisease, Vaccine, VetClinic, DewormingRemedy

admin.site.register(RemedyForTicks)
admin.site.register(TreatmentAndDisease)
admin.site.register(Vaccine)
admin.site.register(VetClinic)
admin.site.register(DewormingRemedy)
