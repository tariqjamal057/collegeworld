from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .token import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.forms import AuthenticationForm


@login_required(login_url = 'login')
def home(request):
    return HttpResponse("Hello world")
 

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').strip().lower()
            email_id = (form.cleaned_data.get('email').strip()).lower()
            password1 = form.cleaned_data.get('password1').strip()
            '''
            Need to write validation for check field existrency
            '''
            # user, created = User.objects.get_or_create(username=username, email=email_id, first_name = first_name, last_name=last_name, is_active=False)
            # user.set_password(password1)
            # user.save()

            # current_site = get_current_site(request)
            # mail_subject = 'Activation link has been sent to your email id'
            # message = render_to_string('auth/account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(
            #     mail_subject, message, to = [to_email]
            # )
            # email.send()

            return redirect('account-verification')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'auth/register.html', context)


def account_verify(request):
    return render(request, 'auth/verification_email_send.html')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'auth/account_activation_success.html', {"is_success": True, "username": user.username})
    else:
        return render(request, 'auth/account_activation_success.html', {"is_success": False})


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('password').strip()
        print(email)
        print(password)
        if User.objects.filter(email=email).exists():
            check_user = User.objects.get(email=email)
            if check_user.is_active:
                user = authenticate(request, username=check_user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'Password is incorrect')
            else:
                messages.info(request, 'Please verify your account before login')
        else:
            messages.error(request, 'Email does not exists')
    return render(request, 'auth/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
