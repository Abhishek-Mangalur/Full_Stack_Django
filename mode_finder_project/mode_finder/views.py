from django.shortcuts import render
from django.http import HttpResponse

def find_mode(request, num_list):
    # Split the input string into a list of numbers
    numbers = list(map(int, num_list.split(',')))

    # Calculate the mode (most frequent number)
    if not numbers:
        mode = None
    else:
        count_dict = {}
        for num in numbers:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        max_count = max(count_dict.values())
        mode = [num for num, count in count_dict.items() if count == max_count]

    return render(request, 'find_mode.html', {
        'num_list': num_list,
        'mode': mode,
    })
