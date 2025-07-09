from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cambio_facil import views

router = routers.DefaultRouter()
router.register('Pessoa', views.PessoaViewSet )
router.register('Cotacao', views.CotacaoViewSet )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),

]