from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from query.models import CadastrialQuery
import time
import random


@method_decorator(csrf_exempt, name='dispatch')
class QueryView(View):
    def post(self, request, *args, **kwargs):
        cadastrial_number = request.POST.get("cadastrial_number")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        # Создаём запись запроса
        cadastrial_query = CadastrialQuery.objects.create(
            cadastrial_number=cadastrial_number,
            latitude=latitude,
            longitude=longitude,
            result=None,
        )

        # Имитация запроса на внешний сервер
        time.sleep(random.randint(1, 60))
        result = random.choice([True, False])

        # Сохраняем результат
        cadastrial_query.result = result
        cadastrial_query.save()

        return JsonResponse(
            {
                "cadastrial_number": cadastrial_number,
                "result": result,
            }
        )


class ResultView(View):
    def get(self, request, *args, **kwargs):
        cadastrial_number = request.GET.get("cadastrial_number")

        try:
            cadastrial_query = CadastrialQuery.objects.get(
                cadastrial_number=cadastrial_number
            )
            result = cadastrial_query.result
            if result is None:
                return JsonResponse({"error": "Result is not available"}, status=404)
            return JsonResponse(
                {"cadastrial_number": cadastrial_number, "result": result}
            )
        except CadastrialQuery.DoesNotExist:
            return JsonResponse(
                {"error": "Query with this cadastrial number does not exist"},
                status=404,
            )


class PingView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"status": "ok"})


class HistoryView(View):
    def get(self, request, *args, **kwargs):
        cadastrial_number = request.GET.get("cadastrial_number")
        if cadastrial_number:
            queries = CadastrialQuery.objects.filter(
                cadastrial_number=cadastrial_number
            )
        else:
            queries = CadastrialQuery.objects.all()

        history = [
            {
                "cadastrial_number": q.cadastrial_number,
                "result": q.result,
                "timestamp": q.timestamp,
            }
            for q in queries
        ]
        return JsonResponse({"history": history})
