from django.http import HttpResponse
from django.shortcuts import render # noqa

# Create your views here.


def home(request):
    raise ValueError()
    return HttpResponse('<html><body>Olá Django!!</body></html>', content_type='text/html')
