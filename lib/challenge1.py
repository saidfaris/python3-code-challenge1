# Challenge 1: 12-hour to 24-hour time conversion
def convert(string):
    if string[-2:] == "AM" and string[:2] == "12":
        return "00" + string[2:-2]
    elif string[-2:] == "AM":
        return string[:-2]
    elif string[-2:] == "PM" and string[:2] == "12":
        return string[:-2]
    else:
        return str(int(string[:2]) + 12) + string[2:8]

# Test for Challenge 1
time = "08:30:42PM"
print("12-hour Format time:", time)
print("24-hour Format time:", convert(time))