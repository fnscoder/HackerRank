"""
    Day 2: Operators
    Challenge https://www.hackerrank.com/challenges/30-operators
    Given the meal price (base cost of a meal), tip percent (the percentage 
    of the meal price being added as tip), and tax percent (the percentage 
    of the meal price being added as tax) for a meal, find and print the 
    meal's total cost.
    @fnscoder
"""

mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

totalCost = round(mealCost + mealCost*tipPercent/100 + mealCost*taxPercent/100)

print('The total meal cost is %s dollars.' %str(totalCost))