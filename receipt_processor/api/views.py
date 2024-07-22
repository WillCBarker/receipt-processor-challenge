import json
import uuid
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .util import PointsCalculator


# temp storage
receipts = {}


@method_decorator(csrf_exempt, name="dispatch")
class ProcessReceiptView(View):
    def post(self, request, *args, **kwargs):
        receipt_data = json.loads(request.body)
        receipt_id = uuid.uuid4()
        points = PointsCalculator.calculate_points(receipt_data)
        receipts[str(receipt_id)] = points
        return JsonResponse({"id": str(receipt_id)})
    

class GetPointsView(View):
    def get(self, request, receipt_id, *args, **kwargs):
        points = receipts.get(str(receipt_id))
        if points is not None:
            return JsonResponse({"points": points})
        else:
            return JsonResponse({"error": "Receipt not found"}, status=404)