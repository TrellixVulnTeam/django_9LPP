from . import views
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
]