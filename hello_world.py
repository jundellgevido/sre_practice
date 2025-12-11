# print Hello World
print("Hello World")

# Variables and Data Types
server = "web-01"
status = 'running'
cpu_count = 8
memory = 16.5
is_online= True
has_error = False

hostname = "web-01"
port = 8080
print(hostname)
print(port*2)

cpu_usage = 85.5
threshold = 90
needs_alert = cpu_usage > threshold

count = 0
count = 5
count += 1

print(cpu_usage)
print(f"CPU:{cpu_usage}%")
print(f"Memory:{memory}GB")
print(is_online)

server = 'prod-web-01'
message = "ERROR: Connection timeout"
hostname = server + '-' + '01'
alert = 'Host:' + hostname

print(hostname)
print(alert)