from django.contrib import admin
from home.models import UserProfile, Problem, Answer, Teacher, Comment

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Problem)
admin.site.register(Answer)
admin.site.register(Teacher)
admin.site.register(Comment)
