original_amount = float(input("Enter the purchase amount: USD "))

payment_method = ''

while payment_method != 'BANK' and payment_method != 'DEBIT' and payment_method != 'CREDIT' and payment_method != 'CASH' and payment_method != 'PIX':

    payment_method = input('''Select method of payment: '
(Bank) - Bank Slip
(Debit) - Debit
(Credit) - Credit
(Cash) - Cash
(PIX) - PIX
Choice: ''').upper()

    if payment_method != 'BANK' and payment_method != 'DEBIT' and payment_method != 'CREDIT' and payment_method != 'CASH' and payment_method != 'PIX':
        print('*******************************************')
        print('Invalid option please enter a valid option!')
        print('*******************************************')
show_discounted_price = True

final_amount = 0
# Bank Slip = 15% and Cash = 15%
if payment_method == 'BANK' or payment_method == 'CASH':
    final_amount = original_amount * 0.85
    
elif payment_method == 'DEBIT' or payment_method == 'PIX':
    final_amount = original_amount * 0.90
    
else:
    
    show_discounted_price = False
    
    wants_installments = input("Do you want to pay in installments? (Y) Yes | (N) No: ").lower()
    
    if  wants_installments == 'n': 
        print(f'Purchase Amount USD {original_amount}')
        
    else:
        num_installments = int(input("Enter the amount of installments: "))
        
        installment_amount = round(original_amount / num_installments, 2)

        print(f'Value installment USD  {installment_amount} - Payments {num_installments} - Total value USD {original_amount}')    
  
     
if show_discounted_price:
    print(f'Value to purchase USD$ {final_amount}')
