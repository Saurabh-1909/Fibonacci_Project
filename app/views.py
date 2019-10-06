from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from app.models import FibonacciTest
from django.views import View
import time


def fibonacci(numeric):
    if numeric < 2:
        return 1

    else:
        numeric_1 = 1
        numeric_2 = 1

        for numeric in range(2, numeric):
            value = numeric_1 + numeric_2
            numeric_1 = numeric_2
            numeric_2 = value

        return numeric_2


class FibonacciAPIView(View):

    def get(self, request):

        number = request.GET.get('value')

        if number is None:
            return render(request, 'index.html')

        else:
            start_time = time.clock()
            time_taken =time.clock() - start_time
            numeric = int(number)
            output = fibonacci(numeric)


            fibonacci_qs = FibonacciTest.objects.create(
                numeric=numeric,
                output=output,
                time_taken=time_taken
            )
            fibonacci_qs.save()

            data = {
                'numeric': numeric,
                'output': output,
                'time_taken': time_taken
            }

            return render(request, 'index.html', data)



