"""
19. Korzystając ze słownika, utwórz funkcję, która będzie zwracać liczbę dni danego miesiąca w roku
"""


def day_month(month):
    months = {'styczeń': '31','luty': '29','marzec': '31','kwiecień': '30','maj': '31','czerwiec': '30','lipiec': '31','siepień': '31','wrzesień': '30','październik': '31','listopad': '30','grudzień': '31'}
    month = month.strip().lower()
    if month not in months.keys():
        print('Zła nazwa miesiaca') 
    else: 
        print(months[month])


day_month('styczeń')