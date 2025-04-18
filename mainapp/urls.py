from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)


urlpatterns = router.urls