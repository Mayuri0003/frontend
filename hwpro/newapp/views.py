from django.shortcuts import render,redirect
from newapp.forms  import NewUserForm
from django.urls import reverse_lazy
# Create your views here.
def newapp(request):
    return render (request,"newapp/index.html")

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, "newapp/landing.html")
        else:
            print('ERROR FORM IS INVALID')
     

    return render(request,'newapp/users.html',{'form': form})





    
