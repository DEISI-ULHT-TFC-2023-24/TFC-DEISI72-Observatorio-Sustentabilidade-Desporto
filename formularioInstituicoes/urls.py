"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('form', views.formulario_view),
    path('update_form/<tema_id>', views.update_form_view),
    path('submmit', views.respostas_view),
    path('dashboard_energia', views.dashboard_energia_view),
    path('dashboard_hidrica', views.dashboard_hidrica_view),
    path('signup', views.sign_up_view),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('instalacoes', views.instalacoes_view),
    path('editinstalacao', views.editinstalacao_view),
    path('deleteinstalacao', views.deleteinstalacao_view),
    path('password_reset', views.passwordreset_view),
    path('', views.instalacoes_view),
    path('post/', views.post_request_submmit),
    re_path(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

