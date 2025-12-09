# Interactive Recap Exercise: Git + Python Sessions 1-2
## Duration: 15-20 minutes

---

## 🎯 **Learning Objectives**
This exercise combines:
- ✅ Git: clone, add, commit, push, branches
- ✅ Python Session 1: variables, data types, print, comments
- ✅ Python Session 2: strings, .split(), .strip(), .replace(), f-strings

---

## 📋 **Scenario**
You're an SRE who needs to:
1. Clone a team repository
2. Create a Python script that parses application log entries
3. Extract server name, timestamp, and error message
4. Commit your work to Git

---

## 🔨 **Exercise Instructions**

### **Part 1: Git Setup (5 minutes)**

**Step 1:** Create a new directory for this exercise
```bash
cd ~/Desktop
mkdir sre-log-parser
cd sre-log-parser
```

**Step 2:** Initialize Git repository
```bash
git init
```

**Step 3:** Configure your Git identity (if not done already)
```bash
git config user.name "Your Name"
git config user.email "your.email@company.com"
```

**Step 4:** Create a new branch for your work
```bash
git checkout -b feature/log-parser
```

---

### **Part 2: Python Script (10 minutes)**

**Step 5:** Create a new Python file called `log_parser.py`

**Step 6:** Write a Python script that does the following:

**Given this log entry:**
```
log_entry = "  2024-12-07 14:35:22 ERROR prod-api-03 Database_connection_timeout  "
```

**Your script should:**
1. Remove leading/trailing whitespace
2. Extract the date (first part)
3. Extract the time (second part)
4. Extract the severity level (third part)
5. Extract the server name (fourth part)
6. Extract the error message (remaining parts joined together)
7. Clean up the error message (replace underscores with spaces)
8. Print a formatted alert message using f-strings

**Expected Output:**
```
========================================
ALERT NOTIFICATION
========================================
Date: 2024-12-07
Time: 14:35:22
Severity: ERROR
Server: prod-api-03
Error: Database connection timeout
========================================
```

---

### **Part 3: Git Commit (5 minutes)**

**Step 7:** Add your file to staging
```bash
git add log_parser.py
```

**Step 8:** Commit with a meaningful message
```bash
git commit -m "Add log parser script for error notifications"
```

**Step 9:** Check your Git status and log
```bash
git status
git log --oneline
```

**Step 10:** (Optional) Merge to main branch
```bash
git checkout main
git merge feature/log-parser
```

---

## 💡 **Hints**
- Remember to use `.strip()` to clean whitespace
- Use `.split()` to break the log into parts
- Access parts with [0], [1], [2], etc. (we'll learn more about this in Session 3!)
- Use `.replace("_", " ")` to clean the error message
- F-strings format: `f"Text {variable}"`
- Don't forget comments in your Python code!

---

## ❓ **Questions to Consider**
1. Why do we create a feature branch instead of working directly on main?
2. What would happen if you forgot to use `.strip()` on the log entry?
3. How would you modify this script to handle different log formats?

---

## 🎓 **What This Exercise Covers**

### **Git Skills:**
- ✅ Initialize repository (`git init`)
- ✅ Create branches (`git checkout -b`)
- ✅ Stage changes (`git add`)
- ✅ Commit changes (`git commit`)
- ✅ Check status (`git status`)
- ✅ View history (`git log`)
- ✅ Merge branches (`git merge`)

### **Python Session 1:**
- ✅ Variables (storing strings)
- ✅ Data types (strings)
- ✅ Print statements
- ✅ Comments

### **Python Session 2:**
- ✅ String methods (`.strip()`, `.split()`, `.replace()`)
- ✅ String indexing (`parts[0]`, `parts[1]`)
- ✅ F-strings for formatting
- ✅ String concatenation

---

## 🏆 **Success Criteria**
- [ ] Git repository initialized
- [ ] Feature branch created
- [ ] Python script created and working
- [ ] Correct output displayed
- [ ] Changes committed to Git
- [ ] Can explain what each line of code does

---
