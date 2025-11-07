# Question-1 Counting Positive Numbers in a List # noqa: CPY001, D100, INP001

num_list: list[int] = [-1, -2, 3, 4, -5, 6, -7, -8, 9, 10]
count = 0

for num in num_list:
	if num > 0:
		print(num)
		count += 1

print(f"Number of positive numbers in {num_list} List is: {count}")
