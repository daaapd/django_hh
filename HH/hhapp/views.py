import os

from django.shortcuts import render

from .forms import ReqForm
from django.urls import reverse_lazy,reverse
from .models import Vacancy, Word, Wordskill,Area
from hhapp.management.commands.full_db import Command
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.views.generic.base import ContextMixin

def start(request):
    return render(request, 'hhapp/index.html')


def form(request):
    form1 = ReqForm
    return render(request, 'hhapp/form.html', context={'form': form1})


def result(request):
    if request.method == 'POST':
        form = ReqForm(request.POST)
        if form.is_valid():
            vac = form.cleaned_data['vacancy']
            where = form.cleaned_data['where']
            pages = form.cleaned_data['pages']
            print(vac, where, pages, sep='\n')
            com = Command(vac, pages, where)
            com.handle()
            v = Word.objects.get(word=vac)
            s = Wordskill.objects.filter(id_word_id=v.id).all()
            vac = Vacancy.objects.filter(word_id=v).all()
            print(vac, v, s, sep='\n')
            return render(request, 'hhapp/about.html', context={'vac': vac, 'word': v, 'skills': s})
        else:
            form1 = ReqForm
            return render(request, 'hhapp/form.html', context={'form': form1})

class AreaList(ListView):
    model = Area
    template_name = 'happ/area_list.html'

    def get_queryset(self):
        return Area.object.order_by('name').all()

class AreaDetail(DetailView):
    model = Area
    template_name = 'happ/area_detail.html'

class AreaPostMixin(ContextMixin):
    def prerare_area(self,url,areas):
        for item in areas:
            if item['areas'] is None:
                url[item['name']]=item['id']
                self.prerare_area(url,item['areas'])
            else:
                url[item['name']] = item['id']
    def parse (self,area):
        r = {'url':'https://api.superjob.ru/2.0/vacancies/',
             'param': {'town':area,
                       'period':1}
             'header':{'X-Api-App-Id': os.getenv('key_super')
                       'Autirization':'Bearer r.000000010000001.example.access_token',
                       'Content-Type':'application/x-www-form-urlencoded'}
             }
        self.hh,self.zarpl = dict(),dict()
        for url, d in (('https://api.hh.ru/areas',self.hh),('https://api.zarplate.ru',self.zarpl)):
            res = self.get(url).json()
            self.prerare_area(d,res)
        res = self.get(r['url'],headers = r['header'],param = ['param']).json()
        return {'name' : area, 'ind_hh':self.hh.get('area',0),'ind_zarp':self.zarpl.get('area',0),
                'ind_zarp': self.zarpl.get('area',0),
                'ind_super': res['objects'][0]['town']['id'] if res['objects']else 0}
    def post(self,request,*args,**kwargs):
        text = request.POST['name']
        new_index = self.parse(text)
        Area.objects.create(**new_index)
        return super().post(request,*args,**kwargs)

class AreaList(DetailView):
    model = Area
    template_name = 'happ/area_detail.html'

class AreaCreate(CreateView):
    model = Area
    template_name = 'happ/area_create.html'
    success_url = reverse_lazy('hh:area_list')

class AreaUpdateView(UpdateView):
    model = Area
    template_name = 'happ/area_create.html'
    success_url = reverse_lazy('hh:area_list')

class AreaDeleteView(UpdateView):
    model = Area
    template_name = 'happ/area_delete_confirm.html'
    success_url = reverse_lazy('hhapp:area_list')

