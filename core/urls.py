from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include

from core.config.schemas import swagger_drf_yasg_urlpatterns


# Base Api url
base_url = "api/v1/"


_api_v1_url = lambda url: base_url + _(url)

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path(_api_v1_url('agent/'), include("apps.agent.urls", namespace="agent")),
    path(_api_v1_url('calculator/'), include("apps.calculator.urls", namespace="calculator")),
    path(_api_v1_url('cisco/'), include("apps.cisco.urls", namespace="cisco")),
    path(_api_v1_url('kpi/'), include("apps.kpi.urls", namespace="kpi")),
    path(_api_v1_url('playmobile/'), include("apps.playmobile.urls", namespace="playmobile")),
    path(_api_v1_url('processing/'), include("apps.processing.urls", namespace="processing")),
    path(_api_v1_url('shared/'), include("apps.shared.urls", namespace="shared")),
    path(_api_v1_url('shina/'), include("apps.shina.urls", namespace="shina")),
    path(_api_v1_url('telemarketing/'), include("apps.telemarketing.urls", namespace="telemarketing")),
)

urlpatterns += swagger_drf_yasg_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

