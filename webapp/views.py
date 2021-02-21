from django.shortcuts import render


# Create your views here.
def game_view(request):
    if request.method == 'GET':
        return render(request, "guess_num_view.html")