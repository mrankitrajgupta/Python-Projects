def show_balance():
    print(f'\nYour balance is ${balance:.2f}')


def deposit():
    amount = (input('Enter an amount to be deposited: $'))

    try: 
        amount = float(amount)
        if amount > 0:
            return amount        
        else:
            print("You can't entere negative amount")
            return 0
    except:
        print('Please enter a valid amount')
        return 0
   

def withdraw():
    amount = (input('Enter amount to be withdrawn: $'))

    try:
        amount = float(amount)  
        if balance >= amount:
            return amount
        else:
            print("Insufficient funds")
            return 0
    except:
        print('Please enter a valid amount')
        return 0


def main():
    global balance
    global is_running
    balance = 0
    is_running = True
    while is_running:
        print('\n----------Banking Program----------')
        print('1.Show Balance')
        print('2.Deposite')
        print('3.Withdraw')
        print('4.Exit')

        choice = input('Enter your choice (1-4): ')
        if choice == '1':
            show_balance()
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw()
        elif choice == '4':
            is_running = False
        else:
            print('Invalid choice, please enter a valid choice')

    print('Thank you! Have a nice day')


if __name__ == '__main__':
    main()