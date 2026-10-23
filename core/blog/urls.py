from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    #path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    #path('go-to-editvideo/<int:pk>/', views.RedirectToedit.as_view(), name='redirect-to-editvideo'),
    path('post/',views.PostlistView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),

]