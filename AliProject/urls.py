"""AliProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
from django.urls import re_path as url
from Alisystem.views import *
from django.contrib.auth.views import LoginView, LogoutView
from Alisystem.forms import BootstrapAuthenticationForm, RegistrarPagamentosForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # Telas básicas
    path('', home, name='home'),
    #path(r'^contact$', contact, name='contact'),
    # path(r'^about', about, name='about'),

   # Login e logout
    url(r'^login/$', LoginView.as_view(template_name='app/login.html'), name='login'),
    url(r'^logout$', LogoutView.as_view(next_page='/'), name='logout'),

   # MÓDULO INSERIR ATENDIMENTOS
    url(r'^inserir_atendimentos/$', AtendimentosProcedimentos_aplicadoCreate.as_view(), name='inserir_atendimentos'),

   # MÓDULO PAGAMENTOS
	url(r'^pagamentos/$', mostra_pagamentos, name="pagamentos"),
    url(r'^pagamentos/data_repasse/$', atribui_data_repasse),
	url(r'^pagamentos/data_repasse/confirma/$', confirma_data_repasse),
    url(r'^pagamentos/data_repasse/confirma/atualiza$', atualiza_valores),
    url(r'^registrar_pagamentos/$', registrar_pagamentos, name="registrar_pagamentos"),
    url(r'^registrar_pagamentos/apresenta$', registrar_pagamentos, name="registrar_pagamentos"),
    url(r'^contact/thanks$', contact_thanks),
    
    # MÓDULO PAINÉIS
    url(r'^dentistas/$', DentistaList.as_view(), name='dentistas'),
    url(r'^atendimentos/dentista/([\w-]+)/$', AtendimentoDentistaList.as_view()),
    url(r'^atendimentos/$', AtendimentoList.as_view(), name='atendimentos'),
    url(r'^atendimentos/(?P<pk>[0-9]+)/$', ProcedimentoAtendimentoList.as_view(), name = 'atendimento_list'),
    url(r'^atendimentos/dentista/([\w-]+)/(?P<pk>[0-9]+)/$', ProcedimentoAtendimentoList.as_view()),
    url(r'^procedimentos/dentista/([\w-]+)/$', Procedimentos_aplicadoDentistaDataList.as_view()),
    url(r'^procedimentos/dentista/([\w-]+)/glosado/$', AtendimentoDentistaGlosadoList.as_view()),

]
