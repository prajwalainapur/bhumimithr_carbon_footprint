import param as param


def get_factor(ele):
    return getattr(param, ele)

def calculate_stationary_combustion(content):
    data = content['stationary_combustion']
    total_emissions = 0

    for ele in data.keys():
        calc_factor = get_factor(ele)
        total_emissions += data[ele]['quantity'] * calc_factor 

    return total_emissions

def calculate_mobile_combustion(content):###
    data = content['mobile_combustion']
    total_emissions = 0

    for ele in data.keys():
        calc_factor = get_factor(ele)
        total_emissions += data[ele]['on_road']['distance'] * calc_factor[0] + data[ele]['on_road']['fuel_usage'] * calc_factor[1]

    return total_emissions

def calculate_refrigeration(content):
    data = content['refrigeration']
    total_emissions = 0

    for ele in data.keys():
        calc_factor = get_factor(ele)
        total_emissions += ((data[ele]['new_units'] / 100) + (data[ele]['operating_units'] / 50) + (data[ele]['disposed_units'] / 4)) * calc_factor 

    return total_emissions

def calculate_fire_suppression(content):
    data = content['fire_suppression']
    total_emissions = 0

    for ele in data.keys():
        calc_factor = get_factor(ele)
        total_emissions += data[ele]['units_consumed'] * calc_factor * 0.025
    return total_emissions

def calculate_purchased_gases(content):
    data = content['purchased_gases']
    total_emissions = 0

    for ele in data.keys():
        calc_factor = get_factor(ele)
        total_emissions += data[ele]['units_consumed'] * calc_factor
    return total_emissions



def calculate_scope1(content):

    stationary_combustion = calculate_stationary_combustion(content)
    mobile_combustion = calculate_mobile_combustion(content)
    refrigeration = calculate_refrigeration(content)
    fire_suppression = calculate_fire_suppression(content)
    purchased_gases = calculate_purchased_gases(content)

    scope1_total = stationary_combustion + mobile_combustion + refrigeration + fire_suppression + purchased_gases

    part_conversion = (content['weight_per_unit']) / (content['annual_tonnage'] * content['yield_percent'] / 100)

    scope1_part = scope1_total * part_conversion

    return scope1_part
