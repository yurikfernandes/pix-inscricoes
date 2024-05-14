from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from inscricoes import settings

from pagamentos import views

router = routers.DefaultRouter()
router.register(r'pagamentos', views.PagamentoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)