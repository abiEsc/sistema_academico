from django.contrib import admin
from .models import Question, Option, Character, VerseCard, GeneralQuestion, GeneralOption, Discurso

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Character)
admin.site.register(VerseCard)
admin.site.register(GeneralQuestion)
admin.site.register(GeneralOption)

@admin.register(Discurso)
class DiscursoAdmin(admin.ModelAdmin):
    list_display = ("cita_biblica", "tema_central", "orador", "audiencia")