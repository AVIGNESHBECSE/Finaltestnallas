#1. Write a Python program to check if a given number is prime.
# def prime(num):
#     Flag=False
#     if num<2:
#         return Flag
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 return Flag
#             else:
#                 Flag=True
#                 return Flag
# n=int(input("Enter value:"))
# print(prime(n))
#prime(n)
# #Another method
# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return True
#     return True
# def prime_generater(n):
#     num=2
#     while n:
#         if prime(num):
#             yield num
#             n-=1
#         num+=1
# x=int(input("Enter number:"))
# t=prime_generater(x)
# for e in t:
#     print(e,end=" ")
#2. Write a Python function to find the factorial of a number using recursion.
# def fac(i):
#     if i==0 or i==1:
#         return 1
#     return i*fac(i-1)
# n=int(input("enter number:"))
# print(fac(n))
#3. Implement a Python program to check if a given string is a palindrome.
# str="Programming".lower()
# if str==str[::-1]:
#     print("True")
# else:
#     print("False")
#4. Write a Python script to count the number of vowels in a given string.
# vow=['a','e','i','o','u','A','E','I','O','U']
# val=input("Enter word:")
# cout=0
# for ch in val:
#     if ch in vow:
#         cout+=1
#
# print(cout)
#5. Implement a function to swap two numbers without using a temporary variable.
# def sw(a,b):
#     a,b=b,a
#     return a,b
# x=int(input("Enter x:"))
# y=int(input("Enter y:"))
# x,y=sw(x,y)
# print(f"swapping:x={x},y={y}")
#6. Write a program to find the sum of digits of a given number using bitwise operators.
# def sum_of(n):
#     total=0
#     while n:
#         total+=n&0xF
#         n//=10
#     return total
# num=int(input("Enter:"))
# print(f"Sum:{sum_of(num)}")
#7. Implement a Python function that checks if two numbers have opposite signs using bitwise operations.
# def opp(a,b):
#     return (a^b)<0
# x,y=map(int,input("Enter values:").split())
# print("Op"if opp(x,y) else "same sign")
#8. Write a program that demonstrates the use of the ternary operator in Python.
# a,b=map(int,input("Enter number:").split())
# value=a if a<b else b
# print("Smallar value:",value)
#9. Implement a Python function to perform arithmetic operations without using built-in arithmetic operators.
# def add(x,y):
#     while y:
#         carray=x&y
#         x=x^y
#         y=carray<<1
#     return x
# def subtract(x,y):
#     while y:
#         borrow=(~x)&y
#         x=x^y
#         y=borrow<<1
#     return x
# x,y=map(int,input("Enter:").split())
# x,y=map(int,input("Enter number:").split())
# print("sum",add(x,y))
# print("Difference",subtract(x,y))
#10. Write a program to demonstrate operator precedence with different examples.
# a=5
# b=2
# c=3
# a1=a+b*c
# b1=(a+b)*c
# c1=10-c<<b
# print(a1,b1,c1)
#11.Write a Python program to print the Fibonacci series up to `n` terms using loops.
# def fibonac(n):
#     fib=[0,1]
#     for i in range(2,n):
#         fib.append(fib[-1]+fib[-2])
#     return fib
# n=int(input("Enter Digite:"))
# result=fibonac(n)
# print("Fibonacci series:",result)
#12. Write a function that takes an integer `n` and prints a pattern using nested loops.
# def parten(n):
#     if n>0:
#         parten(n-1)
#         print('*'*n)
# rows=int(input("Enter the number of rows:"))
# parten(rows)
#13. Implement a program that finds all Armstrong numbers between a given range.
# def arm(n):
#     power=len(str(n))
#     return n==sum(int(digit)**power for digit in str(n))
# def arm_ran(start,end):
#     for num in range(start,end+1):
#         if arm(num):
#             print(num,end=" ")
# start,end=map(int,input("Enter range:").split())
# arm_ran(start, end)
# 14. Write a program to remove all duplicate elements from a list using loops.
#
# a=[1,2,2,3,4,4,5]
# unique_list=[]
# for x in a:
#     if x not in unique_list:
#         unique_list.append(x)
# print(unique_list)
# 15. Implement a function that checks if a given number is a strong number.
# def strong(n):
#     digits=[int(d) for d in str(n)]
#     sum=0
#     for d in digits:
#         f=1
#         for i in range(1,d+1):
#             f*=1
#         sum+=f
#     if sum==n:
#         return "yes"
#     else:
#         return "No"
# n=int(input("Enter number:"))
# print(strong(n))
#
#
# Data Structures & Collections
# 16. Write a Python program to reverse a list without using built-in functions.
# a=[1,2,3,4,5]
# res=[]
# for val in a:
#     res.insert(0,val)
# print(res)
# 17. Implement a linked list in Python with insert and delete operations.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def delete(self, key):
#         temp = self.head
#         if temp and temp.data == key:
#             self.head = temp.next
#             return
#
#         prev = None
#         while temp and temp.data != key:
#             prev = temp
#             temp = temp.next
#
#         if temp:
#             prev.next = temp.next
#
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")
# ll = LinkedList()
# ll.insert(10)
# ll.insert(20)
# ll.insert(30)
# ll.display()
# ll.delete(20)
# ll.display()
# 18. Write a function to merge two sorted lists into one sorted list.
# def merge_sorted_lists(lst1, lst2):
#     i, j = 0, 0
#     merged = []
#
#     while i < len(lst1) and j < len(lst2):
#         if lst1[i] < lst2[j]:
#             merged.append(lst1[i])
#             i += 1
#         else:
#             merged.append(lst2[j])
#             j += 1
#     merged.extend(lst1[i:])
#     merged.extend(lst2[j:])
#     return merged
#
# list1 = list(map(int, input("Enter first sorted list: ").split()))
# list2 = list(map(int, input("Enter second sorted list: ").split()))
# print("Merged sorted list:", merge_sorted_lists(list1, list2))
# 19. Implement a function to count the occurrences of each word in a given string using a dictionary.
# def word_count(s):
#     words = s.split()
#     freq = {}
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
#     return freq
#
# text = input("Enter a sentence: ")
# print("Word occurrences:", word_count(text))
# 20. Write a Python program to demonstrate the use of `heapq` for finding the `k` smallest elements in a list.
# import heapq
# def k_smallest(lst, k):
#     smallest_elements = heapq.nsmallest(k, lst)
#     smallest_indices = [i for i, val in enumerate(lst) if val in smallest_elements]
#     return smallest_indices
# list = [5, 4, 3, 2, 1]
# k =int(input("Enter k value:"))
# smallest_indices = k_smallest(list, k)
# print("The smallest index elements are:",smallest_indices)

# Functions & Functional Programming
# 21. Write a Python function that takes a list of numbers and returns a new list with only even numbers using filter().
# a = [1, 2, 3, 4, 5]
#
# res = list(filter(lambda num: num % 2 == 0, a))
# print(res)
# 22. Implement a Python program using `map()` to double all the elements in a list.
# a=[1,2,3,4,5]
# c=list(map(lambda x:x*2,a))
# print(c)
# 23. Write a decorator in Python that logs the execution time of a function.
# from time import time
# def timer_func(func):
#     def wrap_func(*args, **kwargs):
#         t1 = time()
#         result = func(*args, **kwargs)
#         t2 = time()
#         print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
#         return result
#     return wrap_func
#
# @timer_func
# def long_time(n):
#     for i in range(n):
#         for j in range(100000):
#             i * j
# long_time(5)
# 24. Implement a function using `*args` and `kwargs` that takes multiple arguments and prints them dynamically.
# def fun(*args):
#     return sum(args)
#
# print(fun(1,2,3,4))
# def fun(**kwargs):
#     for k, val in kwargs.items():
#         print(f"{k}:{val}")
#
# fun(a=1, b=2, c=3)
# 25. Write a Python function that returns a lambda function to calculate the square of a number.
# a=lambda x:x**2
# print(a(5))
# print((lambda x:x**2)(4))
#
#
#
# Object-Oriented Programming (OOP)
# 26. Write a Python class that represents a bank account with deposit and withdrawal methods.
# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited {amount}. New balance: {self.balance}")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             print(f"Withdrawn {amount}. New balance: {self.balance}")
#
# acc = BankAccount("Vignesh", 1000)
# acc.deposit(500)
# acc.withdraw(300)
# acc.withdraw(1500)
# 27. Implement a class with method overriding for a `Vehicle` class and its subclasses.
# class Vehicle:
#     def description(self):
#         return "This is a vehicle"
#
# class Car(Vehicle):
#     def description(self):
#         return "This is a car"
#
# class Bike(Vehicle):
#     def description(self):
#         return "This is a bike"
#
# v = Vehicle()
# c = Car()
# b = Bike()
#
# print(v.description())
# print(c.description())
# print(b.description())
# 28. Write a Python program demonstrating operator overloading for adding two objects.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
# p1 = Point(2, 3)
# p2 = Point(4, 5)
# p3 = p1 + p2
# print(p3)
# 29. Create a class that implements the `__str__` and `__repr__` methods differently.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Person: {self.name}, Age: {self.age}"
#
#     def __repr__(self):
#         return f"Person('{self.name}', {self.age})"
#
# p = Person("Vignesh", 25)
# #print(str(p))
# print(repr(p))
# 30. Implement a Python class that demonstrates the Singleton design pattern.
# class Singleton:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
# obj1 = Singleton()
# obj2 = Singleton()
#
# print(obj1 is obj2)
#
#
#
# File Handling & Modules
# 31. Write a Python program to read a text file and count the number of words.
# def count_words(filename):
#     with open(filename, "r") as file:
#         text = file.read()
#     words = text.split()
#     return len(words)
#
# filename = "vick.txt"
# print(f"Word count: {count_words(filename)}")
# 32. Implement a function that writes a list of dictionaries to a CSV file.
# import csv
# def write_to_csv(filename, data):
#     with open(filename, mode="w", newline="") as file:
#         writer = csv.DictWriter(file, fieldnames=data[0].keys())
#         writer.writeheader()
#         writer.writerows(data)
#
# data = [{"Name": "Vignesh", "Age": 22}, {"Name": "Kumar", "Age": 23},{"Name":"Ravi","Age":25},{"Name":"Ruthuran","Age":22}]
# write_to_csv("data.csv", data)
# print("CSV file written successfully.")
# 33. Write a script to scan a directory and list all files with a specific extension.
# import os
# def list_files(directory, extension):
#     return [f for f in os.listdir(directory) if f.endswith(extension)]
#
# directory = "./"
# extension = ".txt"
# print("Matching files:", list_files(directory, extension))
# 34.Implement a program that copies content from one file to another.
# file_read="source.txt"
# write_file="destination.txt"
# file=open(file_read,"r")
# data=file.read()
# file.close()
# with open(write_file,"a")as file:
#     file.write(data)
# print("File copied successfully")
# 35. Write a Python program that renames multiple files in a folder using `os` module.
# import os
# path="C:/Users/User/PycharmProjects/PythonProject1/Filehandling/"
# files=os.listdir(path)
# for i in range(len(files)):
#     source=path+files[i]
#     dest=path+str(i+1)
#     os.rename(source,dest)
# print("All files are renamed")
#
#
#
#
# Advanced Topics (Concurrency, Exception Handling, DB)
# 36. Write a program to demonstrate Python multithreading by printing numbers from 1 to 10 using two different threads.
# import threading
# def print_numbers():
#     for i in range(1, 11):
#         print(i)
# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_numbers)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# 37. Implement a Python function that executes two tasks in parallel using multiprocessing.
# import multiprocessing
# import time
# def task1():
#     for i in range(5):
#         print(f"Task 1 - Count: {i}")
#         time.sleep(1)
#
# def task2():
#     for i in range(5):
#         print(f"Task 2 - Count: {i}")
#         time.sleep(1)
#
# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=task1)
#     p2 = multiprocessing.Process(target=task2)
#
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
# 38. Write a Python program that connects to a PostgreSQL database and retrieves all records from a table.
# import psycopg2
# def fetch_records():
#     try:
#         conn = psycopg2.connect(
#             dbname="your_database",
#             user="your_username",
#             password="your_password",
#             host="localhost",
#             port="5432"
#         )
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM your_table")
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print("Error:", e)
# fetch_records()
# 39. Create a program that demonstrates raising a custom exception in Python.
# class CustomError(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
# def check_value(n):
#     if n < 0:
#         raise CustomError("Negative value not allowed!")
#     print("Valid number:", n)
# try:
#     check_value(-5)
# except CustomError as e:
#     print("Caught an error:", e)
# 40. Write a Python program that uses Flask to create a simple REST API with a single endpoint.
# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
# @app.route('/api/hello', methods=['GET'])
# def hello():
#     return jsonify({"message": "Hello, World!"})
#
# if __name__ == '__main__':
#     app.run(debug=True)


#
# Bonus Challenge Questions
# 41. Write a Python function to implement a queue using two stacks.
# class QueueUsingStacks:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def enqueue(self, item):
#         self.stack1.append(item)
#
#     def dequeue(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         if self.stack2:
#             return self.stack2.pop()
#         else:
#             return "Queue is empty!"
#
# q = QueueUsingStacks()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# 42. Implement a Least Recently Used (LRU) Cache using Python dictionaries.
# from collections import OrderedDict
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.capacity = capacity
#
#     def get(self, key: int):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#             return self.cache[key]
#         return -1
#
#     def put(self, key: int, value: int):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         elif len(self.cache) >= self.capacity:
#             self.cache.popitem(last=False)
#         self.cache[key] = value
#
# lru = LRUCache(2)
# lru.put(1, "A")
# lru.put(2, "B")
# print(lru.get(1))
# lru.put(3, "C")
# print(lru.get(2))
# 43. Write a program to solve the Tower of Hanoi problem using recursion.
# def tower_of_hanoi(n, source, auxiliary, target):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     tower_of_hanoi(n - 1, source, target, auxiliary)
#     print(f"Move disk {n} from {source} to {target}")
#     tower_of_hanoi(n - 1, auxiliary, source, target)
#
# tower_of_hanoi(3, "A", "B", "C")
# 44. Implement a Python function to find the longest substring without repeating characters.
# def longest_unique_substring(s):
#     char_index = {}
#     start = max_length = 0
#     for i, char in enumerate(s):
#         if char in char_index and char_index[char] >= start:
#             start = char_index[char] + 1
#         char_index[char] = i
#         max_length = max(max_length, i - start + 1)
#
#     return max_length
# print(longest_unique_substring("abcabcbb"))
# 45. Write a Python program that implements Dijkstra’s algorithm for shortest path finding.
# import heapq
# def dijkstra(graph, start):
#     min_heap = [(0, start)]
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#
#     while min_heap:
#         curr_distance, curr_node = heapq.heappop(min_heap)
#
#         if curr_distance > distances[curr_node]:
#             continue
#
#         for neighbor, weight in graph[curr_node].items():
#             distance = curr_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(min_heap, (distance, neighbor))
#
#     return distances
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }
# print(dijkstra(graph, 'A'))
