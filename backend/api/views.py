from django.http import JsonResponse

def get_response(request):
    data = {'message': 'Successful Reply from Backend!!!'}
    return JsonResponse(data)
