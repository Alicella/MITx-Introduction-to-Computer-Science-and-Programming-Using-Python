def paydebt(balance, annualInterestRate, monthlyPaymentRate, t):
    """input: b for the original balance, air for annual interest rate, mpr for monthly payment rate, 
           t for the time to check what's the unpaid balance by month
    output: return the remaining unpaid balance if only pays the minimum monthly payment 
            required by the credit card company each month.
    """
    # ub for unpaid balance, p for monthly payment

    if t == 1:
        p = balance * monthlyPaymentRate
        ub = balance - p
        return ub * (1 + annualInterestRate/12)
    else:
        p = paydebt(balance, annualInterestRate,
                    monthlyPaymentRate, t-1) * monthlyPaymentRate
        ub = paydebt(balance, annualInterestRate, monthlyPaymentRate, t-1) - p
        return ub * (1 + annualInterestRate/12)


remain_balance = paydebt(42, 0.2, 0.04, 12)
print(round(remain_balance, 2))
