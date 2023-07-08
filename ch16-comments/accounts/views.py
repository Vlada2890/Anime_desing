from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, get_user_model
from django import forms


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home1')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "age",
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        UserModel = get_user_model()
        if UserModel.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})



class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField(required=True)


    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "age",
   
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        UserModel = get_user_model()
        if UserModel.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
