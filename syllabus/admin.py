from django.contrib import admin
from .models import Faculty,Level,Program,Subject,Syllabus
# Register your models here.

#so that this will show in admin page
admin.site.register(Subject)
admin.site.register(Faculty)
admin.site.register(Level)
admin.site.register(Syllabus)
admin.site.register(Program)
