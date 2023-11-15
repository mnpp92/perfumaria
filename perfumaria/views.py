from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from django.shortcuts import redirect
from perfumaria.forms import RegisterForm, LoginForm
from django.contrib import messages





def home_view(request):

    return render(request, 'home.html')


def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            request.session['message'] = "registro bem sucedido!"
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register_view.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('fome_page')
    return render(request, 'login.html')


def login_form_view(request):
    user = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "logado com Sucesso")
                return redirect('/')
        
            else:
                messages.error(request, "usuário ou senha invalidos")
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'login_3.html', context) 