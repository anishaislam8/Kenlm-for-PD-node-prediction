import heapq
import math

def insert_heap(heap, list_of_tokens_with_their_probability, max_heap_size):
    
    for token, probability in list_of_tokens_with_their_probability:
        score = math.log(probability) # using regular probability instead of negative probability
        found = False
        for item in heap:
            if item[1] == token:
                found = True
                if item[0] < score: # found the same item, but the current score is larger
                    heap.remove(item) # remove the current item
                    heapq.heappush(heap, (score, token)) # update with the larger new score
                break
        if found:
            heapq.heapify(heap)
        else:
            if len(heap) < max_heap_size:
                heapq.heappush(heap, (score, token))
            else:
                if score > heap[0][0]: # if current score is larger than the smallest score in the heap, insert the bigger score element
                    heapq.heappop(heap)
                    heapq.heappush(heap, (score, token))
    
    heapq.heapify(heap)
    # print("Min or max")
    # for i in range(len(heap)):
    #     print(heap[i][0], heap[i][1])

    heap.sort(key=lambda x: x[0], reverse=True)
    return heap


max_heap_size = 10

# Test cases

# Test case 1
heap = []
print("Test case 1 with more than max_heap_size elements")
list_of_tokens_with_their_probability = [
    ("sel" , 0.59585905),
    ("bng" , 0.5354099),
    ("msg" , 0.45632756),
    ("comport" , 0.37669763),
    ("change" , 0.65968746),
    ("floatatom" , 0.58062696),
    ("*~" , 0.6664535),
    ("dac~" , 0.833791),
    ("*" , 0.6053265),
    ("osc~" , 0.5178137),
    ("list_prepend", 0.71278006),
    ("list_trim" , 0.3476132),
    ("tabread", 0.57799923)
]

correct_heap = [(math.log(0.833791), 'dac~'), (math.log(0.71278006), 'list_prepend'), (math.log(0.6664535), '*~'), (math.log(0.65968746), 'change'), (math.log(0.6053265), '*'), (math.log(0.59585905), 'sel'), (math.log(0.58062696), 'floatatom'), (math.log(0.57799923), 'tabread'), (math.log(0.5354099), 'bng'), (math.log(0.5178137), 'osc~')]
returned_heap = insert_heap(heap, list_of_tokens_with_their_probability, max_heap_size)
for i in range(len(correct_heap)):
    assert (correct_heap[i][0] == returned_heap[i][0] and correct_heap[i][1] == returned_heap[i][1])
print("Passed test case 1\n")


# Test case 2
print("Test case 2 with more than max_heap_size elements and repeated tokens with different probabilities")
list_of_tokens_with_their_probability = [
    ("sel" , 0.59585905),
    ("bng" , 0.5354099),
    ("msg" , 0.45632756),
    ("comport" , 0.37669763),
    ("change" , 0.65968746),
    ("floatatom" , 0.58062696),
    ("*~" , 0.6664535),
    ("dac~" , 0.833791),
    ("*" , 0.6053265),
    ("osc~" , 0.5178137),
    ("list_prepend", 0.71278006),
    ("list_trim" , 0.3476132),
    ("tabread", 0.57799923),
    ("msg" , 0.56799923)
]

heap = []
correct_heap = [(math.log(0.833791), 'dac~'), (math.log(0.71278006), 'list_prepend'), (math.log(0.6664535), '*~'), (math.log(0.65968746), 'change'), (math.log(0.6053265), '*'), (math.log(0.59585905), 'sel'), (math.log(0.58062696), 'floatatom'), (math.log(0.57799923), 'tabread'), (math.log(0.56799923), 'msg'), (math.log(0.5354099), 'bng')]
returned_heap = insert_heap(heap, list_of_tokens_with_their_probability, max_heap_size)
for i in range(len(correct_heap)):
    assert (correct_heap[i][0] == returned_heap[i][0] and correct_heap[i][1] == returned_heap[i][1])
print("Passed test case 2\n")


# Test case 3

print("Test case 3 with fewer than max_heap_size elements")
list_of_tokens_with_their_probability = [
    ("sel" , 0.59585905),
    ("bng" , 0.5354099),
    ("msg" , 0.45632756),
    ("comport" , 0.37669763),
    ("change" , 0.65968746)
]

heap = []
correct_heap = [(math.log(0.65968746), 'change'), (math.log(0.59585905), 'sel'), (math.log(0.5354099), 'bng'), (math.log(0.45632756), 'msg'), (math.log(0.37669763), 'comport')]
returned_heap = insert_heap(heap, list_of_tokens_with_their_probability, max_heap_size)
for i in range(len(correct_heap)):
    assert (correct_heap[i][0] == returned_heap[i][0] and correct_heap[i][1] == returned_heap[i][1])
print("Passed test case 3\n")


# Test case 4

print("Test case 4 with fewer than max_heap_size elements and repeated tokens with different probabilities")
list_of_tokens_with_their_probability = [
    ("sel" , 0.59585905),
    ("bng" , 0.5354099),
    ("msg" , 0.45632756),
    ("comport" , 0.37669763),
    ("change" , 0.65968746),
    ("msg" , 0.56799923)
]

heap = []
correct_heap = [(math.log(0.65968746), 'change'), (math.log(0.59585905), 'sel'), (math.log(0.56799923), 'msg'), (math.log(0.5354099), 'bng'), (math.log(0.37669763), 'comport')]
returned_heap = insert_heap(heap, list_of_tokens_with_their_probability, max_heap_size)
for i in range(len(correct_heap)):
    assert (correct_heap[i][0] == returned_heap[i][0] and correct_heap[i][1] == returned_heap[i][1])
print("Passed test case 4\n")

# Test case 5

print("Test case 5 with max_heap_size elements")
list_of_tokens_with_their_probability = [
    ("sel" , 0.59585905),
    ("bng" , 0.5354099),
    ("msg" , 0.45632756),
    ("comport" , 0.37669763),
    ("change" , 0.65968746),
    ("floatatom" , 0.58062696),
    ("*~" , 0.6664535),
    ("dac~" , 0.833791),
    ("*" , 0.6053265),
    ("osc~" , 0.5178137)
]

heap = []
correct_heap = [(math.log(0.833791), 'dac~'), (math.log(0.6664535), '*~'), (math.log(0.65968746), 'change'), (math.log(0.6053265), '*'), (math.log(0.59585905), 'sel'), (math.log(0.58062696), 'floatatom'), (math.log(0.5354099), 'bng'), (math.log(0.5178137), 'osc~'), (math.log(0.45632756), 'msg'), (math.log(0.37669763), 'comport')]
returned_heap = insert_heap(heap, list_of_tokens_with_their_probability, max_heap_size)
for i in range(len(correct_heap)):
    assert (correct_heap[i][0] == returned_heap[i][0] and correct_heap[i][1] == returned_heap[i][1])
print("Passed test case 5\n")


# Test case 6

print("Test case 6 with more than max_heap_size elements and same probabilities")
list_of_tokens_with_their_probability = [
    ("sel" , 0.59585905),
    ("bng" , 0.5354099),
    ("msg" , 0.45632756),
    ("comport" , 0.71278006),
    ("change" , 0.65968746),
    ("floatatom" , 0.58062696),
    ("*~" , 0.6664535),
    ("dac~" , 0.833791),
    ("osc~" , 0.5178137),
    ("list_prepend", 0.71278006),
    ("list_trim" , 0.65968746),
    ("*" , 0.833791),
    ("tabread", 0.57799923)
]

heap = []
correct_heap = [(math.log(0.833791), '*'), (math.log(0.833791), 'dac~'), (math.log(0.71278006), 'comport'), (math.log(0.71278006), 'list_prepend'), (math.log(0.6664535), '*~'), (math.log(0.65968746), 'list_trim'), (math.log(0.65968746), 'change'), (math.log(0.59585905), 'sel'), (math.log(0.58062696), 'floatatom'), (math.log(0.57799923), 'tabread')]
returned_heap = insert_heap(heap, list_of_tokens_with_their_probability, max_heap_size)

for i in range(len(correct_heap)):
    assert (correct_heap[i][0] == returned_heap[i][0] and correct_heap[i][1] == returned_heap[i][1])
print("Passed test case 6\n")

# Test case 7

print("Test case 7 with more than max_heap_size elements and same probabilities for all elements")
list_of_tokens_with_their_probability = [
    ("sel" , 0.59585905),
    ("bng" , 0.59585905),
    ("msg" , 0.59585905),
    ("comport" , 0.59585905),
    ("change" , 0.59585905),
    ("floatatom" , 0.59585905),
    ("*~" , 0.59585905),
    ("dac~" , 0.59585905),
    ("*" , 0.59585905),
    ("osc~" , 0.59585905),
    ("list_prepend", 0.59585905),
    ("list_trim" , 0.59585905),
    ("tabread", 0.59585905)
]

heap = []
returned_heap = insert_heap(heap, list_of_tokens_with_their_probability, max_heap_size)
print("Nothing to assert in this test case since all the probabilities are the same\n\n")
print("All test cases passed")

