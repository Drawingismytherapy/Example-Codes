def gig_calc(name):
    cont = 'y'
    print(f'Welcome {name}, what gig are you interested in?\n'
          f'For Basic Code enter b\n'
          f'For Complex Code enter c\n'
          f'For Bigger Projects enter p\n')
    gig = input()
    total = 0
    rushed = 0

    while cont == 'y':
        if gig == 'b':
            total += 10
            print(f'You have selected Basic Code\n'
                  f'Base price is $10 with a delivery time of 1 day.\n'
                  f'There are no extras available for this item.\n')
            cont = input('Would you like to add anything else? (y/n)\n')
            if cont == 'y':
                gig = input(f'What gig are you interested in?\n'
                            f'For Basic Code enter b\n'
                            f'For Complex Code enter c\n'
                            f'For Bigger Projects enter p\n')

        if gig == 'c':
            total += 20
            print(f'You have selected Complex Code\n'
                  f'Base price is $20 with a delivery time of 2 days.\n'
                  f'There is an option to rush the order to 1 day for $5.\n')
            print('Would you like to rush the order?\n')
            excont= input()
            if excont == 'y':
                total += 5
                rushed += 1
                print('Your Complex Code order will be rushed!')
            cont = input('Would you like to add anything else? (y/n)\n')
            if cont == 'y':
                gig = input(f'What gig are you interested in?\n'
                            f'For Basic Code enter b\n'
                            f'For Complex Code enter c\n'
                            f'For Bigger Projects enter p\n')

        if gig == 'p':
            total += 35
            print(f'You have selected Bigger Projects\n'
                  f'Base price is $35 with a delivery time of 4 days.\n'
                  f'There is an option to rush the order to 2 days for $5.\n')
            print('Would you like to rush the order?\n')
            excont= input()
            if excont == 'y':
                total += 5
                rushed += 1
                print('Your Bigger Projects order will be rushed!')
            cont = input('Would you like to add anything else? (y/n)\n')
            if cont == 'y':
                gig = input(f'What gig are you interested in?\n'
                            f'For Basic Code enter b\n'
                            f'For Complex Code enter c\n'
                            f'For Bigger Projects enter p\n')

    print(f'Your final total is ${total} with {rushed} rushed order(s)')


name = input('What is your name?\n')
gig_calc(name)