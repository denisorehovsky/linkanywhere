from rest_framework.routers import DefaultRouter

from linkanywhere.apps.users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)