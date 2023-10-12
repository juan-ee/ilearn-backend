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

RATINGS_ECOVADIS = [
    "Platinum",
    "Gold",
    "Silver",
    "Bronze",
]

RATINGS_MSCI = [
    "AAA",
    "AA",
    "A",
    "BBB",
    "BB",
    "B",
    "CCC",
]

RATINGS_DOWJONES = [
    "AAA",
    "AA+",
    "AA",
    "AA-",
    "A+",
    "A",
    "A-",
    "BBB+",
    "BBB",
    "BBB-",
    "BB+",
    "BB",
    "BB-",
    "B+",
    "B",
    "B-",
    "CCC+",
    "CCC",
    "CCC-",
    "CC",
    "C",
    "D",
]

RATINGS_SUSTAINALYTICS = [
    "A+",
    "A",
    "A-",
    "B+",
    "B",
    "B-",
    "C+",
    "C",
    "C-",
    "D+",
    "D",
    "D-",
]


RATINGS_CDP = [
    "A",
    "A-",
    "B",
    "B-",
    "C",
    "C-",
    "D",
    "D-",
]

def get_ratings_cdp():
    return random.choice(RATINGS_CDP)


def get_ratings_sustainalytics():
    return random.choice(RATINGS_SUSTAINALYTICS)

def get_ratings_dowjones():
    return random.choice(RATINGS_DOWJONES)

def get_ratings_msci():
    return random.choice(RATINGS_MSCI)


def get_ratings_ecovadis():
    return random.choice(RATINGS_ECOVADIS)

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
