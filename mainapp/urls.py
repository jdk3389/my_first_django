from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ShipList, ShipDetail

urlpatterns = [
    path('', ShipList.as_view()),
    path('<int:pk>/', ShipDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
