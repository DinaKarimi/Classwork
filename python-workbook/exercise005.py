num_small= int(input('small bottles:'))
num_large= int(input('large battles:'))

refund_small= num_small* 0.10
refund_large= num_large*0.25
refund_total= refund_large+refund_small

print(f'your total refund is:{refund_total}')
