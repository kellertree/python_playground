# The line below creates a list of toys.
toy_box = ['gameboy', 'action figure', 'carved stick', 'squirt gun']
# The following statement checks to see if the toy requires electricity or not.
for toy in toy_box:
    if toy == 'gameboy':
        print(f'This {toy} requires electricity.\n')
    elif toy == 'squirt gun':
        print(f'This {toy} requires water.\n')
    else:
        print(f'The {toy} does not require electricity.\n')
print(f'I think I will play with the {toy_box[2]} today.')