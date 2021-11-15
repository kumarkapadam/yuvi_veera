"""
ATM money transfer
pinno
amount
10,000
Amount: System Issue


pin_no = int(input("enter your pin"))

if pin_no == 1234:
    print("**** pin match *****")
    balance = 10000
    print("balance is    :", balance)
    if balance > 1000:
        print("allow withdraw")
    else:
        print("  insufficient funds ")

    while True:
        print('press    1.check your balance')
        print('press    2.Deposit ')
        print('press    3.Withdraw ')
        print('press    4.pin change')
        print('press    4.exit')
        choose = int(input("enter your choice"))

        if choose == 1:
            print("******  check balance ******")
            print("current balance   :", balance)

        elif choose == 2:
            print(" ***** Deposit *****")
            deposit = int(input("enter deposit money"))
            balance += deposit
            print("****  after deposit *****")
            print("current balance   :", balance)

        elif choose == 3:
            print(" *****  withdraw ***** ")
            print("your current balance is :",balance)
            withdraw = int(input("enter how much money do you want:"))
            balance -= withdraw
            balance = abs(balance)
            print("current balence :", balance)
            break
        else:
            print("******  exit ********")
            print("*****  thank you ****")

else:
    print(" you enter wrong pin ")
    print(" try again ")

"""

"""
Blocks to handle the exception
===============================    
try*      : Code which causes the exception
except*   : to handle exception occurred in try block
else
finally


try:
    x = int(input("enter x value:"))
    y = int(input("enter y value:"))
    z = x / y
    print("the value z :", z)

except:
    print("EXCEPTION ::: please enter denominator other than zero ")

try:
    x = int(input("enter x value:"))
    y = int(input("enter y value:"))
    z = x / y
    print("the value z :", z)

except ValueError as ve:
    print("please enter integers  ")

except Exception as e:
    print("exception is there")

# compile_time error

try:
    x=10
    if x == 10
        print("both are same")
except Exception as e:
    print("error occurred ",type(e))
finally:
    print("------end the program----")


"""