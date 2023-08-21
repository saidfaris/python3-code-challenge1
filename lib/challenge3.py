import re

def solve(word):
    consonant_values = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
    
    substrings = re.split("[aeiou]+", word)
    
    max_value = 0
    
    for substring in substrings:
        value = sum(consonant_values[c] for c in substring)
        
        max_value = max(max_value, value)
    
    return max_value

print(solve("zodiacs"))   
print(solve("strength"))  
