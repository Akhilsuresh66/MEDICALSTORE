
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from.forms import AccountForm 


#home page
def medical(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            acc = form.save()
            return render(request,'form-data.html',{
                'message': 'Data saved to db' ,
                'Account':acc          })
    else:
        form = AccountForm()
    return render(request,'index.html',{'form':form})

#login page

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

class AccountUserCreationForm(UserCreationForm):
    def _init_(self,*args,**kwargs):
        super()._init_(*args,**kwargs)
        self.fields['password1'].help_text=None
        self.fields['password2'].help_text=None
        self.fields['username'].label=None

#signup page
def signup_page(request):
    if request.method == 'POST':
        form = AccountUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()  
            login(request, user)
            return redirect('login')
    else:
        form = AccountUserCreationForm()
    return render(request, 'signup.html', {'form': form})
