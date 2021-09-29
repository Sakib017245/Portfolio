from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(About)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Summary)
admin.site.register(Education)
admin.site.register(ProfessionaExperience)
admin.site.register(Service)
admin.site.register(Project)

