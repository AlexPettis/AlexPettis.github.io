data = open("data.txt", 'r')

total = 0
count = 0
missing = 0
min_value = float('inf')
max_value = float('-inf')

for line in data:
    line = line.strip()
    number = float(line)
    total += number
    count += 1
    if number != -1 and number < min_value:
        min_value = min(number, min_value)
    if number != -1 and number > max_value:
        max_value = max(number, max_value)
    if number == -1:
        missing = missing + 1
print(f"The total number of lines is {count}")
print(f"The min value is {min_value}")
print(f"The max value is {max_value}")
print(f"The mean is {total/count:.2f}")
print(f"The number of missing values is {missing}")

data.close()

