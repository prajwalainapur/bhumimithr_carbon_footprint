import param as param


def get_factor(ele):
    return getattr(param, ele)


def calculate_business_travel(content):
    data = content['business_travel']
    total_emissions = 0

    for ele in data.keys():
        calc_factor = get_factor(ele)
        total_emissions += data[ele]['passenger_distance'] * calc_factor / 100 / 1.6

    return total_emissions

def calculate_commuting(content):
    data = content['commuting']
    total_emissions = 0

    for ele in data.keys():
        calc_factor = get_factor(ele)
        total_emissions += data[ele]['average_daily_distance'] * calc_factor / 100 / 1.6 * data[ele]['no_employees'] * 365

    return total_emissions

def calculate_upstream(content):
    data = content['upstream']
    total_emissions = 0

    for ele in data.keys():
        calc_factor = get_factor(ele)
        total_emissions += data[ele]['ton_kms'] * calc_factor / 100 / 1.6 

    return total_emissions

def calculate_waste(content):
    data = content['waste']
    total_emissions = 0

    # for ele in data.keys():
    return total_emissions

def calculate_scope3(content):

    business_travel = calculate_business_travel(content)
    commuting = calculate_commuting(content)
    upstream = calculate_upstream(content)
    waste = calculate_waste(content)

    scope3_total = business_travel + commuting + upstream + waste

# 'weight_per_unit': 1, 'total_units': 1000, 'annual_tonnage': 100, 'yield_percent': 98,
    part_conversion = (content['weight_per_unit']) / (content['annual_tonnage'] * content['yield_percent'] / 100)

    scope3_part = scope3_total * part_conversion
    print(scope3_part)
    return scope3_part

