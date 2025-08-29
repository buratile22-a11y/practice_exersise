# 1. Write a program to check if a number is even or odd.
def even_or_odd():
    n = int(input("Enter a number: "))
    print("Even" if n % 2 == 0 else "Odd")

even_or_odd()

# 2. Given three numbers, find the largest one using if-elif-else.
def largest_of_three():
    a = int(input("Enter first: "))
    b = int(input("Enter second: "))
    c = int(input("Enter third: "))
    print(f"Largest: {max(a, b, c)}")

largest_of_three()

# 3. Write a program that categorizes a given age into child (<13), teen (13-19), adult (20+).
def categorize_age():
    age = int(input("Enter age: "))
    if age < 13:
        print("Child")
    elif age < 20:
        print("Teen")
    else:
        print("Adult")

categorize_age()

# 4. Given three sides of a triangle, determine if it’s equilateral, isosceles, or scalene.
def triangle_type():
    a = int(input("Side A: "))
    b = int(input("Side B: "))
    c = int(input("Side C: "))
    if a == b == c:
        print("Equilateral")]
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

triangle_type()
#1. Write a program that takes a user's name and age as input and prints: "Hello [name], you are [age] years old

def user():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello {name}, you are {age} years old.")

user()

# 2. Write a program that takes two numbers and prints their sum.

def numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Sum: {a + b}")

numbers()

# 3. Write a program that reads a file and counts the number of words in it.
def words():
    filename = input("Enter the file name to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print(f"The file contains {word_count} words.")
    except FileNotFoundError:
        print("File not found.")

words()

# 4. Write a program that takes a sentence and writes it to a file in reverse order.

def reverse_string():
    s = input("Enter a string to reverse: ")
    print(f"Reversed: {s[::-1]}\n")

reverse_string()

# 5. Write a program that reads a CSV file and converts it into a dictionary.
import csv

def csv_to_dict():
    filename = input("Enter CSV filename: ")
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
            print("CSV converted to dictionary:")
            for item in data:
                print(item)
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print("Error reading CSV:", e)

csv_to_dict()

# 6. Write a script that monitors a log file and alerts if a specific keyword appears.
import os
import time
def monitor_log_file():
    filename = input("Enter log file name to monitor: ")
    keyword = input("Enter keyword to alert on: ")
    
    if not os.path.isfile(filename):
        print("File does not exist.")
        return

    print(f"Monitoring '{filename}' for keyword '{keyword}'... Press Ctrl+C to stop.")
    try:
        with open(filename, 'r') as file:
            file.seek(0, os.SEEK_END)
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.5)
                    continue
                if keyword in line:
                    print(f"[ALERT] Keyword '{keyword}' found: {line.strip()}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

monitor_log_file()
# I. Write a program to find the length of a tuple without using len().
def tuple_length():
    t = eval(input("Enter a tuple: "))
    count = 0
    for _ in t:
        count += 1
    print("Length of tuple:", count)

tuple_length()

# II. Create a tuple with numbers and print the maximum and minimum values.\
def tuple_min_max():
    t = eval(input("Enter a tuple of numbers: "))
    print("Min:", min(t))
    print("Max:", max(t))

tuple_min_max()

# III. Write a program to remove duplicates from a list.
def remove_duplicates():
    lst = eval(input("Enter a list: "))
    print("List without duplicates:", list(set(lst)))

remove_duplicates()

# IV. Given a list [1, 2, 3, 4, 5], square each element and store it in a new list.
def square_list():
    lst = [1, 2, 3, 4, 5]
    squared = [x**2 for x in lst]
    print("Original:", lst)
    print("Squared :", squared)

square_list()

# V. Write a program to merge two dictionaries.
def merge_dicts():
    d1 = eval(input("Enter first dictionary: "))
    d2 = eval(input("Enter second dictionary: "))
    merged = {**d1, **d2}
    print("Merged Dictionary:", merged)

merge_dicts()

# VI. Given a dictionary {'a': 1, 'b': 2, 'c': 3}, swap keys and values (output: {1: 'a', 2: 'b', 3: 'c'}).
def swap_dict():
    d = {'a': 1, 'b': 2, 'c': 3}
    swapped = {v: k for k, v in d.items()}
    print("Original:", d)
    print("Swapped :", swapped)

swap_dict()

# VII. Write a function that returns the n-th Fibonacci number using memoization (optimization)
def fib(n, m={}): return m[n] if n in m else n if n<2 else m.setdefault(n, fib(n-1,m)+fib(n-2,m))

name = input("Name: ")
print(f"Hi, {name}!\nFibonacci:")
print(fib(int(input("n = "))))

# VIII. Implement a list comprehension that generates all Pythagorean triplets up to n.
def pythagorean_triplets():
    n = int(input("Generate triplets up to: "))
    triplets = [(a, b, c)
                for a in range(1, n)
                for b in range(a, n)
                for c in range(b, n)
                if a**2 + b**2 == c**2]
    print("Triplets:", triplets)

pythagorean_triplets()

# IX. Write a function that simulates a shopping cart using nested dictionaries (add/remove items, calculate total).
def shopping_cart():
    cart = {}
    while True:
        print("\nShopping Cart Menu")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Checkout")
        choice = input("Choice: ")
        if choice == "1":
            item = input("Item name: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            cart[item] = {"price": price, "quantity": qty}
        elif choice == "2":
            item = input("Item to remove: ")
            if item in cart:
                del cart[item]
        elif choice == "3":
            print(cart)
        elif choice == "4":
            total = sum(v["price"] * v["quantity"] for v in cart.values())
            print("Total cost: $", total)
            break
        else:
            print("Invalid choice")

shopping_cart()

# X. Implement a dictionary-based cache system with a max_size (LRU eviction).

from collections import OrderedDict
from mimetypes import init

class LRUCache:
    def init(self, max_size=5):
        self.cache = OrderedDict()
        self.max_size = max_size

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)  

init()

# XI. Write a function that takes a tuple of numbers and returns a new tuple with only even numbers.

def even_in_tuple():
    t = eval(input("Enter tuple of numbers: "))
    even_t = tuple(x for x in t if x % 2 == 0)
    print("Even numbers tuple:", even_t)

even_in_tuple()
# XII. Write a program to sort a list of tuples based on the second element (e.g., [('a', 3), ('b', 1)] → [('b', 1), ('a', 3)]).
def sort_tuples():
    lst = eval(input("Enter list of tuples: "))
    sorted_lst = sorted(lst, key=lambda x: x[1])
    print("Sorted list:", sorted_lst)

sort_tuples()

# XIII. Write a function to flatten a nested list (e.g., [[1, 2], [3, 4]] → [1, 2, 3, 4]).
def flatten_list():
    nested = eval(input("Enter nested list: "))
    flat = [x for sub in nested for x in sub]
    print("Flattened list:", flat)

flatten_list()

# XIV. Write a program to remove all occurrences of a specific element from a list.
def remove_all_occurrences():
    lst = eval(input("Enter list: "))
    val = eval(input("Enter value to remove: "))
    filtered = [x for x in lst if x != val]
    print("Resulting list:", filtered)

remove_all_occurrences()

# XV. Write a function that inverts a dictionary (handle duplicate values by storing them in a list).
def invert(d):
    inv = {}
    for k, v in d.items(): inv.setdefault(v, []).append(k)
    return inv

d = {int(input(f"Key {_+1}: ")): int(input("Value: ")) for _ in range(int(input("How many pairs? ")))}
print("Inverted:", invert(d))
# XVI. Given a dictionary of student marks, find the student with the highest average score.
def highest_avg_student():
    students = eval(input("Enter student marks (e.g. {'John': [80,90]}): "))
    avg_scores = {name: sum(marks)/len(marks) for name, marks in students.items()}
    best = max(avg_scores, key=avg_scores.get)
    print(f"Top student: {best} with average {avg_scores[best]:.2f}")

highest_avg_student()
# 1. Write a Python program to reverse a given string (e.g., "hello" → "olleh").

def reverse_string():
    text = input("Enter a string to reverse: ")
    print("Reversed string:", text[::-1])

reverse_string()

# 2. Write a program that counts the number of vowels (a, e, i, o, u) in a given string.

def count_vowels():
    text = input("Enter a string: ")
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in text if char in vowels)
    print("Number of vowels:", count)

count_vowels()
# 3. Write a function that checks if two strings are anagrams (e.g., "listen" and "silent").

def are_anagrams():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print("Are anagrams?" , sorted(s1) == sorted(s2))

are_anagrams()
# 4. Write a program to count the occurrences of each word in a given sentence.

def word_occurrences():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    counts = {word: words.count(word) for word in set(words)}
    print("Word counts:", counts)

word_occurrences()
# 5. Write a function that implements the Caesar Cipher (shift letters by n positions).

def caesar_cipher():
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))
    cipher = ''.join(
        chr((ord(c) - ord('a') + shift) % 26 + ord('a')) if c.islower()
        else chr((ord(c) - ord('A') + shift) % 26 + ord('A')) if c.isupper()
        else c for c in text
    )
    print("Encrypted text:", cipher)

caesar_cipher()
# 6. Write a regex-based program to validate an email address.
import re

def validate_email():
    email = input("Enter an email address: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

validate_email()
# 1. Write a function that takes a number and returns its square.
def square_number():
    try:
        n = float(input("Enter a number: "))
        print(f"Square of {n} is {n ** 2}")
    except ValueError:
        print("Please enter a valid number.")

square_number()

# 2. Write a function that checks if a string is a palindrome (e.g., "madam").

def check_palindrome():
    s = input("Enter a string: ")
    if s == s[::-1]:
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")

check_palindrome()

# 3. Write a decorator that logs the execution time of a function.
import time

def log_time(f):
    def w(): s=time.time(); r=f(); print(f"Time: {time.time()-s:.6f}s"); return r
    return w

@log_time
def add():
    print("Sum:", sum(map(int, input("Enter numbers: ").split())))

add()

# 4. Write a generator function that yields an infinite sequence of prime numbers
def primes():
    D, q = {}, 2
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]: D.setdefault(p+q, []).append(p)
            del D[q]
        q += 1

n = int(input("How many primes? "))
gen = primes()
for _ in range(n):
    print(next(gen))
    # 1) Print numbers from 1 to 10 using a for loop.

def number_printer():
    choice = input("Choose an option:\n1) Print numbers from 1 to 10\n> ")
    if choice == "1":
        for i in range(1, 11):
            print(i)
    else:
        print("Invalid option.")

number_printer()



# 2) Print the multiplication table of a given number using a while loop.
def multiplication_table():
    n = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

multiplication_table()



# 3) Print a pyramid pattern using * 
def pyramid():
    n = int(input("Enter height of pyramid: "))
    for i in range(1, n+1):
        print('*' * i)
pyramid()


# 4) Write a program to find all prime numbers up to a given number.
def prime_numbers():
    limit = int(input("Find primes up to: "))
    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            print(num, end=" ")
    print()

prime_numbers()



# 5) Functions (recursion, args/kwargs)

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def sum_args(*args):
    return sum(args)

n = int(input("Enter a number to calculate its factorial (recursion): "))
print("Factorial:", factorial(n))

nums = input("Enter numbers separated by spaces to sum them (*args): ")
nums = list(map(int, nums.split()))
print("Sum:", sum_args(*nums))


# 6) Write a recursive function to compute the factorial of a number.

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

n = int(input("Enter a number to compute its factorial: "))
print(f"Factorial of {n} is {factorial(n)}")



# 7) Write a function that accepts any number of arguments and returns their sum.

def sum_args(*args):
    return sum(args)

nums = input("Enter numbers separated by spaces to sum: ")
nums = list(map(int, nums.split()))
print("The sum is:", sum_args(*nums))


# 8) Write a loop that prints numbers from 1 to 10 but skips 5 using continue.
print("Printing numbers from 1 to 10, skipping 5:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)



# 9) Write a loop that stops when it encounters the number 7 using break.
print("Printing numbers from 1 to 10, stopping at 7:")
for i in range(1, 11):
    if i == 7:
        break
    print(i)


# 10) Write a program to solve the Tower of Hanoi problem recursively.

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        tower_of_hanoi(n-1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        tower_of_hanoi(n-1, auxiliary, target, source)

n = int(input("Enter number of disks for Tower of Hanoi: "))
tower_of_hanoi(n, 'A', 'C', 'B')



# 11) Simulate a tic-tac-toe game using loops and conditionals.

def tic_tac_toe():
    board = [" "]*9

    def print_board():
        for i in range(0, 9, 3):
            print(" | ".join(board[i:i+3]))
            if i < 6: print("-"*5)

    player = "X"
    for turn in range(9):
        print_board()
        move = int(input(f"Player {player}, choose position (1-9): ")) - 1
        if 0 <= move < 9 and board[move] == " ":
            board[move] = player
            # Check win
            wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
            if any(board[a]==board[b]==board[c]==player for a,b,c in wins):
                print_board()
                print(f"Player {player} wins!")
                return
            player = "O" if player == "X" else "X"
        else:
            print("Invalid move. Try again.")
    print_board()
    print("It's a draw!")
    print("prepaired by bura.t")
tic_tac_toe()
