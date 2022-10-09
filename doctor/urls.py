from django.urls import path
from . import views

urlpatterns = [
    path('', views.doc_home, name="doc_name"),
]
