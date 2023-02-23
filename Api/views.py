from django.http import JsonResponse

# Create your views here.


def home(request, *args, **kwargs):
    return JsonResponse({"message": "Hi there, Django rest API"})