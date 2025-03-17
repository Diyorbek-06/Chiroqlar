from django.shortcuts import render
from django.views import View
from .models import Chiroq
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import ChiroqForm

# Create your views here.


def home_page(request):
    return render(request, 'home.html')


class ChiroqList(View):
    def get(self, request):
        t = request.GET.get('q')
        chiroqlar = Chiroq.objects.filter(brand__icontains=t) if t else Chiroq.objects.all()
        return render(request, 'chiroq_list.html', {'chiroqlar':chiroqlar})



class ChiroqDetail(DetailView):
    model = Chiroq
    template_name = 'chiroq_detail.html'
    context_object_name = 'chiroq'

class ChiroqDelete(DeleteView):
    model = Chiroq
    success_url = reverse_lazy('chiroq-list')
    template_name = 'chiroq_delete.html'
    context_object_name = 'chiroq'

class ChiroqCreate(CreateView):
    model = Chiroq
    form_class = ChiroqForm
    success_url = reverse_lazy('chiroq-list')
    template_name = 'chiroq_create.html'


class ChiroqUpdate(UpdateView):
    model = Chiroq
    template_name = 'chiroq_update.html'
    fields = ['brand', 'price', 'quantity', 'vatt_kuchi', 'color', 'image']

    def get_success_url(self):
        return reverse_lazy('chiroq-detail', kwargs={'pk': self.object.pk})

