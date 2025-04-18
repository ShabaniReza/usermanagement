from django.urls import path
from search.views import SearchUsers

urlpatterns = [
    path("user/<str:query>/", SearchUsers.as_view()),
]