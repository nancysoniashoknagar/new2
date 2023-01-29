from django.contrib import admin
from aap1.models import Student,Games

class StudentAdmin(admin.ModelAdmin):
    list_display= ('name','rollno','phone')

class GamesAdmin(admin.ModelAdmin):
    list_display=('gamename','point')

admin.site.register(Student,StudentAdmin)
admin.site.register(Games,GamesAdmin)

# Register your models here.