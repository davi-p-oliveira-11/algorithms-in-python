'''
9) Create an algorithm that reads how much money a person has in their wallet
 (in R$) and shows how many dollars they can buy. Consider US$1.00 = R$3.45.
'''

availableBRL = float(input('Enter a value in BRL: ' ))
valueUSD = availableBRL / 3.45

print(f'You can buy a total of {valueUSD:.2f} USD')
