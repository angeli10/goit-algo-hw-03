import re


def normalize_phone(phone_number):
    formated_number = re.sub(r'[^\d+]', '', phone_number)
    
    if formated_number.startswith('+38'):
        return formated_number
    elif formated_number.startswith('38'):
        return "+" + formated_number
    elif formated_number.startswith('0'):
        return "+38" + formated_number


n = normalize_phone("    khg(05--$0)123-32-34   ")
print(n)