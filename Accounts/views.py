from django.shortcuts import render,reverse,get_object_or_404
from django.views.generic import View
from .forms import UserForm,UserProfileForm,ProfileUpdate,PasswordUpdate,ContactForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import UserProfile 
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Login(View):
    template_name='Accounts/login.html'
    form_class=AuthenticationForm
    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})
    def post(self,request):
            username=self.request.POST['username']
            password=self.request.POST['password']
            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Invalid Credentials')
                return redirect('login')


class Register(View):
    template_name='Accounts/registration.html'
    user_form=UserForm
    profile_form=UserProfileForm
    def get(self,request):
        return render(request,self.template_name,{'user_form':self.user_form,'profile_form':self.profile_form })

    def post(self,request):
        user_form=UserForm(request.POST)
        profile_form=UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            if user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
                user=user_form.save() # saving user_form to the database
                user.set_password(user.password)#hashing the pwd
                user.save() #save changes to the user

                profile=profile_form.save(commit=False)
                profile.user=user

                if 'profile_pic' in request.FILES:
                    profile.profile_pic=request.FILES['profile_pic']

                    profile.save()
                return redirect('login')
            else:
                messages.error(request,'Passwords do not match')
                return render(request,self.template_name,
                        {'user_form':self.user_form,'profile_form':self.profile_form})
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,self.template_name,
                        {'user_form':self.user_form,'profile_form':self.profile_form})


class Logout(View):
    def get(self,request):
        logout(request)
        return render(request,'Tik/home.html')

class UserProfileView(View):
    template_name='Accounts/user_profile.html'
    def get(self,request,username):
        user=get_object_or_404(User,username=username)
        userprofile=get_object_or_404(UserProfile,user=user)
        return render(request,self.template_name,{"userprofile":userprofile,"user":user})


class ProfileUpdateView(LoginRequiredMixin,View):
    template_name='Accounts/update_profile.html'
    def get(self,request):
        update_bound_form=ProfileUpdate(instance=request.user)
        profile_bound_form=UserProfileForm(instance=request.user.userprofile)
        return render(request,self.template_name,{"update_form":update_bound_form,"user_profile":profile_bound_form})

    def post(self,request):
        update_form=ProfileUpdate(request.POST,instance=request.user)
        profile_form=UserProfileForm(request.POST,instance=request.user.userprofile)
        if update_form.is_valid() and profile_form.is_valid():
            user=update_form # saving user_form to the database
            user.save() 
            profile=profile_form
            profile.save()
            return redirect('login')
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,self.template_name,{'user_form':update_form,'profile_form':profile_form})


class PasswordUpdateView(LoginRequiredMixin,View):
    template_name='Accounts/update_password.html'
    form_class=PasswordUpdate
    def get(self,request):
        return render(request,self.template_name,{'password_form':self.form_class()})
    
    def post(self,request):
        update_form=PasswordUpdate(request.POST,instance=request.user)
        if update_form.is_valid():
            if update_form.cleaned_data['password'] == update_form.cleaned_data['confirm_password']:
                user=update_form.save()
                user.set_password(user.password)
                user.save()
                return redirect('login')
            else:
                messages.error(request,"Two passwords should match!")
                return redirect('update_password')


class ContactUsView(View):
    template_name='Accounts/contact.html'
    form_class=ContactForm

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class()})

    def post(self,request):
        bound_form=self.form_class(request.POST)
        if bound_form.is_valid():
            mail_sent=bound_form.send_mail()
            if mail_sent:
                messages.success(request,'Successfully sent.')
                return redirect('home')

        return render (request,self.template_name,{'form':bound_form})
