import gc
import IntDLList as Dll


x = Dll.IntDLList()
while True:
    while True:
        try:
            print('\nOptions:')
            print('1: Append to list')
            print('2: Prepend to list')
            print('3: Remove node from list')
            print('4: Print list')
            print('5: Exit')
            z = int(input('What would you like to do?: '))
            if 0 < z < 6:
                break
            else:
                print('Invalid Input. Please enter either 1, 2, 3, 4, or 5!')
        except ValueError:
            print('Invalid Input. Please enter either 1, 2, 3, 4, or 5!')
    if z == 1:
        while True:
            try:
                z = int(input('\nWhat value would you like to append?: '))
                x.append(z)
                break
            except ValueError:
                print('Invalid Input. Please enter an integer!')
    elif z == 2:
        while True:
            try:
                z = int(input('\nWhat value would you like to prepend?: '))
                x.prepend(z)
                break
            except ValueError:
                print('Invalid Input. Please enter an integer!')
    elif z == 3:
        while True:
            try:
                z = int(input('\nWhat value would you like to remove?: '))
                x.remove(z)
                break
            except ValueError:
                print('Invalid Input. Please enter an integer!')
    elif z == 4:
        if not x.is_empty():
            print(end='\nList: ')
        x.print_list()
    else:
        print('Exiting program...')
        break

#gc.collect()
