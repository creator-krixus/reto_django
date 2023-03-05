from django.urls import path
from .views import VulnerabilityView

urlpatterns = [
    path('vulnerability/', VulnerabilityView.as_view(), name='vulnerability_list'),
    path('vulnerability/<int:id>', VulnerabilityView.as_view(),
         name='vulnerability_process')
]
