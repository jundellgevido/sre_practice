# Quick Reference: Interactive Recap Exercise
## Cheat Sheet for Students

---

## 🔧 **Git Commands You'll Need**

```bash
# Initialize Git
git init

# Create and switch to new branch
git checkout -b feature/log-parser

# Check current branch
git branch

# Stage files
git add filename.py

# Commit changes
git commit -m "Your message here"

# Check status
git status
git branch -vv

# View commit history
git log --oneline

# to Push the branch from local to the github repository branch
git push -u origin feature/log-parser


# Merge feature branch into current branch
git merge feature/log-parser

# Switch to main branch
git checkout main

```



---

## 🐍 **Python String Methods Refresher**

### **Remove Whitespace:**
```python
text = "  hello  "
clean = text.strip()  # → "hello"
```

### **Split into Parts:**
```python
text = "apple banana cherry"
parts = text.split()  # → ['apple', 'banana', 'cherry']
```

### **Access Parts (Indexing):**
```python
parts = ['apple', 'banana', 'cherry']
first = parts[0]   # → 'apple'
second = parts[1]  # → 'banana'
third = parts[2]   # → 'cherry'
```

### **Replace Text:**
```python
text = "hello_world"
fixed = text.replace("_", " ")  # → "hello world"
```

### **F-strings (Formatting):**
```python
name = "Alice"
age = 30
message = f"Hello {name}, you are {age} years old"
# → "Hello Alice, you are 30 years old"
```

---

## 📝 **Exercise Quick Start**

### **1. Setup (2 minutes)**
```bash
mkdir sre-log-parser
cd sre-log-parser
git init
git checkout -b feature/log-parser
```

### **2. Create Python File (1 minute)**
Create `log_parser.py` in VS Code or text editor

### **3. Your Log Entry**
```python
log_entry = "  2024-12-07 14:35:22 ERROR prod-api-03 Database_connection_timeout  "
```

### **4. What to Extract**
- Date: `2024-12-07`
- Time: `14:35:22`
- Severity: `ERROR`
- Server: `prod-api-03`
- Error: `Database connection timeout` (clean the underscores!)

### **5. Git Commit (2 minutes)**
```bash
git add log_parser.py
git commit -m "Add log parser script for error notifications"
git status
```

---

## 💡 **Key Reminders**

✅ **Always `.strip()` first** - removes spaces  
✅ **Save results** - strings don't change in-place  
✅ **Indexing starts at 0** - first item is [0], not [1]  
✅ **Git add before commit** - changes must be staged  
✅ **Use f-strings** - easier than concatenation  

---

## 🎯 **Expected Output**

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

## ❓ **Stuck? Try This**

### **Python not working?**
1. Check quotes match: `"text"` or `'text'`
2. Check indentation (none needed yet!)
3. Check variable names match
4. Print intermediate steps: `print(parts)`

### **Git not working?**
1. Are you in the right directory? (`pwd`)
2. Did you `git init`?
3. Did you `git add` before `git commit`?
4. Check status: `git status`

---

## 📚 **What We're Reviewing**

| Concept | Session | Example |
|---------|---------|---------|
| Variables | 1 | `name = "Alice"` |
| Print | 1 | `print("Hello")` |
| Comments | 1 | `# This is a comment` |
| .strip() | 2 | `text.strip()` |
| .split() | 2 | `text.split()` |
| .replace() | 2 | `text.replace("_", " ")` |
| Indexing | 2 | `parts[0]` |
| F-strings | 2 | `f"Hello {name}"` |
| git init | Git | Initialize repo |
| git branch | Git | Create branch |
| git commit | Git | Save changes |

---

## 🏁 **Success = You Can:**

- [ ] Create a Git repository
- [ ] Create a feature branch
- [ ] Write a Python script that parses strings
- [ ] Use .strip(), .split(), .replace()
- [ ] Use f-strings for formatting
- [ ] Commit your work to Git
- [ ] Explain what each line does

---

## 👥 **Need Help?**

1. Check this cheat sheet
2. Try printing intermediate values: `print(parts)`
3. Ask a neighbor
4. Raise your hand for instructor help

**Remember:** Everyone learns at different speeds. Take your time!

---
