def print_even(test_list):
    count = 0
    for i in test_list:
        if i % 2 == 0:
            yield i
            count += 1
    yield count


test_list = [1, 4, 5, 6, 7]

a = print_even(test_list)
print(next(a))
print(next(a))
print(next(a))
