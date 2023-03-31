from django.urls import path
from .views import get_wfs_data
from django.views.generic import TemplateView

urlpatterns = [
    path('wfs-data/', get_wfs_data, name='wfs_data'),
    path('leaflet/', TemplateView.as_view(template_name='leaflet.html')),
]



