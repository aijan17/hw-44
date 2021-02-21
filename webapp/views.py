from random import random

from django.shortcuts import render


# Create your views here.
def game_view(request):
    if request.method == 'GET':
        return render(request, "guess_num_view.html")
    if request.method == 'POST':
        secret_numbs = random.sample(range(10), 4)
        numbers = list(map(int, request.POST['numbers'][0].split(' ')))
        result = ''
        if len(numbers) > 4 or len(numbers) < 4:
            return '`error: there must be exactly 4 numbers`'

        elif numbers == " ":
            return ""

        elif numbers == secret_numbs:
            return "You got it right "
        for number in numbers:
            if number < 1 or number > 10:
                result = "`number cant be less 1 and more 10`"

        for i in range(len(numbers)):
            if numbers[i] in numbers[i+1:]:
                result = '`error`'

        else:
            bulls = 0
            cows = 0

            if numbers[0] == secret_numbs[0]:
                bulls += 1
            if numbers[1] == secret_numbs[1]:
                bulls += 1
            if numbers[2] == secret_numbs[2]:
                bulls += 1
            if numbers[3] == secret_numbs[3]:
                bulls += 1

            for i in numbers:
                if i == secret_numbs[0]:
                    cows += 1
                if i == secret_numbs[1]:
                    cows += 1
                if i == secret_numbs[2]:
                    cows += 1
                if i == secret_numbs[3]:
                    cows += 1

            result = f"You got  bulls: {bulls} and cows: {cows} "
