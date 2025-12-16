response_times = [245, 189, 523, 201, 445, 167, 892, 234]

for response_time in response_times:
    print(f"Response: {response_time}ms")   # Python uses indentation to define code blocks. The print statement must be indented beneath the for loop line to indicate it is part of the loop's execution block.

print("Total number of responses:") 

print(len(response_times))

print("Response times in ascending order")

response_times.sort()

print(response_times)

print("Response times in descending order")

response_times.sort(reverse=True)

print(response_times)


fastest_response = response_times[-1]

print(f"Fastest response: {fastest_response}")

slowest_response = response_times[0]

print(f"Slowest response: {slowest_response}")

print(f"Response Time +2-> {response_times[+2]}")
print(f"Response Time -2-> {response_times[-2]}")

total_time = sum(response_times)
print(f"Total response time: {total_time}")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Count from start to end (inclusive)
for num in range(start, end + 1):
    print(num)


nstart = int(input("Enter the starting number: "))
nend = int(input("Enter the ending number: "))

current = nstart

if nstart <= nend:
    while current <= nend:
        print(current)
        current += 1
else:
    while current >= nend:
        print(current)
        current -= 1