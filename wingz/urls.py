from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.rides.views import RideViewSet, RideEventViewSet
from apps.users.views import UserViewSet

router = SimpleRouter()
router.register(r'api/rides', RideViewSet)
router.register(r'api/events', RideEventViewSet)
router.register(r'api/users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
