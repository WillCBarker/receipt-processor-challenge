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
    """
        POST /receipts/process
        Processes a JSON receipt and returns an ID.
        
        Payload: JSON receipt (See example file in original challenge repo)
        Response: {"id": "receipt_id"}
        
        Example Response:
        {
            "id": "7fb1377b-b223-49d9-a31a-5a02701dd310"
        }
    """
    def post(self, request, *args, **kwargs):
        receipt_data = json.loads(request.body)
        receipt_id = uuid.uuid4()
        points = PointsCalculator.calculate_points(receipt_data)
        receipts[str(receipt_id)] = points
        return JsonResponse({"id": str(receipt_id)})


@method_decorator(csrf_exempt, name='dispatch')
class GetPointsView(View):
    """
        GET /receipts/{id}/points
        Returns the points for a receipt ID.
        
        Response: {"points": number_of_points}
        Error: {"error": "Receipt not found"}
        
        Example Response:
        {
            "points": 32
        }
    """
    def get(self, request, receipt_id, *args, **kwargs):
        points = receipts.get(str(receipt_id))
        if points is not None:
            return JsonResponse({"points": points})
        else:
            return JsonResponse({"error": "Receipt not found"}, status=404)