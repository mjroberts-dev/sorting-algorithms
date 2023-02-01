import seed
import algorithms.bubble
import algorithms.selection

data = seed.generateRandomArray(15)

print(algorithms.bubble.sort(data))
print(algorithms.selection.sort(data))