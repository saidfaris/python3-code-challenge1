# Coding Challenges

This repository contains solutions to three coding challenges. Each challenge focuses on solving a specific problem using Python. Below is a brief description of each challenge:

## Challenge 1: 12-hour to 24-hour Time Conversion

### Problem Description:
Convert a 12-hour time format (e.g., "8:30 am" or "8:30 pm") to a 24-hour time format (e.g., "0830" or "2030"). The input includes an hour (1 to 12), minutes (0 to 59), and a period ("am" or "pm").

### Solution:
A Python function is provided (`convert`) that takes the input time and performs the conversion. It accounts for special cases like midnight (12:00 AM) and noon (12:00 PM). The function returns a four-digit string representing the time in 24-hour format.

## Challenge 2: Exactly Two Positive Numbers

### Problem Description:
Given three integers (a, b, c), determine whether exactly two of them are positive numbers (greater than zero). Return `True` if this condition is met, otherwise return `False`.

### Solution:
A Python function (`exactly_two_positive`) checks the positivity of the three integers and returns `True` if exactly two of them are positive. It returns `False` otherwise. Several test cases are provided to validate the function's correctness.

## Challenge 3: Consonant Value

### Problem Description:
Given a lowercase string containing only alphabetic characters (no spaces), find the highest value of consonant substrings. Consonants are defined as any letters of the alphabet except for "aeiou." Each consonant is assigned a specific value (a = 1, b = 2, c = 3, ..., z = 26).

### Solution:
A Python function (`solve`) calculates the highest value of consonant substrings within the input string. It first removes vowels from the string and then calculates the value of each consonant substring. The function returns the highest calculated value.

---