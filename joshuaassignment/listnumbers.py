data = [1,2,3,4,5]
double = [number * 2 for number in data]
even = [number for number in double if number%2==0]
the_sum = sum(even)
print(the_sum)