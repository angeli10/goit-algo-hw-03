from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return "Неправильний формат дати. Використайте формат 'РРРР-ММ-ДД'"
    
    today = datetime.today().date()
    difference = today.toordinal() - date.toordinal()
    return difference

m = get_days_from_today('2025-10-09')
print(m)
     