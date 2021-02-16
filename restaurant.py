def restaurant():


    menu = {'egusi': 150, 
    'akpu': 150, 
    'onugbu': 200, 
    'okro': 150, 
    'garri': 150, 
    'nsala': 300, 
    'rice': 150, 
    'stew': 150, 
    'isiewu': 1000
    }
    total = 0

    print()
    while True:
        order = input("Order: ").strip().lower()
        if not order:
            break
        
        if order in menu:
            total += menu[order]
            print(f'{order} cost {menu[order]}, total is {total}')
        else:
            print(f'Sorry, we are fresh out of {order} today.')

    print(f'Your total is {total}')
    return total




def main():
    restaurant()
    print()


main()