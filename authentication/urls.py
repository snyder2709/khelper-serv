from django.urls import path
from .views import RegistrationAPIView

urlpatterns = [
    path('reg', RegistrationAPIView.as_view()),
]