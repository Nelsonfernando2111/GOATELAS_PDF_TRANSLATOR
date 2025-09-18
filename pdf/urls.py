from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_pdf_ajax/', views.upload_pdf_ajax, name='upload_pdf_ajax'),
    path('progresso_pdf/<str:filename>/', views.progresso_pdf, name='progresso_pdf'),
    path('download_pdf/<str:filename>/', views.download_pdf, name='download_pdf'),
    

    path("termos/", views.termos, name="termos"),
    path('privacidade/', views.privacidade, name='privacidade'), 

]
