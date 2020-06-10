def unique_loop(a):
    result = []
    for num in a:
        if num not in result:
            result.append(num)
    return result

def unique_set(a):
    return list(set(a))

print(unique_loop([1, 2, 2, 3, 3, 3]))
print(unique_set([1, 2, 2, 3, 3, 3]))
