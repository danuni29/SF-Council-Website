from django.shortcuts import render

# Create your views here.


def operate(request):
    return render(
        request,
        'organizations/operate.html',
    )


def collabo(request):
    return render(
        request,
        'organizations/collabo.html',
    )


def intro_col(request):
    return render(
        request,
        'organizations/intro_col.html',
    )


def call(request):
    return render(
        request,
        'organizations/call.html',
    )


def sns(request):
     return render(
        request,
        'organizations/sns.html',
    )


def intro_sns(request):
    return render(
        request,
        'organizations/intro_sns.html',
    )


def report_sns(request):
    return render(
        request,
        'organizations/report_sns.html',
    )


def welfare(request):
    return render(
        request,
        'organizations/welfare.html',
    )


def intro_wel(request):
    return render(
        request,
        'organizations/intro_wel.html',
    )


def manage(request):
    return render(
        request,
        'organizations/manage.html',
    )




