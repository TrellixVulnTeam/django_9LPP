from . import views
from django.conf import settings
from django.urls import path
from django.conf.urls import include, url, static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('summernote/', include('django_summernote.urls')),
    
]

