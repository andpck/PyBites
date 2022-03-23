def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    list_positives = [i for i in numbers if ((i > 0) & ((i % 2) == 0))]
    return list_positives
