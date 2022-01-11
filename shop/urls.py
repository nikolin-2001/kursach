from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Note34', views.notepr, name='Notepr'),
    path('SB10', views.notesale10, name='Notesale10'),
    path('Accsesor', views.accsesor, name='Accsesor'),
    path('open/<int:product_id>/', views.open, name='open'),
    path('buy/<int:product_id>/', views.PurchaseCreate.as_view(), name='buy'),
    path('promocod', views.PromocodCreate.as_view(), name='promocod'),
]

if settings.DEBUG:
    assert isinstance(settings.STATIC_ROOT, object)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
