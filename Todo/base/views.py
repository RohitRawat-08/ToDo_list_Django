from django.shortcuts import render,redirect
from base.models import TodoModel,DeleteModel,CompleteModel
# Create your views here.


def home(request):

    tasks_list = TodoModel.objects.all()
    
    context={"data":tasks_list}
    return render(request,"home.html",context)



def addtask(request):

    if request.method == "POST":
        title=request.POST['title']
        desc=request.POST['desc']

        # print(title,desc)

        TodoModel.objects.create(title=title,desc=desc)

    return render (request , "addtask.html")


def edittask(request,id):
    a = TodoModel.objects.get(id=id)
    
    print(a.title)
    print(a.desc)

    if request.method == "POST":
        titleData = request.POST['title'] 
        descData = request.POST['desc']
        print(titleData,descData)
        a.title = titleData
        a.desc = descData

        a.save()
        return redirect('home')
    
    return render (request , "edit.html" , context={'data':a})




def taskHistory(request):
    data = DeleteModel.objects.all()
    # print(delt)
    return render (request , "history.html",context={'del_tsk':data})

def task_His_del(request,id):
    de = TodoModel.objects.get(id=id)
    DeleteModel.objects.create(title=de.title,desc=de.desc)
    de.delete()

    return redirect('taskhistory')
    


def Complete(request,id):
    com = TodoModel.objects.get(id=id)
    DeleteModel.objects.create(title=com.title,desc=com.desc)
    CompleteModel.objects.create(title=com.title,desc=com.desc)
    com.delete()
    
    return redirect('taskcomplete')


def taskComplete(request):
    data = CompleteModel.objects.all()
    return render (request , "taskCompleted.html",context={'com_tsk':data})



def About(request):
    return render (request , "about.html")