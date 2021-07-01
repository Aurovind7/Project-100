class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def enter_pin(self, pin):
        self.pin = pin
    def check_balance(self):
            print("Your Balance is: 50000")
    def withdrawal(self, amount):
        new_amount = 50000 - amount
        print("You have withdrawn amount "+str(amount)+ ". Your remaining balance is "+str(new_amount))

        
def main():
    card_number = input("Insert your card number: ")
    pin_number = input("Enter a new pin: ")

    new_User = Atm(card_number, pin_number)

    print("Choose your activity: ")
    print("1- Balance Enquiry, 2- Withdrawal")
    activity = int(input("Enter Activity Number: "))
    
    if (activity == 1):
        new_User.check_balance()
    elif (activity == 2):
        amount = int(input("Enter the amount to be withdrawn: "))
        new_User.withdrawal(amount)
    else: 
        print("Enter a valid number")



if __name__ == "__main__":
    main()