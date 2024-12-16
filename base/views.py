from django.shortcuts import render,redirect
from .forms import Userdataform
from .models import Userdata
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def send_confirmation_email(email):
    subject = "Confirmation Email"
    message = "Thank you for submitting your data. We have received your information."
    from_email = settings.DEFAULT_FROM_EMAIL 
    
    
    send_mail(subject, message, from_email, [email])
def user_form_view(request):
    if request.method == 'POST':
        form = Userdataform(request.POST)
        if form.is_valid():
            form.save() 
            #send_confirmation_email(form.cleaned_data['email']) 
            return redirect('success')  
    else:
        form = Userdataform()

    return render(request, 'base/form.html', {'form': form})
def delete_user_view(request, user_id):
    user = Userdata.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'base/delete_user.html', {'user': user})




def success_view(request):
    return render(request, 'base/success.html')
def user_list_view(request):
    users = Userdata.objects.all()
    return render(request, 'base/user_list.html', {'users': users})
def edit_user_view(request, user_id):
    user = Userdata.objects.get(id=user_id)
    if request.method == 'POST':
        form = Userdataform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = Userdataform(instance=user)

    return render(request, 'base/edit_user.html', {'form': form})
def delete_user_view(request, user_id):
    user = Userdata.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'base/delete_user.html', {'user': user})