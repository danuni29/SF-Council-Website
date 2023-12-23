from django.shortcuts import render

# Create your views here.


def sfarm_overflow(request):
    return render(
        request,
        'sfarm_overflow/sfarm_overflow_main.html',
    )