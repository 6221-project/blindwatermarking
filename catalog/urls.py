from django.urls import path
from catalog import views
from django.conf.urls import url
from django.views.static import serve
import sys
sys.path.append('../')
from blindwatermarking import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_image/', views.upload_image),
    path('encode_image/', views.encode_image),
    path('decode_image/', views.decode_image),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]