
from django.contrib import admin

from .models import Student, Teacher

class TutoringInline(admin.TabularInline):
    model = Student.teacher.through
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [TutoringInline,]
    exclude = ('teacher',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [TutoringInline,]