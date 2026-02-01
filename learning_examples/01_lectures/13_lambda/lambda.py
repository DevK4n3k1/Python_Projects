##############################################
# With map()
##############################################
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8, 10]


##############################################
# With filter()
##############################################
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]


##############################################
# With sorted()
##############################################
words = ["apple", "banana", "kiwi"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ['kiwi', 'apple', 'banana']


##############################################
# Quick One-Off Calculations
##############################################
result = (lambda x, y: x * y)(3, 4)
print(result)  # 12




