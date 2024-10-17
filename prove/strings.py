number = int(input("select a number: "))

if number == 1:
    animal = 'cat'
    vegetable = 'carrot'
    mineral = 'aurum'
    print('animal, vegetable and mineral: \n' +
          animal, ' ', vegetable, ' ', mineral)
elif number == 2:
    text = input("write a text: ")
    print("you wrote: ", text)
elif number == 3:
    cat_says = input("what say the cat? ")
    text_len = len(cat_says)
    print('        {}'.format('_' * text_len))
    print('      < {} >'.format(cat_says))
    print('        {}'.format('-' * text_len))
    print("      /")
    print("     /")
    print("/\_/\ ")
    print("(o.o)")
    print(">   <")