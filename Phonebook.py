gr = """
                                             *** Hello This is a Phone Book Application ***

The Way This Application Works Is That It Lookup Info.
Please Note That Capitalization Is Important!
    """
print(gr)


def greet():
    start = input("""
    Search in The Phonebook Enter 'Search'
    Add New Member Info. Enter 'Add'
        """)
    while start == 'Search' or 'Add':
        if start == 'Add':
            add()
            break
        elif start == 'Search':
            search_meth()
            break
        else:
            print('Sorry That Is incorrect Input')
            greet()
            break


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
    input_search = input('Please Enter a Phone#: ')
    i = 0
    while not input_search.isdigit() or len(input_search) != 10:
        input_search = input('This Is Invalid Number, Please Enter a Correct Phone Number: ')
        if input_search.isdigit():
            continue
        elif len(input_search) == 10:
            break
    while i <= 6:
        if int(input_search) == phb[i]['Pn#']:
            print('This Number Belongs TO :"' + phb[i]['name'] + '"')
            break
        i += 1
    if i == len(phb):
        print('Sorry, The Number Is Not Found')


def search_na():
    i = 0
    x = str(input('Please Enter a Name: '))
    while i <= len(phb):
        if x == phb[i]['name']:
            print(phb[i]['Pn#'])
            break
        i += 1
    if i == len(phb):
        print('Sorry, The Name Is Not Found')


def add():
    new_name = input('Please Enter The Name: ')
    new_phone = input('Please Enter Thw Phone# :')
    while not new_phone.isdigit() or len(new_phone) != 10:
        new_phone = input('This Is Invalid Number, Please Enter a Correct Phone Number: ')
        if new_phone.isdigit():
            continue
        elif len(new_phone) == 10:
            break
    new_dic = {'name': new_name, 'Pn#': new_phone}
    phb.append(new_dic)


def again():
    agg = input("""
If You Want To Search Again Please Type 'Yes' 
If Not Please Type 'Leave'
""")
    while agg == 'Yes' or 'Leave':
        if agg == 'Yes':
            print('Ok')
            greet()
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
again()
