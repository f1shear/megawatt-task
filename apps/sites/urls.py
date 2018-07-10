from django.urls import path
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from . import views


urlpatterns = [
    path('sites/', views.SiteListView.as_view(), name='site-list'),
    path('', RedirectView.as_view(url=reverse_lazy('site-list'))),
    path('sites/<int:pk>/', views.SiteDetailView.as_view(), name='site-detail'),
    path('summary/', views.SiteSummarySumView.as_view(), name='sites-summary-sum'),
    path('summary-average/', views.SiteSummaryAverageView.as_view(),
         name='sites-summary-average'),
]
