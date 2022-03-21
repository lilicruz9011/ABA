from django.urls import path

from ABA_App import views
from django.conf import settings
from django.conf.urls.static import static

from ABA_App.views import SignUpView, BienvenidaView,SignInView,SignOutView


urlpatterns = [
    path('home/', views.home, name="Home"),
    path('', BienvenidaView.as_view(), name='bienvenida'),
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('incia-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
] 

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
