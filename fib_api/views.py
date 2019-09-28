from django.shortcuts import render
import time
from fib_api.models import Fibinocci

def fibinocci_series(num):
    if num < 2:
        return 1
    else:
        num_seq_1 = 1
        num_seq_2 = 1
        for i in range(2, num):
            temp = num_seq_1 + num_seq_2
            num_seq_1 = num_seq_2
            num_seq_2 = temp
        return num_seq_2


def fib_number(request):
    start_time = time.time()
    num = 0
    result = 0
    time_taken = 0
    get_num = request.GET.get('number')

    if get_num:
        num = int(get_num)
        validate = Fibinocci.objects.filter(element=num)
        if validate:
            obj = Fibinocci.objects.get(element=get_num)
            result = obj.value
            end_time = time.time() - start_time
            time_taken = str(end_time)[0:7]
        else:
            num = int(get_num)
            result = fibinocci_series(num)
            obj = Fibinocci.objects.create(element=num,value=result)
            obj.save()
            end_time = time.time() - start_time
            time_taken = str(end_time)[0:7]

    return render(
        request,
        'index.html',
        {
            'number': num,
            'result': result,
            'time_taken': time_taken
        }
    )
