from django.http import HttpResponse

from pets_accounting.settings import API_KEY


def check_api_token(get_response):
    def middleware(request):
        print(request.path)
        if '/admin' in request.path:
            return get_response(request)
        token = request.headers.get('Authorization')
        if 'X-API-KEY' not in token:
            return HttpResponse(content='Invalid token header. No credentials provided', status=401)
        elif token != 'X-API-KEY ' + API_KEY:
            return HttpResponse(content='Invalid token header. Value is not correct', status=401)
        return get_response(request)
    return middleware
