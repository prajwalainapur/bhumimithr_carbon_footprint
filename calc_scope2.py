import param as param


def get_factor(ele):
    return getattr(param, ele)

def calculate_electrity(content):
    data = content['electrity']
    print(data)
    sum_per = data['per_solar'] + data['per_coal'] + data['per_wind'] + data['per_gas'] + data['per_hydro'] + data['per_oil'] + data['per_nuclear'] + data['per_biomass'] + data['per_geothermal'] + data['per_others']

    solar_emissions = (data['per_solar'] / sum_per) * data['units_consumed'] * get_factor('Solar')
    coal_emissions = (data['per_coal'] / sum_per) * data['units_consumed'] * get_factor('Coal')
    wind_emissions = (data['per_wind'] / sum_per) * data['units_consumed'] * get_factor('Wind')
    gas_emissions = (data['per_gas'] / sum_per) * data['units_consumed'] * get_factor('Gas')
    hydro_emissions = (data['per_hydro'] / sum_per) * data['units_consumed'] *get_factor('Hydro')
    oil_emissions = (data['per_oil'] / sum_per) * data['units_consumed'] *get_factor('Oil')
    nuclear_emissions = (data['per_nuclear'] / sum_per) * data['units_consumed'] *get_factor('Nuclear')
    biomass_emissions = (data['per_biomass'] / sum_per) * data['units_consumed'] *get_factor('Biomass')
    geothermal_emissions = (data['per_geothermal'] / sum_per) * data['units_consumed'] *get_factor('Geothermal')
    others_emissions = (data['per_others'] / sum_per) * data['units_consumed'] *get_factor('Others')

    total_emissions = solar_emissions + coal_emissions + wind_emissions + gas_emissions + hydro_emissions + oil_emissions + nuclear_emissions + biomass_emissions + geothermal_emissions + others_emissions

    return total_emissions


def calculate_steam(content):
    data = content['steam']
    total_emissions = 0

    for ele in data.keys():
        calc_factor = get_factor(ele)
        total_emissions += data[ele]['boiler_efficiency'] * calc_factor * data[ele]['steam_purchased'] 

    return total_emissions

def calculate_scope2(content):

    electrity = calculate_electrity(content)
    steam = calculate_steam(content)
    scope2_total = electrity + steam 

    part_conversion = (content['weight_per_unit']) / (content['annual_tonnage'] * content['yield_percent'] / 100)

    scope2_part = scope2_total * part_conversion
    print(scope2_part)
    return scope2_part
