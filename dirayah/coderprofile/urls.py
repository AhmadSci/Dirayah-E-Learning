from django.urls import path
from coderprofile import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('<str:username>',views.user_profile, name='user_profile'),
    path('',views.my_profile, name='my_profile'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)