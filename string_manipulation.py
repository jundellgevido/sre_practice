# string manipulation

# .strip() -Remove whitespace
#.split(delimiter) - Create list from string
# .startswith()/.endswith() - Pattern matching
#.replace(old,new) - Replace text
# .upper()/.lower() - Change case

log = "    ERROR: Disk space critical     "
clean = log.strip()
upper = log.upper()
lower = log.lower()

print(clean)
print(upper)
print(lower)

starts = log.strip().startswith("ERROR")
ends = log.endswith("critical     ")
                    
parts = "prod-web-01".split("-")
csv_data = "name,age,city".split(",")

print(parts)
print(csv_data)

readable = "DB_timeout".replace("_"," ")
print(readable)

server = "prod-web-01"
env = server[0:4]
service = server[5:8]
last_two = server[-2:]

print(server)
print(env)
print(server)
print(last_two)

timestamp = "2025-11-24 15:30:45"
date = timestamp[:10]
time = timestamp[11:]

print(date)
print(time)

server = "prod-web-01"
cpu = 85.7
memory = 12.4

print(f"Server {server} CPU at {cpu}%")
print(f"Memory {memory:.1f}GB ({memory/16*100:.0f}%)")
print(f"Memory {memory:.2f}GB ({memory/16*100:.2f}%)")      

report = f"{server}: CPU={cpu}%, Memory={memory}GB"
print(report)
print()

total_memory = memory / 16 * 100
print(f"Memory usage: {total_memory:.0f}%")
print()

log = "2025-11-24 15:30:45 ERROR prod-api-01 DB_timeout"

parts = log.split() 
print(parts)

time = parts[0]
severity = parts[2]
server = parts[3]
error = parts[4]

alert = f"[{severity}] {server} at {time}: {error}"
print(alert)

# Chapter assignment

snippet = "  2024-11-24 10:15:33 INFO prod-api-03 Response_time=245ms status=200  "
fsnip = snippet.strip()

snip = fsnip.split()
date = snip[0]
time = snip[1]
server = snip[3]
resp = snip[4].split('=')[1]
response_time = resp.replace('ms','')
status = snip[5].split('=')[1]

print(f"Date {date}, Time {time}, Server: {server}, Response Time {response_time}ms,  Status {status}")
