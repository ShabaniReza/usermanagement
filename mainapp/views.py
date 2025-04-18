from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.pagination import PageNumberPagination
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
from .models import Profile
from .serializers import ProfileSerializer
from .permissions import IsOwnerOrReadOnly


# @method_decorator(cache_page(60 * 15))
class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    pagination_class = PageNumberPagination


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

