from django.http import HttpResponse


def home(request):
    return HttpResponse("Головна сторінка сайту 'Світ книг)'!!!'")