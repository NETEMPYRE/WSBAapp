from django.urls import path
from .views import RequestView

urlpatterns = [
    path('withdrawl/', RequestView.as_view(), name='RequestView'),
]