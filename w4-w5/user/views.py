from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.db import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required

from .forms import LoginForm
from .forms import CustomUserCreationForm

User = get_user_model()
#
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            # logout(request)
            return redirect('/')
        form = LoginForm()
        print(form.as_p())
        next_url = request.GET.get('next', '')
        context = {
            'form': form,
            'next_url': next_url
        }
        return render(request, 'user/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "login successfully!")
                next_url = request.GET.get('next', None)
                if next_url:
                    return redirect(next_url)
                return redirect('/')
            else:
                return redirect('login')

#
# class SignUp(View):
#     def get(self, request):
#         form = CustomUserCreationForm()
#         context = {
#             'form': form
#         }
#
#         return render(request, 'signup.html', context)
#
#     def post(self, request):
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#
#         context = {
#             'form': form
#         }
#         return render(request, 'user/signup.html', context)
#
#
def logout_view(request):
    logout(request)
    return redirect('user-view')

#
# @login_required(login_url='login')
# # @permission_required('user_profile.can_dance',  raise_exception=True)
# def gher_umdan(request):
#     if request.user.has_perm('user_profile.can_dance'):
#         return HttpResponse('Baba Karam!')
#     return HttpResponse('raghs harameh!')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        if email:
            password = request.POST.get('password', None)
            if password:
                user = authenticate(request, email=email, password=password)
                if user:
                    login(request, user)
                    return redirect("home")
                else:
                    return HttpResponse("user pass eshtebah")
        else:
            return HttpResponse("email ro bezar")


def user_view(request):
    return render(request, "user/user.html", {})


def signup(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        if email:
            password = request.POST.get('password', None)
            repeated_passweord = request.POST.get('repeat_password', None)
            if password:
                if password == repeated_passweord:
                    try:
                        User.objects.create_user(email=email, password=password, phone=phone)
                        messages.success(request, "Register Successfully!")
                        return redirect('user-view')
                    except IntegrityError as e:
                        # return render(request, "user/error.html", {"message": e})
                        messages.error(request, f"{e}")
                        return redirect('user-view')
                else:
                    return HttpResponse("pass va tekraresh equal nistan")


@method_decorator(csrf_exempt, name="dispatch")
class ProfileView(View):
    def get(self, request):
        profile_object = request.user.profile
        context = {
            'profile_object': profile_object,
        }
        return render(request, 'user/profile.html', context)

    def post(self, request):
        return HttpResponse("in post")


class ProfileEdit(TemplateView):
    template_name = 'user/profile_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_object'] = self.request.user
        return context