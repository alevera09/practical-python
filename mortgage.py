principal: float = 500000.0
rate:float = 0.05
payment:float = 2684.11
total_paid:float = 0.0
months:int = 0
extra_payment_start_month:float = 61
extra_payment_end_month:float = 108
extra_payment:float = 1000


while principal > 0:
    
    
    
    
    if months+1 > 59:
        if months+1 == 60:
            principal = principal * (1+rate/12) - (payment + extra_payment_start_month)
            total_paid += payment + extra_payment_start_month
            months += 1
                     
        elif months+1 > 60:    
            principal = principal * (1+rate/12) - (payment + extra_payment)
            if principal < 0:
                total_paid -=  payment + extra_payment
                principal = 0
            else:    
                total_paid += extra_payment + payment
            months += 1
                   
    elif months+1 < 60:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        months += 1


    print(f"{months} {total_paid:.2f} {principal:.2f}")