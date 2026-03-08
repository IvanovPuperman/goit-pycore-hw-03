import re

def normalize_phone(phone_number):
    phone = re.sub(r"[^\d]", "", phone_number)

    if phone.startswith("380"):
        return "+" + phone

    return "+38" + phone

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567"
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print(sanitized_numbers)
