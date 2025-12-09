

# iaasn00583690.NAEAST.ad.jpmorganchase.com
# \\iaasn00583690.NAEAST.ad.jpmorganchase.com\epvdocs$\ProdSupport\Tejas\sre-training\python

log_entry = "  2024-12-07 14:35:22 ERROR prod-api-03 Database_connection_timeout  "

# ```
# **Your script should:**
# 1. Remove leading/trailing whitespace
# 2. Extract the date (first part)
# 3. Extract the time (second part)
# 4. Extract the severity level (third part)
# 5. Extract the server name (fourth part)
# 6. Extract the error message (remaining parts joined together)
# 7. Clean up the error message (replace underscores with spaces)
# 8. Print a formatted alert message using f-strings

# **Expected Output:**
# ```
# ========================================
# ALERT NOTIFICATION
# ========================================
# Date: 2024-12-07
# Time: 14:35:22
# Severity: ERROR
# Server: prod-api-03
# Error: Database connection timeout
# ========================================
# ```

# Remove leading/trailing whitespace
rem_ws = log_entry.strip()

# Change it to a list
l_rem_ws = rem_ws.split()

# Extract the date (first part)
date = l_rem_ws[0]

# Extract the time (second part)
time = l_rem_ws[1]

# Extract the severity level (third part)
sev = l_rem_ws[2]

#  Extract the server name (fourth part)
serv_name = l_rem_ws[3]

# Extract the error message
err_mess = l_rem_ws[4]
form_err_mess = err_mess.replace("_"," ")

# Print a formatted alert message using f-strings
print(f"Date -> {date}, Time -> {time}, Severity -> {sev},  Server Name -> {serv_name},  Error Message -> {form_err_mess}") 

alert = f"""========================================
ALERT NOTIFICATION
========================================
Date: {date}
Time: {time}
Severity: {sev}
Server: {serv_name}
Error: {form_err_mess}
========================================"""
print(alert)