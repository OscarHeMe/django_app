from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Product


def index(request):
    reponse = {
        'message': 'Product'
    }
    return JsonResponse(reponse)


def bulk_insert(request):
    try:
        products = request.POST['products']
        return JsonResponse(products, status=201)
    except Exception as e:
        error_msg = str(e)
        reponse = {
            'error': error_msg
        }
        return JsonResponse(reponse, status=400)


