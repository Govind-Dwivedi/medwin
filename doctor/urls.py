from django.urls import path
from . import views

urlpatterns = [
    path('', views.doc_home, name="doc_home"),
    path('appointments/', views.appointHistory, name="appointHistory_doc"),
    path('add-comment/<int:id>', views.doc_comment, name="doc_comment")
]
