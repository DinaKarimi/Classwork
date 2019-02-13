print('How many bottles are you recycling?')
bottles = int(input())
print('How many litres do the containers hold?')
litres= float(input())
if litres==1 or litres<1 :
    print(f'{bottles*0.10}$')
elif litres>1:
        print(f'{bottles*0.25}$')
