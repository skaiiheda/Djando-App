from random import random

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView
from django.utils.translation import gettext_lazy as _, ngettext
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from shopapp.models import Order
from .forms import ProfileForm
from .models import Profile
from shopapp.serializers import OrderSerializer


# class AboutMeView(TemplateView):
#     template_name = "myauth/about-me.html"


class HelloView(View):
    welcome_message = _("welcome hello word")

    def get(self, request: HttpRequest) -> HttpResponse:
        items_str = request.GET.get("items") or 0
        items = int(items_str)
        products_line = ngettext(
            "one product",
            "{count} products",
            items,
        )
        products_line = products_line.format(count=items)
        return HttpResponse(
            f"<h1>{self.welcome_message}</h1>"
            f"\n<h2>{products_line}</h2>"
        )


# class HelloView(View):
#     def get(self, request: HttpRequest) -> HttpResponse:
#         welcome_message = _("welcome hello word")
#         return HttpResponse(f"<h1>{welcome_message}</h1>")


def about_me(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('myauth:about-me')
        else:
            form = ProfileForm(instance=profile)
        return render(request, 'myauth/about-me.html', {'profile': profile, 'form': form})
    else: return render(request, 'myauth/about-me.html')


class UsersListView(ListView):
    template_name = "myauth/users-list.html"
    model = User
    context_object_name = "users"


class UserDetailsView(DetailView):
    template_name = "myauth/user-details.html"
    model = User
    context_object_name = "user"


class UserOrdersListView(ListView):
    template_name = "myauth/user_orders-list.html"
    model = Order
    context_object_name = "user_orders"

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        self.usr = user
        self.owner = user
        return super().get_queryset().filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.usr
        context['owner'] = self.owner
        return context


class OrdersDataExportView(View):
    def get(self, request: HttpResponse, *args, **kwargs) -> JsonResponse:
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        cache_key = f'orders_export|{user_id}'
        print(cache_key)
        orders_data = cache.get(cache_key)
        if orders_data is None:
            orders = Order.objects.filter(user=user).order_by('id')
            orders_serializer = OrderSerializer(orders, many=True)
            orders_data = orders_serializer.data
            cache.set(cache_key, orders_data, timeout=60*2)
        return JsonResponse(orders_data, safe=False)


def AvatarUpdateView(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user=user)
    if request.user.is_staff and request.user.profile == profile:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('myauth:user_details', pk=pk)
        else:
            form = ProfileForm(instance=profile)
        return render(request, 'myauth/avatar_update_form.html', {'user': user, 'profile': profile, 'form': form})
    else:
        return redirect('myauth:user_details', pk=pk)


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/')
        return render(request, 'myauth/login.html')
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin/')
    return render(request, 'myauth/login.html', {"error": "Invalid login credentials"})


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(reverse('myauth:login'))


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('myauth:login')


def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse('Cookie set')
    response.set_cookie('fizz', 'buzz', max_age=3600)
    return response


@cache_page(60 * 2)
def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get('fizz', 'default value')
    return HttpResponse(f'Cookie value: {value!r} + {random()}')


@permission_required("myauth.view_profile", raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session["foobar"] = "spameggs"
    return HttpResponse('Session set')


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get('foobar', 'default')
    return HttpResponse(f'Session value: {value!r}')


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({'foo': 'bar', 'spam': 'eggs'})
