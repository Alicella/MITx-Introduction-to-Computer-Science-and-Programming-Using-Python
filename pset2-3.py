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


balance = 999999
annualInterestRate = 0.18

lower = balance/12
upper = balance*((1+annualInterestRate/12)**12)/12

while True:
    p = (lower + upper)/2
    payoff = paydebt(balance, annualInterestRate, p, 12)

    if round(payoff) == 0:
        p = round(p, 2)
        break
    elif payoff > 0:
        lower = p
    else:
        upper = p


print("Lowest Payment: " + str(p))
