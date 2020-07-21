import json

from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from .models import Product


def index(request):
    if request.method == 'GET':
        products = Product.objects.all().values()
        serialized_prods = list(products)
        response = {
            'products': serialized_prods
        }
        return JsonResponse(response, status=200)
    else:
        response = {
            'error': 'method not allowed'
        }
        return JsonResponse(response, status=400)


def bulk_insert(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            products = body['products']
            bulk_insert_response = Product.bulk_insert(products)
            if bulk_insert_response[0]:
                response = {
                    'status': 'OK'
                }
                return JsonResponse(response, status=200)
            else:
                response = {
                    'status': 'ERROR',
                    'products_report': bulk_insert_response[1],
                        # {
                        #     “product_id”: string,
                        #     “errors”: [string] <- Un array de strings con las validaciones que no paso.
                        # }
                    'number_of_products_unable_to_parse': len(bulk_insert_response[1])
                }
                return JsonResponse(response, status=422)
        except Exception as e:
            error_msg = str(e)
            response = {
                'error': error_msg
            }
            return JsonResponse(response, status=400)
    else:
        response = {
            'error': 'method not allowed'
        }
        return JsonResponse(response, status=400)
