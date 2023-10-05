
# This code for turning on/off AC with input 'on' or off
def turn_on_or_off_ac(input):
    print()
    if input.lower() == 'on':
        print('The Air Conditioner is turned on!') 
    elif input.lower() == 'off':
        print('The Air Condition is turned off!')
    else:
        print('The input is wrong. Please make a proper input!')
    print()



turn_on_or_off_ac('oFf')