from django.shortcuts import render

from django.views import View
from django.views.generic import ListView, DetailView

from .models import SiteModel, SiteDataModel


class SiteListView(ListView):
    model = SiteModel
    template_name = 'sites/sites.html'


class SiteDetailView(DetailView):
    model = SiteModel
    template_name = 'sites/site.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['data'] = SiteDataModel.objects.filter(site=context['object'])
        return context


class SiteSummarySumView(View):

    def get(self, request):
        context = {
            'summary': SiteDataModel.summary.get_sum()
        }
        return render(request, 'sites/summary-sum.html', context)


class SiteSummaryAverageView(View):

    def get(self, request):
        context = {
            'summary': SiteDataModel.summary.get_average()
        }
        return render(request, 'sites/summary-average.html', context)
