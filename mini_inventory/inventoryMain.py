from primaryClass import Inventory

############## main function
def main():
    inv = Inventory()

    while True:
        action = input('Actions: add,remove,list, save, exit: ')
        if action == 'exit':
            break
        if action == 'add' or action == 'remove':
            key = input('Enter an animal name: ')
            qty = int(input('Enter the qty: '))
            if action == 'add':
                inv.add(key,qty)
            if action == 'remove':
                inv.remove(key,qty)
        if action == 'list':
            inv.dispaly()
        if action == 'save':
            inv.save()
        
    inv.save()

if __name__ == '__main__':
    main()