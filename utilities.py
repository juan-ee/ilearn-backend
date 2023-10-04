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


def get_industry():
    return random.choice(INDUSTRIES)


def get_timestamp():
    timestamp = int(time.time())
    return str(timestamp)
