print("{{ NEWLY INVENTED ATM WITH HIGH SECURITY }}".center(120,' '))
user           = 'ramakrishna'
password       = 'Rk2451655@'
pin            = '7678'
users          = input('enter the user name : ')
amount         = 300000
if user == users: 
    passwords      = input('enter the password  : ')
    if password == passwords:
        pins       = input('enter pin           : ')
        if pin == pins:
            print('''{{You can perform these operations here}}
                         1.deposite
                         2.withdraw
                         3.check_balance
                         4.pin_change
                         5.statement
                         6.exit
                    ''')
           
            option = int(input('select one option from above : '))
            if option   == 1:
                deposit =  int(input('enter the amount you want to deposite : '))
                amount  += deposit
                print('Deposited successfully .....')
                print('Total balance : ',amount,'.rs')
            if option  == 2:
                withdrew   =  int(input('enter the amount you want to withdraw : '))
                if amount  >= withdrew:
                    amount = amount - withdrew
                    print(withdrew,'.rs amount withdraw successfully......')
                    print('Total balance : ',amount,'.rs')
                else:
                    print('not enough balance in your account ')
            if option  ==  3:
                pin_s  =   input('enter the pin : ')
                if pin ==  pin_s:
                    print('Your Total Balance is :- ',amount,'.rs')
                else:
                    print('Invalid Pin')
            if option  == 4:
                old_pin=input('enter old pin : ')
                if pin == old_pin:
                    new_pin = input('enter new pin : ')
                    if pin == new_pin:
                        print('pin already exist go for different pin')
                        new_pin = input('enter new pin : ')
                    confirm_pin = input('enter again to confirm new pin : ')
                    print('pin changed sucessfully')
                else:
                    print('entered Invalid pin')
            if option == 5:
                pin_  =   input('enter pin : ')
                email           = 'ramakrishna@gmail.com'
                if pin ==  pin_:
                    print('username      : ',user)
                    print('email         : ',email)
                    print('credited      : ',amount)
                    print('debited       : ',amount)
                    print('Final Balance : ',amount)
                else:
                    print('Invalid Pin')
            if option == 6:
                print('exit successfully')
        else:
            print('Invalid Pin')
    else:
        print('invalid password')
else:
    print('Invalid username')
                
            
            
        
                
        
        
       
        
                
                
                
            
        
    
    
