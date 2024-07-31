from django.shortcuts import render

def tables_of_squares(request, x, y):
    pairs = [(i, j, i**2, j**2) for i in range(1, x + 1) for j in range(1, y + 1)]
    return render(request, 'index.html', {'pairs': pairs})

