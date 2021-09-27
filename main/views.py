from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def handle_404(request, exception):
    return render(request, 'main/404.html')


def handle_429(request, exception):
    return render(request, 'main/429.html')


def handle_500(request):
    return render(request, 'main/500.html')
