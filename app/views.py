from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import *
from .forms import *
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .filters import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from datetime import datetime
from django.db import transaction
from django.contrib.messages import constants
from django.contrib.messages.storage import default_storage

@login_required
def home(request):
    context = { 
    'time':datetime.now()
    }
    return render(request, 'app/home.html', context )
    
class SecretPage(TemplateView):
    template_name = 'app/home.html'


class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'app/user_detail.html'

class OsatiCreate(LoginRequiredMixin, CreateView):
    model = OdradjeniSati
    form_class = OSatiForm
    def form_valid(self, form):
        form.instance.korisnik = self.kwargs.get('pk')
        form.instance.korisnik = self.request.user
        print(form.cleaned_data)
        return super(OsatiCreate, self).form_valid(form)

    def get_success_url(self):
        return '/osati'

class OSatiUpdate(LoginRequiredMixin, UpdateView):
    if (datetime.now()):
        model = OdradjeniSati
        form_class = OSatiForm1

class PregledOSati(LoginRequiredMixin, ListView):
    model = OdradjeniSati
    template_name ='app/mojiosati.html'
    paginate_by = 10
    
    def get_queryset(self):
        return OdradjeniSati.objects.filter(korisnik=self.request.user).order_by('datum')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['filter'] = SFilter(self.request.GET, queryset= self.get_queryset())
        return context

class KrajVremena(LoginRequiredMixin, ListView):
    model = OdradjeniSati
    template_name ='app/mojiosati1.html'
    paginate_by = 10
    
    def get_queryset(self):
        return OdradjeniSati.objects.filter(korisnik=self.request.user, datum=datetime.now().date()).order_by('datum')

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/registered')
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {"form":form})

class ListaZCreate(LoginRequiredMixin,CreateView):
   model = ListaZadataka
   form_class = ZadaciForm

   def form_valid(self, form):
        form.instance.korisnik = self.kwargs.get('pk')
        form.instance.korisnik = self.request.user
        print(form.cleaned_data)
        return super(ListaZCreate, self).form_valid(form)

   def get_success_url(self):
    return '/zadaci'

class PregledZ(LoginRequiredMixin, ListView):
    model = ListaZadataka
    template_name ='app/mojizadaci.html'

    def get_queryset(self):
        return ListaZadataka.objects.filter(korisnik=self.request.user, status = 'u').order_by('naziv')

class PregledZR(LoginRequiredMixin, ListView):
    model = ListaZadataka
    template_name ='app/mojizadacir.html'

    def get_queryset(self):
        return ListaZadataka.objects.filter(korisnik=self.request.user, status = 'r').order_by('naziv')

class ZadaciUpdate(LoginRequiredMixin, UpdateView):
   model = ListaZadataka
   form_class = ZadaciForm

   def get_success_url(self):
    return '/zadaci'

class ZDetail(LoginRequiredMixin,DetailView):
    model = ListaZadataka
    template_name ='app/zadaci_detail.html'

class ZadatakDelete(LoginRequiredMixin, DeleteView):
    model = ListaZadataka
    success_url = reverse_lazy('zadaci-pregled')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'app/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
