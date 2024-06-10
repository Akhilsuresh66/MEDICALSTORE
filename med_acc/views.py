from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import MedicineForm
from .models import Medicine
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

#home
@login_required(login_url='login')
def home(request):
    list_medicine=Medicine.objects.all()
    return render(request,'home.html',{'list_medicine':list_medicine})


#add medicines
@login_required(login_url='login')
def create_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =MedicineForm()
    return render(request, 'create.html', {'form': form})



#update medicines
def update_med(request, pk):
    medicines = Medicine.objects.get(pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST,instance=medicines)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =MedicineForm(instance=medicines)           
    return render(request, 'edit.html', {'form': form})


#delete medicines
@login_required(login_url='login')
def del_medicine(request,pk):
    medicine = Medicine.objects.get(pk=pk)
    if request.method == 'POST':
        medicine.delete()
        return redirect('home')
        
    return render(request,'delete.html',{'medicine':medicine})

#search medicine
@login_required(login_url='login')
def search_medicine(request):
    query = request.GET.get('query')
    medicines = Medicine.objects.filter(name__istartswith=query)
    return render(request, 'search.html', {'medicines': medicines})

#logout
@login_required(login_url='/login/')
def user_logout(request):
        logout(request)
        return redirect('login')