# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:

# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

nums_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(nums_list)

nums = list(filter(lambda x: nums_list.count(x)==1, nums_list))
print(f'Список уникальных элементов {nums}')