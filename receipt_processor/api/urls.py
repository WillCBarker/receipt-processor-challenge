from django.urls import path
from .views import ProcessReceiptView, GetPointsView


urlpatterns = [
    path("receipts/process", ProcessReceiptView.as_view(), name="process_receipt"),
    path("receipts/<uuid:receipt_id>/points", GetPointsView.as_view(), name="get_points"),
]