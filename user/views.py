from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def SignUp(request):
    # if request.method == 'GET':
    #     # return HttpResponse("11")
    #     return render(request, 'signup/signup.html')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # user = form.save()
            # login(request, user)
            return redirect('/case_list/')  # 회원 가입 후 리다이렉트할 URL을 지정해주세요.
        else:
            print(form.errors)
    else:
            form = SignUpForm()
    return render(request, 'signup/signup.html', {'form': form})

