from django.shortcuts import render
import string

def analyze_text(request, input_text):
    vowels = 'aeiou'
    input_text_lower = input_text.lower()
    vowels_list = [char for char in input_text_lower if char in vowels]
    consonants_list = [char for char in input_text_lower if char.isalpha() and char not in vowels]

    vowels_count = len(vowels_list)
    consonants_count = len(consonants_list)

    return render(request, 'index.html', {
        'input_text': input_text,
        'vowels_count': vowels_count,
        'consonants_count': consonants_count,
        'vowels_list': vowels_list,
        'consonants_list': consonants_list,
    })
