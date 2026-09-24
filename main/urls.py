from config import settings
from .views import *
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('phase1/', phase1, name='phase1'),
    path('phase2/', phase2, name='phase2'),
    path('phase3/', phase3, name='phase3'),
    path('phase4/', phase4, name='phase4'),
    path('phase5/', phase5, name='phase5'),
    path('phase6/', phase6, name='phase6'),

    path('info/', info, name='info'),

    path('movie/', movie, name='movie'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)