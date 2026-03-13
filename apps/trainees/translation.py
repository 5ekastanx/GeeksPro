from modeltranslation.translator import register, TranslationOptions
from apps.trainees.models import (
    Trainee, Role
)

@register(Trainee)
class TraineeTranslationOptions(TranslationOptions):
    fields = ('name', 'address')

@register(Role)
class RoleTranslationOptions(TranslationOptions):
    fields = ('name', )
