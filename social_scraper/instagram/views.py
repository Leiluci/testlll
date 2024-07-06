from django.http import JsonResponse
from icecream import ic

def example_view(request):
    data = {'message': 'Hello, Instagram!'}
    ic(data)
    return JsonResponse(data)
