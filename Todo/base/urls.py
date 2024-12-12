
from django.urls import path
from . import views

urlpatterns = [
    
    path('home',views.home,name='home'),
    path('addtask',views.addtask,name='addtask'),
    path('Edittask/<int:id>',views.edittask,name='edittask'),
    path('about',views.About,name='about'),

    path('taskHistory',views.taskHistory,name='taskhistory'),
    path('taskHistory_del/<int:id>',views.conform,name='conform'),
    path('taskComplete',views.taskComplete,name='taskcomplete'),
    path('taskComplete_add/<int:id>',views.Complete_btn_on_home,name='complete'), 

    path('restore_single_history_task<int:id>',views.restore_single_history_task,name='restore_single_history_task'),
    path('restore_single_completed_task<int:id>',views.restore_single_completed_task,name='restore_single_completed_task'),
    path('Restore_all_HistoryTask',views.Restore_all_HistoryTask,name='Restore_all_HistoryTask'),
    path('Restore_all_CompletedTask',views.Restore_all_CompletedTask,name='Restore_all_CompletedTask'),
    
    path('conform_Delete_Task_history/<int:id>',views.conform_Delete_Task_history,name='conform_Delete_Task_history'),
    path('conform_Delete_Task_Complete/<int:id>',views.conform_Delete_Task_Complete,name='conform_Delete_Task_Complete'),
    path('conform_DeleteAll_Task_Complete',views.conform_DeleteAll_Task_Complete,name='conform_DeleteAll_Task_Complete'),
    path('conform_DeleteAll_Task_history',views.conform_DeleteAll_Task_history,name='conform_DeleteAll_Task_history'),

]
