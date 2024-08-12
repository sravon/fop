import random
coin = ['heads', 'trails']
heads =0 
tails = 0
trails = 1000
print('\n COIN TOSS\n')
for index in range(trails):
    if random.choice(coin) == 'heads':
        heads = heads + 1
    else:
        tails = tails + 1
print('\nThere were ', heads, ' heads & ', tails, ' tails.\n')
