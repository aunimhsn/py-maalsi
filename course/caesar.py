import json

def caesar(text:str, offset:int = 1) -> str:
    result = ""
    for char in text:
        # Lowercase
        if char.islower():
            index = ord(char) - ord("a")
            index = (index + offset) % 26
            result += chr(index + ord("a"))
            continue

        # Uppercase
        if char.isupper():
            index = ord(char) - ord("A")
            index = (index + offset) % 26
            result += chr(index + ord("A"))
            continue

        # Others
        result += char
    
    return result

def caesar_decrypt(text:str) -> list[list[str, int]]:
    possibilities = []

    for i in range(1, 27):
        possibilities.append([caesar(text, i), 26 - i])

    return possibilities

message = "Doggs ib pcb kssy-sbr"
with open('./data/possibilities.json', 'w') as f:
    json.dump(caesar_decrypt(message), f, indent=4)