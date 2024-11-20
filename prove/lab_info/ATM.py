pin = 1234

for i in range(3):
    user_pin = int(input("inserire PIN: "))
    
    if user_pin==pin:
        print("PIN corretto")
        break
    elif user_pin!=pin:
        if i<2:
            print("PIN errato, riprova")
        else:
            print("carta bloccata")