from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Jfile
from .forms import JfileForm

# Create your views here.
class JsonListView(ListView):
    model = Jfile
    template_name = 'jsonlist.html'

    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Jfile.objects.exclude(privacy='PRIVATE')
        return Jfile.objects.all()

class JsonFileUploadView(CreateView):
    model = Jfile
    form_class = JfileForm
    template_name = 'jfile_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        jfile = form.save(commit=False)
        if self.request.user.username:
            jfile.user = self.request.user.username
        else:
            jfile.user = 'anonymous'
        jfile.save()
        return super().form_valid(form)

