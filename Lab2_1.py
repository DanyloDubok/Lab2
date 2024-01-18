#!/usr/bin/env python3

"""Calculate deposit percent yield based on time period.

Imagine your friend wants to put money on a deposit.
He has got many offers from different banks:
- First bank declares +A% each day;
- Second bank promises +B% each month;
- Third bank offers +C% by the end of the year;
- The 4th bank promotes +D% in a 10-year term;
- ... and so on ...

Your friend gets a terrible headache calculating all this stuff,
and asks you to help checking everything. You quickly realize
it is a common task and having a simple script is a great idea.

Let's implement this.

A simplified task:
Given the SUM amount of money, and PERCENT yield promised in a
FIXED_PERIOD of time, calculate the TOTAL equivalent of money
in a SET_PERIOD of time.

Math formula:
p = PERCENT / 100
TOTAL = SUM * ((1 + p) ** (SET_PERIOD / FIXED_PERIOD))
"""


def calculate_yield(initial_sum, percent, fixed_period, set_period):
    """Calculate deposit yield."""
    per = percent / 100
    growth = (1 + per) ** (set_period / fixed_period)
    return initial_sum * growth


def calculate_common_periods(initial_sum, percent, fixed_period):
    """Calculate yields for common periods of time."""
    one_month_yield = calculate_yield(initial_sum, percent, fixed_period, 1)
    one_year_yield = calculate_yield(initial_sum, percent, fixed_period, 12)
    five_years_yield = calculate_yield(initial_sum, percent, fixed_period, 60)
    ten_years_yield = calculate_yield(initial_sum, percent, fixed_period, 120)

    return one_month_yield, one_year_yield, five_years_yield, ten_years_yield


USAGE = """USAGE: {script} initial_sum percent fixed_period set_period

\tCalculate deposit yield. See script source for more details.
"""
USAGE = USAGE.strip()


def main(args):
    """Gets called when run as a script."""
    if len(args) != 4 + 1:
        exit(USAGE.format(script=args[0]))

    args = args[1:]
    initial_sum, percent, fixed_period, set_period = map(float, args)

    total_yield = calculate_yield(initial_sum, percent, fixed_period, set_period)
    formatted_yield = "{:.2f}".format(total_yield)
    print(f"Total equivalent after {set_period} time period: {formatted_yield}")

    # Calculate and print yields for common periods
    one_month_yield, one_year_yield, five_years_yield, ten_years_yield = calculate_common_periods(
        initial_sum, percent, fixed_period
    )
    formatted_one_month_yield = "{:.2f}".format(one_month_yield)
    formatted_one_year_yield = "{:.2f}".format(one_year_yield)
    formatted_five_years_yield = "{:.2f}".format(five_years_yield)
    formatted_ten_years_yield = "{:.2f}".format(ten_years_yield)

    print(f"1-Month Yield: {formatted_one_month_yield}")
    print(f"1-Year Yield: {formatted_one_year_yield}")
    print(f"5-Year Yield: {formatted_five_years_yield}")
    print(f"10-Year Yield: {formatted_ten_years_yield}")


if __name__ == '__main__':
    import sys

    main(sys.argv)
# master
