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

RISKS = [
    "Possible impacts from severe weather events pose physical risks to the company.",
    "The primary concern involves kernel oil production, notably due to El Nino's threat of reduced crop yield.",
    "Transition risks stem from the shift to a low-emission economy, including potential higher costs linked to CO2 emissions.",
    "The company faces risks due to extreme weather conditions, which might impact its operations negatively.",
    "A significant risk area is the production of kernel oil, especially concerning El Nino-induced low crop yield.",
    "Transition risks arise during the company's shift to a low-emission economy, potentially raising CO2-related costs.",
    "Physical risks tied to extreme weather events could adversely affect the company's operations and infrastructure.",
    "Kernel oil production is vulnerable, primarily due to the threat of low crop yield caused by El Nino.",
    "Transition risks emerge during the move towards a low-emission economy, potentially inflating costs linked to CO2 emissions.",
    "The company's exposure to extreme weather events poses physical risks, impacting its assets and supply chains.",
    "Concerns intensify around kernel oil production due to El Nino, increasing the risk of diminished crop yields.",
    "Transition risks materialize as the company navigates towards a low-emission economy, potentially escalating CO2-related expenses.",
    "Extreme weather-related physical risks jeopardize the company's facilities, supply chains, and overall operations.",
    "The vulnerability of kernel oil production heightens due to El Nino, posing a threat to crop yields and profitability.",
    "Transition risks loom large as the company transitions to a low-emission economy, potentially driving up CO2-related costs.",
    "The company faces physical risks due to extreme weather events, jeopardizing its facilities and supply chain resilience.",
    "Kernel oil production's vulnerability is evident during El Nino, posing significant risks to crop yield and profitability.",
    "Transition risks emerge during the company's transition to a low-emission economy, potentially increasing CO2-related expenditures.",
    "Physical risks stemming from extreme weather events challenge the company's operational and supply chain stability.",
    "The susceptibility of kernel oil production increases due to El Nino, heightening risks related to crop yield and financial outcomes.",
    "Transition risks become apparent as the company embraces a low-emission economy, potentially driving up CO2-related costs.",
    "Extreme weather-related physical risks threaten the company's operations, impacting its facilities and supply chain effectiveness.",
    "Kernel oil production's vulnerability escalates with El Nino, intensifying risks associated with crop yield and financial performance.",
    "Transition risks emerge as the company shifts towards a low-emission economy, potentially inflating costs linked to CO2 emissions.",
    "Physical risks arising from extreme weather events challenge the company's operational resilience and supply chain robustness.",
    "Kernel oil production faces heightened vulnerability due to El Nino, increasing risks related to crop yield and economic performance.",
    "Transition risks surface as the company transitions to a low-emission economy, potentially driving up expenses tied to CO2 emissions.",
    "The company grapples with physical risks linked to extreme weather events, impacting its operational continuity and supply chain viability.",
    "The vulnerability of kernel oil production intensifies with El Nino, heightening risks concerning crop yield and financial stability.",
    "Transition risks become evident during the company's shift to a low-emission economy, potentially increasing costs related to CO2 emissions.",
    "Extreme weather-related physical risks challenge the company's operations, affecting its facilities, supply chain, and overall efficiency.",
    "Kernel oil production's vulnerability rises due to El Nino, heightening risks associated with crop yield and overall economic health.",
    "Transition risks manifest as the company transitions to a low-emission economy, potentially inflating costs associated with CO2 emissions.",
    "The company confronts physical risks resulting from extreme weather events, impacting its operational resilience and supply chain effectiveness.",
    "Kernel oil production's vulnerability becomes pronounced with El Nino, escalating risks tied to crop yield and financial performance.",
    "Transition risks become apparent as the company shifts to a low-emission economy, potentially increasing expenses related to CO2 emissions.",
    "Physical risks arising from extreme weather events pose challenges to the company's operations, affecting facilities, supply chain, and overall functioning.",
    "Kernel oil production faces increased vulnerability due to El Nino, heightening risks related to crop yield and overall financial viability.",
    "Transition risks emerge during the company's transition to a low-emission economy, potentially driving up costs associated with CO2 emissions.",
    "The company grapples with physical risks arising from extreme weather events, impacting operational stability, supply chain, and overall efficiency.",
    "The vulnerability of kernel oil production intensifies with El Nino, increasing risks associated with crop yield and overall economic well-being.",
    "Transition risks become evident as the company moves towards a low-emission economy, potentially increasing costs tied to CO2 emissions.",
    "Physical risks stemming from extreme weather events challenge the company's operational continuity, impacting facilities, supply chain, and overall functioning.",
    "Kernel oil production's vulnerability rises significantly due to El Nino, heightening risks related to crop yield and financial performance.",
    "Transition risks manifest during the company's shift to a low-emission economy, potentially inflating costs linked to CO2 emissions.",
    "The company faces physical risks due to extreme weather events, impacting operational resilience, facilities, supply chain, and overall functioning.",
    "Kernel oil production's vulnerability becomes more pronounced with El Nino, escalating risks concerning crop yield and financial stability.",
    "Transition risks become apparent as the company transitions to a low-emission economy, potentially increasing expenses associated with CO2 emissions.",
    "Physical risks associated with extreme weather events pose challenges to the company's operations, affecting facilities, supply chain, and overall efficiency.",
    "The vulnerability of kernel oil production intensifies due to El Nino, heightening risks related to crop yield and overall economic well-being.",
    "Transition risks emerge as the company transitions to a low-emission economy, potentially driving up costs linked to CO2 emissions.",
    "The company confronts physical risks arising from extreme weather events, impacting operational stability, supply chain, facilities, and overall efficiency.",
    "The vulnerability of kernel oil production escalates with El Nino, increasing risks tied to crop yield and financial performance.",
    "Transition risks become evident as the company shifts to a low-emission economy, potentially increasing expenses associated with CO2 emissions.",
    "Physical risks stemming from extreme weather events challenge the company's operational continuity, impacting facilities, supply chain, and overall functioning.",
    "Kernel oil production's vulnerability rises significantly due to El Nino, heightening risks related to crop yield and financial performance.",
    "Transition risks manifest during the company's shift to a low-emission economy, potentially inflating costs linked to CO2 emissions.",
    "The company faces physical risks due to extreme weather events, impacting operational resilience, facilities, supply chain, and overall functioning.",
    "Kernel oil production's vulnerability becomes more pronounced with El Nino, escalating risks concerning crop yield and financial stability.",
    "Transition risks become apparent as the company transitions to a low-emission economy, potentially increasing expenses associated with CO2 emissions.",
    "Physical risks associated with extreme weather events pose challenges to the company's operations, affecting facilities, supply chain, and overall efficiency.",
    "The vulnerability of kernel oil production intensifies due to El Nino, heightening risks related to crop yield and overall economic well-being.",
    "Transition risks emerge as the company transitions to a low-emission economy, potentially driving up costs linked to CO2 emissions.",
    "The company confronts physical risks arising from extreme weather events, impacting operational stability, supply chain, facilities, and overall efficiency.",
    "The vulnerability of kernel oil production escalates with El Nino, increasing risks tied to crop yield and financial performance.",
    "Transition risks become evident as the company shifts to a low-emission economy, potentially increasing expenses associated with CO2 emissions."
]

OPPORTUNITIES = [
    "Revamp shampoo and conditioner line using increased recycled plastic.",
    "Outlined a sustainability vision till 2030, focusing on constant improvements.",
    "Commit to detailing the sustainability profiles of all products by 2025.",
    "Minimize materials in packaging, enhancing eco-friendliness.",
    "Invest in a sustainable packaging fund, supporting eco-friendly solutions.",
    "Partner with 'Plastic bank' to build recycling systems in developing nations.",
    "Eager to boost local communities, actively engaging in their prosperity.",
    "Expand educational initiatives and volunteer programs in communities.",
    "Encourage and empower employees to embrace sustainable practices.",
    "Utilize production heat to warm nearby offices, conserving energy.",
    "Enhance shampoo and conditioner products using more recycled plastic materials.",
    "Outlined a sustainability roadmap for 2030, striving for continuous enhancements.",
    "Commit to delivering detailed sustainability profiles for all products by 2025.",
    "Focus on reducing packaging materials to promote environmental conservation.",
    "Invest in a fund dedicated to sustainable packaging solutions.",
    "Collaborate with 'Plastic bank' to establish recycling systems in developing nations.",
    "Actively contribute to the growth of local communities by supporting various initiatives.",
    "Expand educational outreach and volunteer programs in communities.",
    "Empower employees to embrace sustainable practices and make a positive impact.",
    "Utilize production heat for warming nearby offices, conserving energy resources.",
    "Revitalize shampoo and conditioner products with increased use of recycled plastics.",
    "Established a sustainability vision extending to 2030, focused on ongoing enhancements.",
    "Pledged to provide detailed sustainability profiles for all products by 2025.",
    "Emphasize the reduction of packaging materials to promote environmental preservation.",
    "Allocate resources to a fund supporting innovative and sustainable packaging solutions.",
    "Work closely with 'Plastic bank' to develop recycling infrastructures in developing nations.",
    "Actively engage in initiatives promoting the prosperity of local communities.",
    "Broaden educational outreach and volunteer programs within communities.",
    "Inspire and enable employees to adopt sustainable practices in their daily lives.",
    "Harness production heat to warm nearby offices, promoting energy efficiency.",
    "Upgrade shampoo and conditioner products with higher levels of recycled plastics.",
    "Set forth a sustainability roadmap reaching into 2030, striving for continuous progress.",
    "Pledged to furnish comprehensive sustainability profiles for all products by 2025.",
    "Prioritize the reduction of packaging materials to promote environmental stewardship.",
    "Allocate resources to a fund dedicated to sustainable and innovative packaging solutions.",
    "Collaborate closely with 'Plastic bank' to create recycling infrastructures in developing nations.",
    "Actively participate in initiatives fostering the prosperity of local communities.",
    "Expand educational outreach and volunteer programs within communities.",
    "Empower and inspire employees to adopt sustainable practices in their daily lives.",
    "Utilize production heat to warm nearby offices, contributing to energy conservation.",
    "Reinvent shampoo and conditioner products with an increased focus on recycled plastics.",
    "Established a clear sustainability vision stretching to 2030, emphasizing continual improvement.",
    "Committed to delivering exhaustive sustainability profiles for all products by 2025.",
    "Focus on minimizing packaging materials to support environmental preservation.",
    "Invest in a fund dedicated to cutting-edge, sustainable packaging solutions.",
    "Collaborate closely with 'Plastic bank' to develop recycling infrastructures in underdeveloped nations.",
    "Actively participate in programs enhancing the well-being of local communities.",
    "Expand educational initiatives and volunteer programs within communities.",
    "Motivate employees to embrace sustainable practices in their daily routines.",
    "Optimize the use of production heat for heating nearby offices, conserving energy.",
    "Revitalize shampoo and conditioner products, emphasizing the use of recycled plastics.",
    "Innovate shampoo and conditioner products with a greater focus on recycled plastic usage.",
    "Established a far-reaching sustainability vision extending to 2030, emphasizing constant progress.",
    "Pledged to provide detailed sustainability profiles for all products, a commitment to be met by 2025.",
    "Emphasize the reduction of packaging materials to promote eco-friendly initiatives.",
    "Allocate resources to a dedicated fund supporting cutting-edge, sustainable packaging solutions.",
    "Collaborate closely with 'Plastic bank' to create robust recycling infrastructures in developing nations.",
    "Actively participate in initiatives aimed at enhancing the prosperity of local communities.",
    "Broaden educational outreach and volunteer programs within local communities.",
    "Inspire and empower employees to adopt sustainable practices in their daily lives.",
    "Leverage production heat to warm neighboring offices, promoting energy efficiency.",
    "Redefine shampoo and conditioner products with an intensified focus on incorporating recycled plastics.",
    "Charted a clear path for sustainability, outlining goals that extend to 2030 and beyond.",
    "Committed to providing comprehensive sustainability profiles for all products by 2025.",
    "Focus on minimizing the use of packaging materials, championing environmental conservation.",
    "Invest in a dedicated fund for state-of-the-art, eco-friendly packaging solutions.",
    "Collaborate closely with 'Plastic bank' to construct efficient recycling systems in developing nations.",
    "Actively engage in programs aimed at bolstering the well-being of local communities.",
    "Expand educational initiatives and volunteer programs, fostering community development.",
    "Motivate and enable employees to embrace sustainable practices in their daily routines.",
    "Optimize the utilization of production heat to warm neighboring offices, promoting energy conservation.",
    "Reinvent shampoo and conditioner products, prioritizing the use of recycled plastics.",
    "Forge ahead with a comprehensive sustainability vision, outlining objectives through 2030.",
    "Commit to delivering exhaustive sustainability profiles for all products, slated for completion by 2025.",
    "Emphasize the reduction of packaging materials, advocating for environmental preservation.",
    "Invest in a dedicated fund for innovative, sustainable packaging solutions.",
    "Collaborate closely with 'Plastic bank' to establish efficient recycling infrastructures in developing nations.",
    "Actively participate in initiatives fostering the prosperity of local communities.",
    "Expand educational initiatives and volunteer programs, fostering community engagement.",
    "Inspire and empower employees to embrace sustainable practices in their daily lives.",
    "Harness production heat efficiently, warming nearby offices and promoting energy efficiency.",
    "Redefine shampoo and conditioner products, emphasizing the use of recycled plastics.",
    "Set forth a robust sustainability vision, delineating goals that extend to 2030 and beyond.",
    "Commit to delivering comprehensive sustainability profiles for all products, ensuring completion by 2025.",
    "Prioritize the reduction of packaging materials, championing eco-friendly initiatives.",
    "Invest in a dedicated fund for cutting-edge, sustainable packaging solutions.",
    "Collaborate closely with 'Plastic bank' to develop efficient recycling infrastructures in developing nations.",
    "Actively engage in initiatives aimed at fostering the well-being of local communities.",
    "Expand educational outreach and volunteer programs, promoting community development.",
    "Inspire and enable employees to adopt sustainable practices in their daily routines.",
    "Leverage production heat effectively, warming neighboring offices and enhancing energy efficiency.",
    "Reimagine shampoo and conditioner products, accentuating the use of recycled plastics.",
    "Establish a comprehensive sustainability vision, delineating goals that extend to 2030 and beyond.",
    "Commit to delivering thorough sustainability profiles for all products, ensuring completion by 2025.",
    "Prioritize the reduction of packaging materials, advocating for environmental preservation.",
    "Invest in a dedicated fund for cutting-edge, sustainable packaging solutions.",
    "Collaborate closely with 'Plastic bank' to develop efficient recycling infrastructures in developing nations.",
    "Actively engage in initiatives aimed at fostering the well-being of local communities.",
    "Expand educational outreach and volunteer programs, promoting community development.",
    "Inspire and enable employees to adopt sustainable practices in their daily routines.",
    "Leverage production heat effectively, warming neighboring offices and enhancing energy efficiency."
]

ENV_EMISSION = [
    "Aiming for 100% renewable energy by 2030, currently at 70% utilization.",
    "Targeting a 65% reduction in CO2 emissions from operations by 2025.",
    "Striving for a 30% reduction in CO2 emissions from raw materials and packaging.",
    "Commitment to limit value-chain CO2 to 100 million tons by 2025.",
    "Working towards 100% renewable energy by 2030, currently 70% achieved.",
    "Efforts underway to reduce CO2 emissions from operations by 65% by 2025.",
    "Seeking a 30% decrease in CO2 emissions from raw materials and packaging.",
    "Pursuing a target of 100 million tons for value-chain CO2 by 2025.",
    "Transitioning to 100% renewable energy sources by 2030, currently at 70%.",
    "Aiming for a 65% reduction in CO2 emissions from operations by 2025.",
    "Striving to reduce CO2 emissions from raw materials and packaging by 30%.",
    "Targeting 100 million tons as the limit for value-chain CO2 by 2025.",
    "Committing to 100% renewable energy utilization by 2030, currently 70%.",
    "Aiming for a 65% cut in CO2 emissions from operations by the year 2025.",
    "Working towards a 30% reduction in CO2 emissions from raw materials and packaging.",
    "Targeting a cap of 100 million tons for value-chain CO2 emissions by 2025.",
    "Envisioning 100% renewable energy usage by 2030, with 70% currently achieved.",
    "Striving for a 65% decrease in CO2 emissions from operations by 2025.",
    "Aiming for a 30% reduction in CO2 emissions from raw materials and packaging.",
    "Targeting a maximum of 100 million tons for value-chain CO2 by 2025.",
    "Committing to 100% renewable energy sources by 2030, currently at 70%.",
    "Aiming for a 65% drop in CO2 emissions from operations by 2025.",
    "Working to reduce CO2 emissions from raw materials and packaging by 30%.",
    "Setting a cap of 100 million tons for value-chain CO2 emissions by 2025.",
    "Striving to achieve 100% renewable energy usage by 2030, currently at 70%.",
    "Aiming for a 65% reduction in CO2 emissions from operations by 2025.",
    "Seeking a 30% decrease in CO2 emissions from raw materials and packaging.",
    "Targeting a maximum of 100 million tons for value-chain CO2 by 2025.",
    "Committed to 100% renewable energy sources by 2030, currently at 70%.",
    "Aiming for a 65% reduction in CO2 emissions from operations by 2025.",
    "Working to decrease CO2 emissions from raw materials and packaging by 30%.",
    "Targeting a cap of 100 million tons for value-chain CO2 emissions by 2025.",
    "Striving to achieve 100% renewable energy usage by 2030, currently at 70%.",
    "Aiming for a 65% reduction in CO2 emissions from operations by 2025.",
    "Working towards a 30% decrease in CO2 emissions from raw materials and packaging.",
    "Targeting a maximum of 100 million tons for value-chain CO2 by 2025.",
    "Committing to 100% renewable energy sources by 2030, currently at 70%.",
    "Aiming for a 65% reduction in CO2 emissions from operations by 2025.",
    "Striving for a 30% reduction in CO2 emissions from raw materials and packaging.",
    "Targeting a cap of 100 million tons for value-chain CO2 emissions by 2025.",
    "Committed to achieving 100% renewable energy usage by 2030, currently at 70%.",
    "Aiming for a 65% decrease in CO2 emissions from operations by 2025.",
    "Working towards a 30% reduction in CO2 emissions from raw materials and packaging.",
    "Setting a maximum of 100 million tons for value-chain CO2 by 2025.",
    "Striving for 100% renewable energy usage by 2030, currently at 70%.",
    "Aiming for a 65% reduction in CO2 emissions from operations by 2025.",
    "Working to decrease CO2 emissions from raw materials and packaging by 30%.",
    "Targeting a cap of 100 million tons for value-chain CO2 emissions by 2025.",
    "Committing to 100% renewable energy sources by 2030, currently at 70%.",
    "Aiming for a 65% reduction in CO2 emissions from operations by 2025.",
    "Striving for a 30% reduction in CO2 emissions from raw materials and packaging.",
    "Setting a cap of 100 million tons for value-chain CO2 emissions by 2025.",
    "Committed to 100% renewable energy usage by 2030, currently at 70%.",
    "Aiming for a 65% reduction in CO2 emissions from operations by 2025.",
    "Working towards a 30% decrease in CO2 emissions from raw materials and packaging.",
    "Targeting a maximum of 100 million tons for value-chain CO2 by 2025.",
    "Transitioning to 100% renewable energy usage by 2030, currently at 70%.",
    "Aiming for a 65% decrease in CO2 emissions from operations by 2025.",
    "Working to reduce CO2 emissions from raw materials and packaging by 30%.",
    "Setting a cap of 100 million tons for value-chain CO2 emissions by 2025.",
    "Striving to achieve 100% renewable energy usage by 2030, currently at 70%.",
    "Aiming for a 65% reduction in CO2 emissions from operations by 2025.",
    "Seeking a 30% decrease in CO2 emissions from raw materials and packaging.",
    "Targeting a maximum of 100 million tons for value-chain CO2 by 2025.",
    'Improved traceability of palm-based raw materials by 5% points.', "Renewed the company's contract for renewable energy sources.", 'Optimizing transportation and logistics chains by analyzing carbon emissions.', 'Evaluating carbon footprint of logistics in 18 countries for CO2 reduction.', 'Increasing ocean freight while decreasing reliance on air transportation.', 'Investing in alternative drive trains such as battery and hydrogen power.', 'Expanding digital tools to enhance efficiency in the logistics sector.', 'Achieved 5% points increase in traceability for palm-based materials.', 'Secured renewed renewable energy contract for sustainable operations.', "Analyzing logistics' carbon footprint for further CO2 emissions reduction.", "Assessing carbon emissions to reduce logistics' impact in 18 countries.", 'Transitioning to more ocean freight and reducing reliance on air transport.', 'Exploring battery and hydrogen-powered drive trains for eco-friendly options.', 'Enhancing efficiency in logistics through the expansion of digital tools.', 'Palm-based raw material traceability improved by 5% points.', "Company's renewable energy contract successfully renewed.", "Analyzing logistics' carbon emissions for more eco-friendly practices.", 'Reducing carbon footprint in logistics across 18 operating countries.', 'Shifted focus to ocean freight, minimizing reliance on air transportation.', 'Investing in battery and hydrogen-powered drive trains for sustainability.', 'Increasing logistics efficiency through the adoption of digital tools.', 'Improved traceability rates for palm-based raw materials by 5% points.', 'Renewed contract for renewable energy sources to support sustainability.', "Analyzing logistics' carbon emissions to achieve further reductions.", 'Assessing CO2 impact in logistics across 18 countries for eco-friendly solutions.', 'Transitioning to ocean freight, reducing environmental impact of air transport.', 'Exploring eco-friendly drive trains, including battery and hydrogen-powered ones.', 'Expanding digital tools to optimize logistics and enhance efficiency.', 'Achieved a 5% points increase in palm-based raw material traceability.', "Successfully renewed the company's contract for renewable energy."
]

ENV_RESOURCES = [
    "Targeting a 35% reduction in water use per ton of product by 2025.",
    "Aiming for 100% responsibly sourced palm and kernel oil by 2025.",
    "Working to cut water consumption by 35% per ton of product by 2025.",
    "Striving to achieve 100% certified or externally confirmed palm and kernel oil by 2025.",
    "Pursuing a 35% decrease in water usage per ton of product by 2025.",
    "Committing to sourcing 100% certified or externally confirmed palm and kernel oil by 2025.",
    "Efforts underway to reduce water use by 35% per ton of product by 2025.",
    "Aiming for 100% responsibly sourced palm and kernel oil by the year 2025.",
    "Targeting a 35% reduction in per-ton water consumption by 2025.",
    "Striving to achieve 100% certification or external confirmation for palm and kernel oil by 2025.",
    "Working to cut water use by 35% per ton of product by 2025.",
    "Committing to sourcing 100% certified or externally confirmed palm and kernel oil by 2025.",
    "Pursuing a 35% decrease in water usage per ton of product by 2025.",
    "Aiming for 100% responsibly sourced palm and kernel oil by the year 2025.",
    "Targeting a 35% reduction in per-ton water consumption by 2025.",
    "Striving to achieve 100% certification or external confirmation for palm and kernel oil by 2025.",
    "Efforts underway to reduce water use by 35% per ton of product by 2025.",
    "Committing to sourcing 100% certified or externally confirmed palm and kernel oil by 2025.",
    "Pursuing a 35% decrease in water usage per ton of product by 2025.",
    "Aiming for 100% responsibly sourced palm and kernel oil by the year 2025.",
    "Working to cut water use by 35% per ton of product by 2025.",
    "Striving to achieve 100% certification or external confirmation for palm and kernel oil by 2025.",
    "Efforts underway to reduce water use by 35% per ton of product by 2025.",
    "Committing to sourcing 100% certified or externally confirmed palm and kernel oil by 2025.",
    "Pursuing a 35% decrease in water usage per ton of product by 2025.",
    "Aiming for 100% responsibly sourced palm and kernel oil by the year 2025.",
    "Targeting a 35% reduction in per-ton water consumption by 2025.",
    "Striving to achieve 100% certification or external confirmation for palm and kernel oil by 2025.",
    "Working to cut water use by 35% per ton of product by 2025.",
    "Committing to sourcing 100% certified or externally confirmed palm and kernel oil by 2025.",
    "Pursuing a 35% decrease in water usage per ton of product by 2025.",
    "Aiming for 100% responsibly sourced palm and kernel oil by the year 2025.",
    "Targeting a 35% reduction in per-ton water consumption by 2025.",
    "Striving to achieve 100% certification or external confirmation for palm and kernel oil by 2025.",
    "Efforts underway to reduce water use by 35% per ton of product by 2025.",
    "Committing to sourcing 100% certified or externally confirmed palm and kernel oil by 2025.",
    "Pursuing a 35% decrease in water usage per ton of product by 2025.",
    "Aiming for 100% responsibly sourced palm and kernel oil by the year 2025.",
    "Working to cut water use by 35% per ton of product by 2025.",
    "Striving to achieve 100% certification or external confirmation for palm and kernel oil by 2025.",
    "Efforts underway to reduce water use by 35% per ton of product by 2025.",
    "Committing to sourcing 100% certified or externally confirmed palm and kernel oil by 2025.",
    "Pursuing a 35% decrease in water usage per ton of product by 2025.",
    "Aiming for 100% responsibly sourced palm and kernel oil by the year 2025.",
    "Targeting a 35% reduction in per-ton water consumption by 2025.",
    "Striving to achieve 100% certification or external confirmation for palm and kernel oil by 2025.",
    "Working to cut water use by 35% per ton of product by 2025.",
    "Committing to sourcing 100% certified or externally confirmed palm and kernel oil by 2025.",
    "Pursuing a 35% decrease in water usage per ton of product by 2025.",
    "Aiming for 100% responsibly sourced palm and kernel oil by the year 2025.",
    "Targeting a 35% reduction in per-ton water consumption by 2025.",
    "Striving to achieve 100% certification or external confirmation for palm and kernel oil by 2025.",
    "Efforts underway to reduce water use by 35% per ton of product by 2025.",
    "Committing to sourcing 100% certified or externally confirmed palm and kernel oil by 2025.",
    "Pursuing a 35% decrease in water usage per ton of product by 2025.",
    "Aiming for 100% responsibly sourced palm and kernel oil by the year 2025.",
    'Analyzing carbon emissions in logistics for sustainable CO2 reduction.', 'Reducing environmental impact by optimizing logistics in 18 countries.', 'Shifting to ocean freight, minimizing ecological effects of air transport.', 'Investigating battery and hydrogen-powered drive trains for sustainability.', 'Enhancing logistics efficiency through the expansion of digital solutions.', 'Improved traceability for palm-based raw materials by 5% points.', 'Renewed renewable energy contract to support green initiatives.', "Evaluating logistics' carbon emissions for further CO2 reductions.", 'Assessing CO2 impact in logistics across 18 countries for greener practices.', 'Increasing ocean freight while reducing reliance on air transport.', 'Investigating battery and hydrogen-powered drive trains for sustainable options.', 'Expanding digital tools to optimize logistics and enhance overall efficiency.', 'Achieved 5% points increase in traceability for palm-based materials.', "Successfully renewed company's renewable energy contract.", "Analyzing logistics' carbon emissions for sustainable practices.", 'Reducing carbon footprint in logistics across 18 operating countries.', 'Transitioning to ocean freight, minimizing reliance on air transportation.', 'Exploring battery and hydrogen-powered drive trains for sustainability.', 'Enhancing efficiency in logistics through the expansion of digital tools.', 'Improved traceability rates for palm-based raw materials by 5% points.', 'Successfully renewed contract for renewable energy sources.', "Analyzing logistics' carbon emissions to achieve further reductions.", 'Assessing CO2 impact in logistics across 18 countries for eco-friendly solutions.', 'Transitioning to ocean freight, reducing environmental impact of air transport.', 'Exploring eco-friendly drive trains, including battery and hydrogen-powered ones.', 'Expanding digital tools to optimize logistics and enhance efficiency.', 'Achieved a 5% points increase in palm-based raw material traceability.', "Successfully renewed the company's contract for renewable energy.", 'Analyzing carbon emissions in logistics for sustainable CO2 reduction.', 'Reducing environmental impact by optimizing logistics in 18 countries.'
]

SOCIAL = [
    "Launched 'Sustainability at Heart' program to engage and empower employees.",
    "Enhancing small farmers' lives while preserving nature.",
    "Collaborating consistently with OECD-backed coalition, B4IG.",
    "Introduced 'I am unique. We are diverse' campaign and diversity week.",
    "Established LGBTQ+ Network for openness and awareness at work.",
    "Striving for gender parity across all management levels by 2025.",
    "Partnering with ability:IN to promote disability inclusion.",
    "Promoting lifelong learning to bridge generational divides.",
    "Initiated 'Sustainability at Heart' program to empower employees.",
    "Enhancing lives of small farmers while conserving natural resources.",
    "Partnering with OECD-supported B4IG for global collaboration.",
    "Launched DE&l campaign and diversity week to promote inclusivity.",
    "Established LGBTQ+ Network to foster an inclusive work environment.",
    "Aiming for gender parity across management levels by 2025.",
    "Collaborating with ability:IN for accelerated disability inclusion.",
    "Promoting continuous learning to bridge generational gaps.",
    "Implemented 'Sustainability at Heart' initiative for employee engagement.",
    "Supporting small farmers' livelihoods while preserving ecosystems.",
    "Engaging with OECD-backed B4IG for global collaboration efforts.",
    "Launched DE&l campaign and diversity week to enhance workplace inclusivity.",
    "Established LGBTQ+ Network for a more inclusive work culture.",
    "Striving for gender parity in all management levels by 2025.",
    "Partnership with ability:IN to fast-track disability inclusion.",
    "Fostering lifelong learning to connect different generations.",
    "Inaugurated 'Sustainability at Heart' program for employee empowerment.",
    "Improving small farmers' lives and safeguarding natural habitats.",
    "Collaborating with OECD-endorsed B4IG for global partnerships.",
    "Launched DE&l campaign and diversity week to promote workplace inclusivity.",
    "Established LGBTQ+ Network for a more accepting work atmosphere.",
    "Committed to gender parity in all management tiers by 2025.",
    "Joined forces with ability:IN for accelerated disability inclusion efforts.",
    "Promoting lifelong learning to bridge generational divides.",
    "Unveiled 'Sustainability at Heart' initiative for employee engagement.",
    "Enhancing small farmers' livelihoods while preserving ecosystems.",
    "Consistent collaboration with OECD-backed B4IG for global partnerships.",
    "Introduced DE&l campaign and diversity week to enhance workplace inclusivity.",
    "Established LGBTQ+ Network to foster inclusivity and awareness.",
    "Striving for gender parity at all management levels by 2025.",
    "Partnered with ability:IN to expedite disability inclusion efforts.",
    "Promoting lifelong learning to bridge generational gaps.",
    "Launched 'Sustainability at Heart' initiative to empower employees.",
    "Enhancing the lives of small farmers while preserving natural habitats.",
    "Collaborating with OECD-supported B4IG for global partnership.",
    "Introduced DE&l campaign and diversity week to enhance workplace inclusivity.",
    "Established LGBTQ+ Network for an inclusive and diverse work environment.",
    "Aiming for gender parity across all management levels by 2025.",
    "Partnered with ability:IN to accelerate disability inclusion efforts.",
    "Promoting continuous learning to bridge generational divides.",
    "Implemented 'Sustainability at Heart' program for employee empowerment.",
    "Enhancing small farmers' lives while conserving natural resources.",
    "Engaging with OECD-backed B4IG for global collaboration efforts.",
    "Launched DE&l campaign and diversity week to promote inclusivity at work.",
    "Established LGBTQ+ Network for a more inclusive workplace.",
    "Striving for gender parity in all management levels by 2025.",
    "Collaborating with ability:IN for accelerated disability inclusion efforts.",
    "Promoting lifelong learning to bridge generational gaps.",
    "Inaugurated 'Sustainability at Heart' initiative for employee empowerment.",
    "Improving small farmers' livelihoods and safeguarding natural habitats.",
    "Collaborating with OECD-endorsed B4IG for global partnerships.",
    "Launched DE&l campaign and diversity week to enhance workplace inclusivity.",
    "Established LGBTQ+ Network for a more accepting work atmosphere.",
    "Committed to gender parity in all management tiers by 2025.",
    "Joined forces with ability:IN for accelerated disability inclusion efforts.",
    "Promoting lifelong learning to bridge generational divides.",
    "Unveiled 'Sustainability at Heart' program for employee engagement.",
    "Enhancing small farmers' livelihoods while preserving ecosystems.",
    "Consistent collaboration with OECD-backed B4IG for global partnerships.",
    "Introduced DE&l campaign and diversity week to enhance workplace inclusivity.",
    "Established LGBTQ+ Network to foster inclusivity and awareness.",
    "Striving for gender parity at all management levels by 2025.",
    "Partnered with ability:IN to expedite disability inclusion efforts.",
    "Promoting lifelong learning to bridge generational gaps."
]

GOVERNANCE = [
    "The company boasts a robust sustainability strategy and an expert board dedicated to sustainable advancement.",
    "They excel in meticulous data collection and analysis, tracking various metrics to gauge their sustainability journey.",
    "Their adept approach to data collection ensures accuracy, aiding their tracking of diverse sustainability indicators.",
    "The company demonstrates adeptness in gathering and analyzing data, vital for monitoring their sustainability strides.",
    "A diligent sustainability board and an adept data system facilitate their progress in the sustainability realm.",
    "The company showcases an adeptness in data collection and analysis, essential for tracking diverse sustainability metrics.",
    "Their precise data collection method ensures accuracy, enabling a comprehensive assessment of their sustainability endeavors.",
    "Their comprehensive sustainability strategy, bolstered by expert guidance, steers their sustainable initiatives.",
    "A proficient sustainability board and meticulous data analysis drive their successful sustainability endeavors.",
    "Their careful data analysis supports the tracking of various metrics, pivotal for their sustainability progress.",
    "The company possesses an expert sustainability board, guiding their strategic sustainability initiatives.",
    "Their strategic data collection and analysis empower their efforts in tracking diverse sustainability metrics.",
    "A knowledgeable sustainability board and precise data analysis guide their impactful sustainability measures.",
    "Their adept data analysis method ensures accuracy, enhancing their sustainability monitoring efforts.",
    "Their sustainability strategy, guided by a proficient board, propels their impactful sustainability initiatives.",
    "A knowledgeable board and precise data analysis underpin their meticulous sustainability tracking.",
    "Their expert board and meticulous data analysis bolster their strategic sustainability progress.",
    "Their sustainability strategy, underpinned by a proficient board, drives their impactful sustainability initiatives.",
    "A knowledgeable board and accurate data analysis form the foundation of their meticulous sustainability tracking.",
    "Their adept board and precise data analysis strengthen their strategic sustainability efforts.",
    "Their comprehensive sustainability strategy, coupled with expert guidance, steers their impactful sustainability initiatives.",
    "A proficient board and meticulous data analysis drive their strategic sustainability progress.",
    "Their expert board and meticulous data analysis bolster their impactful sustainability initiatives.",
    "Their strategic sustainability strategy, guided by a proficient board, propels their impactful sustainability initiatives.",
    "A knowledgeable board and precise data analysis underpin their meticulous sustainability tracking.",
    "Their expert board and meticulous data analysis bolster their strategic sustainability efforts.",
    "Their sustainability strategy, underpinned by a proficient board, drives their impactful sustainability initiatives.",
    "A knowledgeable board and accurate data analysis form the foundation of their meticulous sustainability tracking.",
    "Their adept board and precise data analysis strengthen their strategic sustainability efforts.",
    "Their comprehensive sustainability strategy, coupled with expert guidance, steers their impactful sustainability initiatives.",
    "A proficient board and meticulous data analysis drive their strategic sustainability progress.",
    "Their expert board and meticulous data analysis bolster their impactful sustainability initiatives.",
    "Their strategic sustainability strategy, guided by a proficient board, propels their impactful sustainability initiatives.",
    "A knowledgeable board and precise data analysis underpin their meticulous sustainability tracking.",
    "Their expert board and meticulous data analysis bolster their strategic sustainability efforts.",
    "Their sustainability strategy, underpinned by a proficient board, drives their impactful sustainability initiatives.",
    "A knowledgeable board and accurate data analysis form the foundation of their meticulous sustainability tracking.",
    "Their adept board and precise data analysis strengthen their strategic sustainability efforts.",
    "Their comprehensive sustainability strategy, coupled with expert guidance, steers their impactful sustainability initiatives.",
    "A proficient board and meticulous data analysis drive their strategic sustainability progress.",
    "Their expert board and meticulous data analysis bolster their impactful sustainability initiatives.",
    "Their strategic sustainability strategy, guided by a proficient board, propels their impactful sustainability initiatives.",
    "A knowledgeable board and precise data analysis underpin their meticulous sustainability tracking.",
    "Their expert board and meticulous data analysis bolster their strategic sustainability efforts.",
    "Their sustainability strategy, underpinned by a proficient board, drives their impactful sustainability initiatives.",
    "A knowledgeable board and accurate data analysis form the foundation of their meticulous sustainability tracking.",
    "Their adept board and precise data analysis strengthen their strategic sustainability efforts.",
    "Their comprehensive sustainability strategy, coupled with expert guidance, steers their impactful sustainability initiatives.",
    "A proficient board and meticulous data analysis drive their strategic sustainability progress.",
    "Their expert board and meticulous data analysis bolster their impactful sustainability initiatives.",
    "Their strategic sustainability strategy, guided by a proficient board, propels their impactful sustainability initiatives.",
    "A knowledgeable board and precise data analysis underpin their meticulous sustainability tracking.",
    "Their expert board and meticulous data analysis bolster their strategic sustainability efforts.",
    "Their sustainability strategy, underpinned by a proficient board, drives their impactful sustainability initiatives.",
    "A knowledgeable board and accurate data analysis form the foundation of their meticulous sustainability tracking.",
    "Their adept board and precise data analysis strengthen their strategic sustainability efforts.",
    "Their comprehensive sustainability strategy, coupled with expert guidance, steers their impactful sustainability initiatives.",
    "A proficient board and meticulous data analysis drive their strategic sustainability progress.",
    "Their expert board and meticulous data analysis bolster their impactful sustainability initiatives.",
    "Their strategic sustainability strategy, guided by a proficient board, propels their impactful sustainability initiatives.",
    "A knowledgeable board and precise data analysis underpin their meticulous sustainability tracking.",
    "Their expert board and meticulous data analysis bolster their strategic sustainability efforts.",
    "Their sustainability strategy, underpinned by a proficient board, drives their impactful sustainability initiatives.",
    "A knowledgeable board and accurate data analysis form the foundation of their meticulous sustainability tracking.",
    "Their adept board and precise data analysis strengthen their strategic sustainability efforts."
]


ENV_WASTE = [
    "Strive for zero plastic waste in natural environments, setting an ambitious goal.",
    "Target 30% recycled plastic, cutting fossil-based virgin plastics by 50% in consumer goods packaging by 2025, up from the current 16%.",
    "Aim to make all packaging 100% recyclable or reusable by 2025, building on our current 87% rate.",
    "Pledge to halve total waste by 2025 compared to 2010, showcasing our enduring commitment to sustainability.",
    "Work tirelessly to eradicate plastic pollution from nature, setting a challenging objective.",
    "Plan to increase recycled plastic to 30%, reducing fossil-based virgin plastics by 50% in consumer goods packaging by 2025, from the current 16%.",
    "Commit to ensuring all packaging is 100% recyclable or reusable by 2025, enhancing our current 87% rate.",
    "Strategize to decrease total waste by 50% by 2025, a substantial reduction from 2010 levels.",
    "Strive for a future with no plastic waste in nature, setting a high aspiration.",
    "Aim for 30% recycled plastic, cutting fossil-based virgin plastics by 50% in consumer goods packaging by 2025, up from the current 16%.",
    "Dedicate efforts to make all packaging 100% recyclable or reusable by 2025, building on our current 87% rate.",
    "Pledge to halve total waste by 50% by 2025 compared to 2010, demonstrating our strong commitment to sustainability.",
    "Focus on eliminating plastic pollution from nature, setting an ambitious target.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for zero plastic waste in nature, setting a challenging goal.",
    "Target 30% recycled plastic, reducing fossil-based virgin plastics by 50% in consumer goods packaging by 2025, from the current 16%.",
    "Dedicate efforts to achieve 100% recyclable or reusable packaging by 2025, building on our current 87% rate.",
    "Pledge to cut total waste by 50% by 2025 compared to 2010, showcasing our enduring commitment to sustainability.",
    "Focus on eradicating plastic pollution from nature, setting a high aspiration.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for a future with no plastic waste in nature, setting a high aspiration.",
    "Target 30% recycled plastic, cutting fossil-based virgin plastics by 50% in consumer goods packaging by 2025, up from the current 16%.",
    "Dedicate efforts to make all packaging 100% recyclable or reusable by 2025, building on our current 87% rate.",
    "Pledge to halve total waste by 50% by 2025 compared to 2010, demonstrating our strong commitment to sustainability.",
    "Focus on eliminating plastic pollution from nature, setting an ambitious target.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for zero plastic waste in nature, setting a challenging goal.",
    "Target 30% recycled plastic, reducing fossil-based virgin plastics by 50% in consumer goods packaging by 2025, from the current 16%.",
    "Dedicate efforts to achieve 100% recyclable or reusable packaging by 2025, building on our current 87% rate.",
    "Pledge to cut total waste by 50% by 2025 compared to 2010, showcasing our enduring commitment to sustainability.",
    "Focus on eradicating plastic pollution from nature, setting a high aspiration.",
    "Strive for 100% recyclable or reusable packaging by 2025, enhancing our current 87% rate.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for a future with no plastic waste in nature, setting a high aspiration.",
    "Target 30% recycled plastic, cutting fossil-based virgin plastics by 50% in consumer goods packaging by 2025, up from the current 16%.",
    "Dedicate efforts to make all packaging 100% recyclable or reusable by 2025, building on our current 87% rate.",
    "Pledge to halve total waste by 50% by 2025 compared to 2010, demonstrating our strong commitment to sustainability.",
    "Focus on eliminating plastic pollution from nature, setting an ambitious target.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for zero plastic waste in nature, setting a challenging goal.",
    "Target 30% recycled plastic, reducing fossil-based virgin plastics by 50% in consumer goods packaging by 2025, from the current 16%.",
    "Dedicate efforts to achieve 100% recyclable or reusable packaging by 2025, building on our current 87% rate.",
    "Pledge to cut total waste by 50% by 2025 compared to 2010, showcasing our enduring commitment to sustainability.",
    "Focus on eradicating plastic pollution from nature, setting a high aspiration.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for a future with no plastic waste in nature, setting a high aspiration.",
    "Target 30% recycled plastic, cutting fossil-based virgin plastics by 50% in consumer goods packaging by 2025, up from the current 16%.",
    "Dedicate efforts to make all packaging 100% recyclable or reusable by 2025, building on our current 87% rate.",
    "Pledge to halve total waste by 50% by 2025 compared to 2010, demonstrating our strong commitment to sustainability.",
    "Focus on eliminating plastic pollution from nature, setting an ambitious target.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for zero plastic waste in natural habitats, setting an ambitious objective.",
    "Target 30% recycled plastic, reducing fossil-based virgin plastics by 50% in consumer goods packaging by 2025, up from the current 16%.",
    "Dedicate efforts to ensure all packaging is 100% recyclable or reusable by 2025, building on our current 87% rate.",
    "Pledge to halve total waste by 50% by 2025 compared to 2010, demonstrating our unwavering commitment to sustainability.",
    "Focus on eradicating plastic pollution from natural ecosystems, setting a challenging goal.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for a future with no plastic waste in natural environments, setting a high aspiration.",
    "Target 30% recycled plastic, cutting fossil-based virgin plastics by 50% in consumer goods packaging by 2025, up from the current 16%.",
    "Dedicate efforts to make all packaging 100% recyclable or reusable by 2025, building on our current 87% rate.",
    "Pledge to halve total waste by 50% by 2025 compared to 2010, demonstrating our strong commitment to sustainability.",
    "Focus on eliminating plastic pollution from natural habitats, setting an ambitious target.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for zero plastic waste in nature, setting a challenging goal.",
    "Target 30% recycled plastic, reducing fossil-based virgin plastics by 50% in consumer goods packaging by 2025, from the current 16%.",
    "Dedicate efforts to achieve 100% recyclable or reusable packaging by 2025, building on our current 87% rate.",
    "Pledge to cut total waste by 50% by 2025 compared to 2010, showcasing our enduring commitment to sustainability.",
    "Focus on eradicating plastic pollution from natural ecosystems, setting a high aspiration.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for a future with no plastic waste in nature, setting a high aspiration.",
    "Target 30% recycled plastic, cutting fossil-based virgin plastics by 50% in consumer goods packaging by 2025, up from the current 16%.",
    "Dedicate efforts to make all packaging 100% recyclable or reusable by 2025, building on our current 87% rate.",
    "Pledge to halve total waste by 50% by 2025 compared to 2010, demonstrating our strong commitment to sustainability.",
    "Focus on eliminating plastic pollution from nature, setting an ambitious target.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for zero plastic waste in nature, setting a challenging goal.",
    "Target 30% recycled plastic, reducing fossil-based virgin plastics by 50% in consumer goods packaging by 2025, from the current 16%.",
    "Dedicate efforts to achieve 100% recyclable or reusable packaging by 2025, building on our current 87% rate.",
    "Pledge to cut total waste by 50% by 2025 compared to 2010, showcasing our enduring commitment to sustainability.",
    "Focus on eradicating plastic pollution from nature, setting a high aspiration.",
    "Strive for 100% recyclable or reusable packaging by 2025, enhancing our current 87% rate.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for a future with no plastic waste in nature, setting a high aspiration.",
    "Target 30% recycled plastic, cutting fossil-based virgin plastics by 50% in consumer goods packaging by 2025, up from the current 16%.",
    "Dedicate efforts to make all packaging 100% recyclable or reusable by 2025, building on our current 87% rate.",
    "Pledge to halve total waste by 50% by 2025 compared to 2010, demonstrating our strong commitment to sustainability.",
    "Focus on eliminating plastic pollution from nature, setting an ambitious target.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    "Aim for zero plastic waste in nature, setting a challenging goal.",
    "Target 30% recycled plastic, reducing fossil-based virgin plastics by 50% in consumer goods packaging by 2025, from the current 16%.",
    "Dedicate efforts to achieve 100% recyclable or reusable packaging by 2025, building on our current 87% rate.",
    "Pledge to cut total waste by 50% by 2025 compared to 2010, showcasing our enduring commitment to sustainability.",
    "Focus on eradicating plastic pollution from nature, setting a high aspiration.",
    "Commit to reducing total waste by 50% by 2025 compared to 2010 levels, emphasizing our dedication to sustainability.",
    'Shifting to ocean freight, minimizing ecological effects of air transport.', 'Investigating battery and hydrogen-powered drive trains for sustainability.', 'Enhancing logistics efficiency through the expansion of digital solutions.', 'Improved traceability for palm-based raw materials by 5% points.', 'Renewed renewable energy contract to support green initiatives.', "Evaluating logistics' carbon emissions for further CO2 reductions.", 'Assessing CO2 impact in logistics across 18 countries for greener practices.', 'Increasing ocean freight while reducing reliance on air transport.', 'Investigating battery and hydrogen-powered drive trains for sustainable options.', 'Expanding digital tools to optimize logistics and enhance overall efficiency.', 'Achieved 5% points increase in traceability for palm-based materials.', "Successfully renewed company's renewable energy contract.", "Analyzing logistics' carbon emissions for sustainable practices.", 'Reducing carbon footprint in logistics across 18 operating countries.', 'Transitioning to ocean freight, minimizing reliance on air transportation.', 'Exploring battery and hydrogen-powered drive trains for sustainability.', 'Enhancing efficiency in logistics through the expansion of digital tools.', 'Improved traceability rates for palm-based raw materials by 5% points.', 'Successfully renewed contract for renewable energy sources.', "Analyzing logistics' carbon emissions to achieve further reductions.", 'Assessing CO2 impact in logistics across 18 countries for eco-friendly solutions.', 'Transitioning to ocean freight, reducing environmental impact of air transport.', 'Exploring eco-friendly drive trains, including battery and hydrogen-powered ones.', 'Expanding digital tools to optimize logistics and enhance efficiency.', 'Achieved a 5% points increase in palm-based raw material traceability.', "Successfully renewed the company's contract for renewable energy.", 'Analyzing carbon emissions in logistics for sustainable CO2 reduction.', 'Reducing environmental impact by optimizing logistics in 18 countries.', 'Shifting to ocean freight, minimizing ecological effects of air transport.', 'Investigating battery and hydrogen-powered drive trains for sustainability.', 'Enhancing logistics efficiency through the expansion of digital solutions.'
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

    if company_name == "henkel":
        return "Chemical"
    elif company_name in ["apple", "amazon"]:
        return "Tech"
    elif company_name in ["mcdonalds"]:
        return "Food"
    elif company_name in ["volkswagen"]:
        return "Automotive"
    elif company_name in ["aldi"]:
        return "Retail"
    else:
        return "N/A"


def get_industry():
    return random.choice(INDUSTRIES)


def get_timestamp():
    timestamp = int(time.time())
    return str(timestamp)


def get_location(company_name):
    if company_name == "henkel":
        return "Duesseldorf"
    elif company_name == "apple":
        return "Cupertino"
    elif company_name == "mcdonalds":
        return "Chicago"
    elif company_name == "amazon":
        return "Seattle"
    elif company_name == "aldi":
        return "Essen"
    elif company_name == "volkswagen":
        return "Wolfsburg"
    else:
        return "-"

def get_head_count():
    return f'{random.randrange(12, 500)}000'


def build_arr_str(arr):
    arr[0] = "- " + arr[0]

    return '\n- '.join(arr)


def generate_risks():
    risks = random.sample(RISKS, 3)

    return build_arr_str(risks)


def generate_opportunities():
    opportunities = random.sample(OPPORTUNITIES, 7)

    return build_arr_str(opportunities)


def generate_social():
    social = random.sample(SOCIAL, 10)

    return build_arr_str(social)


def generate_governance():
    governance = random.sample(GOVERNANCE, 7)

    return build_arr_str(governance)


def generate_env_general():
    general = random.sample(ENV_GENERAL, 5)

    return build_arr_str(general)


def generate_env_emission():
    emission = random.sample(ENV_EMISSION, 6)

    return build_arr_str(emission)


def generate_env_resources():
    resources = random.sample(ENV_RESOURCES, 5)

    return build_arr_str(resources)


def generate_env_waste():
    waste = random.sample(ENV_WASTE, 4)

    return build_arr_str(waste)
