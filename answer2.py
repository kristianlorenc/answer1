import random

def get_random(number=3):
    if not isinstance(number, int) or number < 1 or number > 100:
        raise Exception("Invalid Data!")

    result = []
    while len(result) < number:
        rand_num = random.randint(1, 100)
        if rand_num not in result:
            result.append(rand_num)

    return sorted(result)

# Example usage
print(get_random(5))  # Expected output (example): [2, 33, 46, 81, 100]
print(get_random())   # Expected output (example): [58, 66, 99]

