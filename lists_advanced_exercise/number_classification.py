number_list = [int(n) for n in input().split(", ")]

negative = []
positive = []
odd = []
even = []
[positive.append(number) if number >= 0 else negative.append(number) for number in number_list]
[even.append(number) if number % 2 == 0 else odd.append(number) for number in number_list]

print("Positive:", end=" ")
print(*positive, sep=", ")
print("Negative:", end=" ")
print(*negative, sep=", ")
print("Even:", end=" ")
print(*even, sep=", ")
print("Odd:", end=" ")
print(*odd, sep=", ")