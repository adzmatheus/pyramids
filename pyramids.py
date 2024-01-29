print ("\n Normal Pyramid")
for i in range(5):
    x = '* '
    x = x*i
    print(f'{x: ^10}')

print ("\n Inverse Pyramid \n")
for i in range(5):
    x = '* '
    x = x*(5-i)
    print(f'{x: ^10}')

print ("\n Left Pyramid")
for i in range(5):
    x = '* '
    x = x*i
    print(f'{x: <10}')

print ("\n Right Pyramid")
for i in range(5):
    x = '* '
    x = x*i
    print(f'{x: >10}')
