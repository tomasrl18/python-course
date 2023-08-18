# and, or, not

gas = True
ignition = False

if gas and ignition:
    print('Go')
else:
    print('No entró al and')

if gas or ignition:
    print('Go')
else:
    print('No entró al or')

if gas or not ignition:
    print('Go')
else:
    print('No entró al not')