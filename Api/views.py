from django.http import JsonResponse
import json
from Products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def home(request, *args, **kwargs):
    # body = request.body
    # print(body)
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
    return Response(data)