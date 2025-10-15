from datetime import datetime

s = input("Введіть дату у форматі РРРР-ММ-ДД: ")

def get_days_from_today(date: str) -> int:

    try:
        target = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        
        delta = today - target
        print(delta.days)
        return delta.days
  
    except ValueError:
        print("Неправильний формат. Використовуйте формат YYYY-MM-DD")
        return None

get_days_from_today (s)