from django.contrib import admin
from .models import Student, Recruiter, Job

# Register your models here.

# register recruiter model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['contact','gender','user_type','user']

# register recruiter model
@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ['contact','gender','user_type','company','status','user']

# register job model
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title','start_date','end_date','location','experience','salary','description','recruiter']