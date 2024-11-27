
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('addtask',views.addtask,name='addtask'),
    path('Edittask/<int:id>',views.edittask,name='edittask'),

    path('taskHistory',views.taskHistory,name='taskhistory'),
    path('taskHistory_del/<int:id>',views.task_His_del,name='delete'),


    path('taskComplete',views.taskComplete,name='taskcomplete'),
    path('taskComplete_add/<int:id>',views.Complete,name='complete'),

    path('about',views.About,name='about'),
]
