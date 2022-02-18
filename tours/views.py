from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure: str):
    return render(request, 'tours/departure.html')


def tour_view(request, id: int):
    return render(request, 'tours/tour.html')
