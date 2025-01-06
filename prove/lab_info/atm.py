for i in range(3):
    pin = int(input("inserire PIN: "))

    if pin == 1234:
        print("PIN corretto")
        break
    else:
        print("PIN errato")
        
    if i == 2:
        print("carta bloccata")