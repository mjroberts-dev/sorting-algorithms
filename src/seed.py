import random

def generateRandomArray(length : int = 10):
    output = [0] * length
    for index, element in enumerate(output):
        output[index] = random.randrange(0, 100)
    return output