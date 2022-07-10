def greet():
    gr = """
                                             *** Hello This is a Phone Book Application ***
                        
The Way This Application Works Is That It Lookup Info.
    """
    print(gr)


def search_meth():
    g = input('Please Enter the Search Method: Phone# or Name?')
    while g == 'Name' or 'Phone#':
        if g == 'Phone#':
            search_ph()
        elif g == 'Name':
            search_na()
            break



def search_ph():
    i = 0
    x = int(input('Please Enter The Phone#: '))
    while i <= 6:
        if x == phb[i]['Pn#']:
            print(phb[i]['name'])
        i += 1


def search_na():
    i = 0
    x = str(input('Please Enter a Name: '))
    while i <= 6:
        if x == phb[i]['name']:
            print(phb[i]['Pn#'])
        i += 1


phb = [

    {'name': 'Amal', 'Pn#': 1111111111},
    {'name': 'Mohammed', 'Pn#': 2222222222},
    {'name': 'Khadijah', 'Pn#': 3333333333},
    {'name': 'Abdullah', 'Pn#': 4444444444},
    {'name': 'Rawan', 'Pn#': 5555555555},
    {'name': 'Faisal', 'Pn#': 6666666666},
    {'name': 'Layla', 'Pn#': 7777777777}

]

greet()
search_meth()
