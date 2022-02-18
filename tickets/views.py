import random
from django.shortcuts import render
import numpy as np
# Create your views here.
def home(request):
    ticket_array = np.zeros((3, 9), dtype=int)
    #print(ticket_array)

    total_indices = [(i, j) for i in range(3) for j in range(9)]
    #print(total_indices)

    random_indices = []
    firstRow = random.sample(total_indices[:9], 5)
    secondRow = random.sample(total_indices[:9], 5)
    thirdRow = random.sample(total_indices[:9], 5)

    for index in firstRow:
        random_indices.append(index)

    for index in secondRow:
        random_indices.append(index)

    for index in thirdRow:
        random_indices.append(index)

    #print(random_indices)
    context = {
        'ticket_array' : ticket_array,
        'total_indices' : total_indices
    }
    return render(request, 'tickets/home.html', context)