def greet():
    gr = """
                                             *** Hello This is a Phone Book Application ***
                        
The Way This Application Works Is That It Lookup Info.
Please Note That Capitalization Is Important!
    """
    print(gr)


def search_meth():
    g = input('Please Enter the Search Method: Phone# or Name? ')
    while g == 'Name' or 'Phone#':
        if g == 'Phone#':
            search_ph()
            break
        elif g == 'Name':
            search_na()
            break
        elif g != 'Name' or 'Phone#':
            print('Sorry That Is incorrect Input')
            search_meth()
            break




def search_ph():
    input_search = 'str'
    i = 0
    while not input_search.isdigit():
        input_search = input('Please Enter The Phone#: ')
        if not input_search.isdigit():
            input_search = input('Wrong Data Type, Please Enter a Phone Number: ')
        else:
            return int(input_search)

    while i <= 6:
        if int(input_search) == phb[i]['Pn#']:
            print('This Number Belongs TO :"' + phb[i]['name'] + '"')
            break
        i += 1
    if i == 7:
        print('Sorry, The Number Is Not Found')


def search_na():
    i = 0
    x = str(input('Please Enter a Name: '))
    while i <= 6:
        if x == phb[i]['name']:
            print(phb[i]['Pn#'])
            break
        i += 1
    if i == 7:
        print('Sorry, The Name Is Not Found')


def again():
    agg = input(print("""
If You Want to Search Again Please Type 'Yes' 
If Not Please Type 'Leave'
"""))
    while agg == 'Yes' or 'Leave':
        if agg == 'Yes':
            print('Ok')
            search_meth()
            again()
            break
        elif agg == 'Leave':
            print('Goodbye')
            quit()
            break
        elif agg != 'Yes' or 'Leave':
            print('Sorry That Is incorrect Input')
            again()
            break


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
again()
