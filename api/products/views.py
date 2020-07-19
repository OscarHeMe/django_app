import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Product


def index(request):
    reponse = {
        'message': 'Product'
    }
    return JsonResponse(reponse)


def bulk_insert(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            products = body['products']
            return JsonResponse(body, status=200)
        except Exception as e:
            error_msg = str(e)
            reponse = {
                'error': error_msg
            }
            return JsonResponse(reponse, status=400)
    else:
        reponse = {
            'error': 'method not allowed'
        }
        return JsonResponse(reponse, status=400)
