import re

def normalize_phone(phone_number):
    phone = re.sub(r"[^\d]", "", phone_number)

    if phone.startswith("380"):
        return "+" + phone

    return "+38" + phone
