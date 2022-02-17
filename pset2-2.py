def paydebt(balance, annualInterestRate, monthlyPayment, t):
    """input: monthlyPayment is fixed, t for the time to check what's the unpaid balance by month
    output: return the remaining unpaid balance if pay by the monthlypayment
    """
    p = monthlyPayment
    # ub for unpaid balance

    if t == 1:
        ub = balance - p
        return ub * (1 + annualInterestRate/12)
    else:
        ub = paydebt(balance, annualInterestRate, monthlyPayment, t-1) - p
        return ub * (1 + annualInterestRate/12)


p = 10
payoff = balance
while payoff > 0:
    p += 10
    payoff = paydebt(balance, annualInterestRate, p, 12)

print("Lowest Payment: " + str(p))
