from django.shortcuts import render
from django.views.generic import ListView

from centers.models import CentersModel

# Create your views here.
class CentersListView(ListView):
    model = CentersModel
    template_name = 'centers/centers.html'
    context_object_name = 'centers'
    paginate_by = 10
    queryset = CentersModel.objects.all()