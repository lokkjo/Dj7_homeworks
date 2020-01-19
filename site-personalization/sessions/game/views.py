from django.shortcuts import render


def show_home(request):
    visits = request.session.get('players', 0)
    # if
    context = {}
    return render(
        request,
        'home.html',
        context
    )
