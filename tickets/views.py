import random
from django.shortcuts import render
import numpy as np
from tabulate import tabulate
# Create your views here.
def home(request):
    return render(request, 'tickets/home.html')
def ticket(request):
    ticket_array = np.zeros((3, 9), dtype=int)
    #print(ticket_array)
    total_numbers = [num for num in range(1, 90)]
    total_indices = [(i, j) for i in range(3) for j in range(9)]
    #print(total_indices)

    random_indices = []
    firstRow = random.sample(total_indices[:9], 5)
    secondRow = random.sample(total_indices[9:18], 5)
    thirdRow = random.sample(total_indices[-9:], 5)

    for index in firstRow:
        random_indices.append(index)

    for index in secondRow:
        random_indices.append(index)

    for index in thirdRow:
        random_indices.append(index)

    #print(random_indices)

    for num in random_indices:
        if num[1] == 0:
            number = random.choice(total_numbers[:10])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 1:
            number = random.choice(total_numbers[10:20])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 2:
            number = random.choice(total_numbers[20:30])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 3:
            number = random.choice(total_numbers[30:40])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 4:
            number = random.choice(total_numbers[40:50])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 5:
            number = random.choice(total_numbers[60:70])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 6:
            number = random.choice(total_numbers[70:80])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 7:
            number = random.choice(total_numbers[80:89])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0
        elif num[1] == 8:
            number = random.choice(total_numbers[20:30])
            ticket_array[num] = number
            total_numbers[total_numbers.index(number)] = 0

    for col in range(9):
        # if all the rows are filled with random number
        if(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
            for row in range(2):
                if ticket_array[row][col] > ticket_array[row+1][col]:
                    temp = ticket_array[row][col]
                    ticket_array[row][col] = ticket_array[row+1][col]
                    ticket_array[row+1][col] = temp

        # if 1st and 2nd row are filled by random number
        elif(ticket_array[0][col] != 0 and ticket_array[1][col] != 0 and ticket_array[2][col] == 0):
            if ticket_array[0][col] > ticket_array[1][col]:
                temp = ticket_array[0][col]
                ticket_array[0][col] = ticket_array[1][col]
                ticket_array[1][col] = temp

        # if 1st and 3rd row are filled by random number
        elif(ticket_array[0][col] != 0 and ticket_array[2][col] != 0 and ticket_array[1][col] == 0):
            if ticket_array[0][col] > ticket_array[2][col]:
                temp = ticket_array[0][col]
                ticket_array[0][col] = ticket_array[2][col]
                ticket_array[2][col] = temp

        # if 2nd and 3rd rows are filled with random numbers
        elif(ticket_array[0][col] == 0 and ticket_array[1][col] != 0 and ticket_array[2][col] != 0):
            if ticket_array[1][col] > ticket_array[2][col]:
                temp = ticket_array[1][col]
                ticket_array[1][col] = ticket_array[2][col]
                ticket_array[2][col] = temp


    print(tabulate(ticket_array, tablefmt="fancy_grid", numalign="center"))
    context = {
        'ticket_array' : ticket_array,
        'total_indices' : total_indices,
        'rowrange' : [0,1,2],
        'columnrange' : [0,1,2,3,4,5,6,7,8]
    }
    return render(request, 'tickets/ticket.html', context)