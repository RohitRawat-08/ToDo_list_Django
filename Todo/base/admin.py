from django.contrib import admin
from base.models import TodoModel ,DeleteModel,CompleteModel


# Register your models here.

admin.site.register(TodoModel)


class Ordering(admin.ModelAdmin):
    list_display=['title','desc']
    ordering = ['-id']  

admin.site.register(DeleteModel,Ordering)
admin.site.register(CompleteModel,Ordering)