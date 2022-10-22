from django.urls import path

from deal.views import DealClientView, DealClientChangeView

urlpatterns = [
    path('api/v1/fetch/', DealClientView.as_view()),

    path('api/v1/<unique>/fetch/', DealClientChangeView.as_view())

]
