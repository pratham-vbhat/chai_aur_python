# Question-2: Sum of Even Numbers:


def sum_of_even_num(
	start_num: int,
	end_num: int,
) -> int:
	even_num = 0
	for num in range(start_num, end_num):
		if num % 2 == 0:
			even_num += num
	return even_num


start_num = int(input("Enter the start range of Number: "))
end_num = int(input("Enter the End range of number:"))

result_even_num = sum_of_even_num(start_num, end_num)

print(
	f"Sum of all the even numbers between the range {start_num} and {end_num} is: {
		result_even_num
	}",
)
