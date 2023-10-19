from pptx_filler import *
from ai import *

def save_pptx2(company_name, logo_path, ratings, pptx_path):
    general_info = {
        1: company_name,
        3: get_industry_auto(company_name.lower()),
        5: get_location(company_name.lower()),
        7: get_head_count()
    }

    ratings_info = {
        1: ratings['ecovadis'],
        4: ratings['cdp'],
        7: ratings['sustainalytics'],
        10: ratings['msci'],
        13: ratings['dowjones'],
    }

    risks = build_arr_str([
            "Physical risks associated with extreme weather",
            "Main risk here is the kernel oil production and mainly the risks of a low crop yield because of El Nino"
            "Transition risks associated with the transition to low-emission economy and society. This risk mainly steam from a potential increase in costs associated with CO2 emissions"
    ])

    opportunities = build_arr_str([
            "Relaunch shampoo and conditioner brand with more recycled plastic",
            "Has published a 2030+ sustainability ambition framework with where they currently work on improving and have ambitions of improving",
            "Provide a comprehensive sustainability profile for all products by 2025",
            "Reducing material in packaging",
            "Invests in fund for sustainable packaging",
            'Collaborates with “Plastic bank” to reduce plastic waste by developing recycling infrastructure in developing countries',
            "Actively wants to contribute to thriving communities",
            "Expand community education and volunteering programs",
            "Try to engage and empower all employees to be more sustainable",
    ])

    social = build_arr_str([
            "They launched sustainability at heart program to inform and empower employees to support their joint engagement concerning sustainability",
            "Improve livelihood of small farmers and protection of nature",
            "Continuously collaborate with OECD supported global business coalition Business for Inclusive Growth (B4IG)",
            'Has launched the DE&I campaign “I am unique. We are Henkel” and an diversity week that aims to expand the knowledge among workers about diversity, equity and inclusion',
            'Have a LGBTQ+ Network that aims to create a more open work environment and raise awareness about different topics aimed at LGBTQ+',
            'Have ambitions of gender parity across all management levels 2025',
            'Has partnership with ability:IN to accelerate the inclusion of people with disabilities',
            'Encourage lifelong learning to bridge the gap between generations.',
    ])

    governance = build_arr_str([
            "Henkel have an extensive sustainability strategy and a sustainability board that has extensive knowledge in how to move forward with sustainability",
            'The company seem to have a good and correct way of collecting and analyzing data to keep track of different metrics and their sustainability progress, they also show their base year?',
            'Their Carbon Disclosure Project score is A-'
    ])

    env_data = {
        'emission_management': build_arr_str([
                "100% renewable energy to 2030 (currently have 70%)",
                '65% less CO2 emissions 2025 compared to 2015 from operations (currently have -55%)',
                '30% less CO2 emissions 2025 compared to 2015 from raw materials and packaging (currently have -55%)',
                '100 less million ton CO2 in their value-chain 2025 compared to 2016 (currently over 78 million)',
    ]),
        'resources_management': build_arr_str([
                "35% less water consumption per ton of product 2025 compared to 2010 (currently -25%)",
                "100% palm and kernel oil whose responsible sourcing is certified or externally confirmed 2025 (currently 89%)"
    ]),
        'waste_management': build_arr_str([
                'Have ambition of zero plastic waste into nature',
                '30% share of recycled plastic (–50% fossil-based virgin plastics) for all packaging of consumer goods products 2025 (currently 16%)',
                '100% of packaging designed for recycling or reusability 2025 (currently 87%)',
                'Reduce total amount of waste by 50% 2025 compared to 2010',
    ]),
    }

    presentation = Presentation('template.pptx')
    slide = presentation.slides[0]

    fill_logo(slide, logo_path)

    for shape in slide.shapes:
        if shape.name == 'GeneralInfo':
            fill_data(general_info, shape)
        if shape.name == 'Ratings':
            fill_data(ratings_info, shape)
        if shape.name == 'Risks':
            fill_bullet_list_data(risks, shape)
        if shape.name == 'Opportunities':
            fill_bullet_list_data(opportunities, shape)
        if shape.name == 'Social':
            fill_bullet_list_data(social, shape)
        if shape.name == 'Governance':
            fill_bullet_list_data(governance, shape)
        if shape.name == 'Enviromental':
            fill_env_data(env_data, shape.shapes)

    presentation.save(pptx_path)

    return ratings_info

ratings = {
        'ecovadis': get_ratings_ecovadis(),
        'cdp': get_ratings_cdp(),
        'sustainalytics': get_ratings_sustainalytics(),
        'msci': get_ratings_msci(),
        'dowjones': get_ratings_dowjones()
}

save_pptx2('Henkel', '../logos/henkel.png', ratings, 'test.pptx')
