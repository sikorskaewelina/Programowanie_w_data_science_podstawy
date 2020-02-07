"""
16. Utwórz funkcję własną, która jako argument przyjmować będzie listę argumentów i wartości,
a jako wynik będzie wyświetlać sformatowany wykres (stosowny zakres, opis, kolory, legenda)
"""


import matplotlib.pyplot as plt


def create_bar_chart(data, labels):
    num_bars = len(data)
    positions = range(1, num_bars+1)
    plt.barh(positions, data, align='center')
    plt.yticks(positions, labels)
    plt.xlabel('Amount')
    plt.ylabel('Category')
    plt.title('Weekly expenditures')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    try:
        data = int(input('Podaj ilość kategorii: '))
        category = []
        amount = []
        for i in range(1, data + 1):
            labels = str(input('Podaj kategorię: '))
            category.append(labels)
            a = float(input('Podaj kwotę: '))
            amount.append(a)
    except ValueError:
        print('Podałeś złą wartość')
    else:
        create_bar_chart(amount, category)