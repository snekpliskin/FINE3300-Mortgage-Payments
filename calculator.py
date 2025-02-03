
# make a function to calculate pva
def calculate_pva(r,n):
    if r == 0:
        return n # formula says when the interest rate is 0, PVA will equal n
    return (1 - (1 + r) ** -n) / r

# make a function to calculate mortgage; answering Q#1
def mortgage_payments(principal, rate, amortization):
    """
    principal = principal loan amount
    rate = quoted interest rate (as a decimal)
    amortization = loan term in years
    """
# calculate number of periods
    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52

# calculate period interest rates
    r_monthly = (1 + rate / 2) ** (2 / 12) - 1
    r_semi_monthly = (1 + rate / 2) ** (2 / 24) - 1
    r_bi_weekly = (1 + rate / 2) ** (2 / 26) - 1
    r_weekly = (1 + rate / 2) ** (2 / 52) - 1

# calculate present value of annuity for each case using pairs of above r and n
    pva_monthly = calculate_pva(r_monthly, n_monthly)
    pva_semi_monthly = calculate_pva(r_semi_monthly, n_semi_monthly)
    pva_bi_weekly = calculate_pva(r_bi_weekly, n_bi_weekly)
    pva_weekly = calculate_pva(r_weekly, n_weekly)

# calculate the payments
    monthly_payment = principal / pva_monthly
    semi_monthly_payment = principal / pva_semi_monthly
    bi_weekly_payment = principal / pva_bi_weekly
    weekly_payment = principal / pva_weekly

    # accelerate both bi-weekly and weekly payments using monthly payment
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4

# output the results rounded to two decimal places; answering Q#3
    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print(f"Semi-monthly Payment: ${semi_monthly_payment:.2f}")
    print(f"Bi-weekly Payment: ${bi_weekly_payment:.2f}")
    print(f"Weekly Payment: ${weekly_payment:.2f}")
    print(f"Rapid Bi-weekly Payment: ${rapid_bi_weekly_payment:.2f}")
    print(f"Rapid Weekly Payment: ${rapid_weekly_payment:.2f}")

# promt the users for input values; answering Q#2
principal = float(input("Enter the loan principal amount: $"))
rate = float(input("Enter the quoted interest rate (as a decimal): "))
amortization = int(input("Enter the loan term in years: "))

# calculate and print the PVA; run calculator
mortgage_payments(principal, rate, amortization)








