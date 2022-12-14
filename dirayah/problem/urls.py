from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # unique id for each problem
    path('<int:problem_id>', views.problem, name='problem'),
    path('compile', views.compile, name='compile'),
    path('comment/<int:problem_id>', views.comment, name='comment'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)