'''
 12) Create a program that reads the price of a product,
 calculates, and displays its PROMOTIONAL PRICE with a 5% discount.
'''

product_price = float(input('Enter the price of the product: ' ))

discount = product_price * 0.05
final_price = product_price - discount

print(f'The original price of the product is {product_price}')
print(f'The price with discount is {final_price}')
