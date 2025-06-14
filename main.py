# 
# ================================
# 📘 PURPOSE
# This script demonstrates how Python's built-in `max()` and `sort()` behave
# when applied to a list of strings. It also includes explanation of
# assignment operations like `i = i + int` inside a loop.
# ================================

# List of strings to work with
l = ["flower", "flow", "flight"]

print("\nOriginal List:", l)

# --------------------------------
# 1️⃣ max(l): Lexicographical Comparison
# --------------------------------
# By default, max() compares strings in lexicographical order (dictionary order).
# Longer strings with the same prefix come after.
lexical_max = max(l)
print("\nmax(l) — Lexicographical Maximum:", lexical_max)

# --------------------------------
# 2️⃣ max(l, key=len): Maximum by Length
# --------------------------------
# You can use `key=len` to get the longest string in the list.
length_max = max(l, key=len)
print("max(l, key=len) — Longest String:", length_max)

# --------------------------------
# 3️⃣ Sorted by Length (using sorted, returns new list)
# --------------------------------
sorted_by_length = sorted(l, key=lambda x: len(x))
print("\nSorted by Length using sorted():", sorted_by_length)

# --------------------------------
# 4️⃣ Sorting In-place using .sort() (returns None)
# --------------------------------
l.sort(key=lambda x: len(x))
print("List after in-place sort using .sort():", l)

# --------------------------------
# 5️⃣ Assignment inside loop: i = i + int has no side effect
# --------------------------------
# Demonstrating that reassigning a loop variable doesn't affect the loop itself.
print("\nDemonstrating i = i + int inside for loop:")

for i in range(3):
    print(f"Before reassignment: i = {i}")
    i = i + 100  # Has no effect on loop iteration
    print(f"After reassignment: i = {i}")

print("\nNote: The reassignment i = i + 100 does NOT affect the loop iteration.")
