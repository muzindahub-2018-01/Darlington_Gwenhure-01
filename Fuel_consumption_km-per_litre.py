import sys

#calculate vehicle fuel consumption
print('Welcome!')

print('This program calculates fuel consumption in km_per_litre')
print('')
print('\n\n')

    
#user to input mileage reading in kms
start_mileage = input('Enter start_mileage: ')
start_mileage = float(start_mileage)
print('')
closing_mileage = input('Enter closing_mileage: ')
closing_mileage = float(closing_mileage)
print('')
    
km_driven = closing_mileage - start_mileage
print('')

#user to input fuel used in litres
litres_used = input('Enter litres used: ')
litres_used = float(litres_used)
print('')

#Calculate fuel consumption
trip_consumption = km_driven / litres_used
print("trip_consumption: ")
print(trip_consumption)
target = 2
print('')

def targeted_consumption(target):
    target = float(2)
    print(target)

targeted_consumption(target)

#inform user of vehicle performance
def restart(done):
    while True:
        
        if trip_consumption < 2:
            print('vehicle consumption is too high than target: ')
            break
        else:
            if trip_consumption > 2:
                print('vehicle is performing well above target: ')
                break

        if done:
            restart = input("Try again? Y/n: ").lower()
            if restart != 'n':
                return restart(done=False)
            else:
                sys.exit()

done = False

restart(done)


    



        



