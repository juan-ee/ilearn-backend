import random
import time

INDUSTRIES = [
    "Agriculture",
    "Automotive",
    "Banking",
    "Biotechnology",
    "Chemical",
    "Construction",
    "Consulting",
    "Consumer Goods",
    "Education",
    "Energy",
    "Entertainment",
    "Environmental",
    "Fashion",
    "Finance",
    "Food and Beverage",
    "Government",
    "Healthcare",
    "Hospitality",
    "Information Technology",
    "Insurance",
    "Manufacturing",
    "Media",
    "Mining",
    "Non-profit",
    "Pharmaceutical",
    "Real Estate",
    "Retail",
    "Telecommunications",
    "Transportation",
    "Utilities",
]

INDUSTRIES_AUTO = [
    "Chemical",
    "Tech",
    "Food",
]


def get_industry_auto(company_name):
    industry = ""

    if company_name == "Henkel":
        industry = INDUSTRIES_AUTO[0]
    elif company_name == "Apple":
        industry = INDUSTRIES_AUTO[1]
    elif company_name == "Mcdonalds":
        industry = INDUSTRIES_AUTO[2]
    else:
        industry = "N/A"

    return industry


def get_industry():
    return random.choice(INDUSTRIES)


def get_timestamp():
    timestamp = int(time.time())
    return str(timestamp)
