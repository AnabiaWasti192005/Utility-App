items = [
    {
        'code':0,
        'name':'Aquafina Water bottle',
        'price':2 
    },
    {
        'code':1,
        'name':'Galaxy plain bar',
        'price':3.50
    },
    {
        'code':2,
        'name':'Doritos sweet chilli pepper',
        'price':2
    },
    {
        'code':3,
        'name':'Raja chips',
        'price':0.53
    },
    {
        'code':4,
        'name':'Kitkat 4 finger bar',
        'price':2.5000
    },
    {
        'code':5,
        'name':'Sprite can',
        'price':5
    },
    {
        'code':6,
        'name':'Coca-Cola can',
        'price':5
    },
    {
        'code':7,
        'name':'Tiffany chocolate chip cookies',
        'price':1
    },
]

is_quit = False
item = ''

while is_quit == False:
    print("Welcome to Anabia's vending machine")
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")

    query = int(input("Please enter your item's code number here: "))
    for i in items:
        if query == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')
    else:
        print(f"Good!, {item['name']} is for {item['price']} dhs")

        price = int(input(f"Enter {item['price']} dhs to purchase: "))
        if price == item['price']:
            print(f"Thanks for buying here is your {item['name']}")
        else:
            print(f"Please enter only {item['price']} dhs")

    query = input("To quit the machine enter q and to continue buying enter anything: ")
    if query == 'c':
        is_quit = False
    else:
        is_quit = True
    print('')