import re

for _ in range(int(input())):
    card_number = input().strip()
    
    structure_pattern = r"^[456](?:\d{15}|\d{3}(?:-\d{4}){3})$"
    
    if re.match(structure_pattern, card_number):
        clean_number = card_number.replace("-", "")
        
        if re.search(r"(\d)\1{3}", clean_number):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")
