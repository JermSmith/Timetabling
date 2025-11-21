from enum import Enum

class PrintStyle(Enum):
    Raw = 0,
    NewLine = 1

def to_int(string):
    original_string = string
    
    if string is int:
        return string
    
    if string is not str:
        string = str(string)
    
    string = string.replace("\ufeff", "")
    string = string.strip()
    
    if string == "":
        return 0
    
    try:
        return int(string)
    except Exception as e:
        print(f"Error converting {original_string} to int: {e}")
