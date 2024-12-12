from django.shortcuts import render,redirect
from base.models import TodoModel,DeleteModel,CompleteModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#! Show all task
@login_required(login_url='LogIn')
def home(request):
    tasks_list = TodoModel.objects.all()
    if not TodoModel.objects.exists(): 
        msg = "No task Added Please Add Task"
        context={"data":msg}
        return render(request,"homeEmpty.html",context)
    else:
        context={"data":tasks_list}
        return render(request,"home.html",context)
       
        
#! add task 
@login_required(login_url='LogIn')
def addtask(request):
    a = TodoModel.objects.all()

    if request.method == "POST":
        title=request.POST['title']
        desc=request.POST['desc']

        for i in a:
            if title == i.title:
                ...
            
            # print(f"this is desc :{i['desc']}") 

        TodoModel.objects.create(title=title,desc=desc)
        return redirect("home")
    return render (request , "addtask.html")



#! Edit task
@login_required(login_url='LogIn')
def edittask(request,id):
    a = TodoModel.objects.get(id=id)
    if request.method == "POST":
        titleData = request.POST['title'] 
        descData = request.POST['desc']
        # print(titleData,descData)
        a.title = titleData
        a.desc = descData
        a.save()
        return redirect('home')
    return render (request , "edit.html" , context={'data':a})


#! show all Deleted task
@login_required(login_url='LogIn')
def taskHistory(request):
    data = DeleteModel.objects.all()
    return render (request , "history.html",context={'del_tsk':data})

#! This function will show conform msg beform delete all task from History page
@login_required(login_url='LogIn')
def conform_DeleteAll_Task_history(request):
    if request.method == 'POST':
        all_data = DeleteModel.objects.all()
        all_data.delete()
        return redirect('taskhistory')
    return render(request,"conform_DeleteAll_Task_history.html")


#! This function will show conform msg beform delete task from home page
@login_required(login_url='LogIn')
def conform(request,id):
    de = TodoModel.objects.get(id=id)
    
    if request.method == 'POST':
        DeleteModel.objects.create(title=de.title,desc=de.desc)
        de.delete()
        return redirect("taskhistory")

    return render(request,"conform.html")

#! This function will show conform msg beform delete single task from History page
@login_required(login_url='LogIn')
def conform_Delete_Task_history(request,id):
    de = DeleteModel.objects.get(id=id)
    if request.method == 'POST':
        de.delete()
        return redirect("taskhistory")
    return render(request,"conform_Delete_Task_history.html")
    


# ! This function give the logic to Task Completed button on home page
@login_required(login_url='LogIn')
def Complete_btn_on_home(request,id):
    com = TodoModel.objects.get(id=id)
    CompleteModel.objects.create(title=com.title,desc=com.desc)
    com.delete()
    return redirect('taskcomplete')

# ! This function show all task of the completed page
@login_required(login_url='LogIn')
def taskComplete(request):
    data = CompleteModel.objects.all()
    return render (request , "taskCompleted.html",context={'com_tsk':data})

#! This function will show conform msg beform delete All task from Completed task
@login_required(login_url='LogIn')
def conform_DeleteAll_Task_Complete(request):
    if request.method == "POST":
        all_data = CompleteModel.objects.all()
        all_data.delete()
        return redirect('taskcomplete')
    return render(request,"conform_DeleteAll_Task_Complete.html")

#! This function will show conform msg beform delete Single task from Completed Task
@login_required(login_url='LogIn')
def conform_Delete_Task_Complete(request,id):
    de = CompleteModel.objects.get(id=id)
    if request.method == 'POST':
        de.delete()
        return redirect("taskcomplete")
    return render(request,"conform_Delete_Task_Complete.html")

#! This function will resotre Single task from History task 
@login_required(login_url='LogIn')
def restore_single_history_task(request,id):
    data = DeleteModel.objects.get(id=id)
    TodoModel.objects.create(title=data.title,desc=data.desc)
    data.delete()

    return redirect('home')

#! This function will resotre Single task from Completed task
@login_required(login_url='LogIn') 
def restore_single_completed_task(request,id):
    data = CompleteModel.objects.get(id=id)
    TodoModel.objects.create(title=data.title,desc=data.desc)
    data.delete()

    return redirect('home')

#! This function will resotre all task from History 
@login_required(login_url='LogIn')
def Restore_all_HistoryTask(request):
    data = DeleteModel.objects.all()
    for i in data:
        TodoModel.objects.create(title=i.title,desc=i.desc)
    data.delete()

    return redirect('home')

#! This function will resotre all task from Completed task 
@login_required(login_url='LogIn')
def Restore_all_CompletedTask(request):
    data = CompleteModel.objects.all()
    for i in data:
        TodoModel.objects.create(title=i.title,desc=i.desc)
    data.delete()

    return redirect('home')

#! About Page
def About(request):
    return render (request , "about.html")