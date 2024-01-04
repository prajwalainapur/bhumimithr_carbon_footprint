import param as param

def calculate_emissions(content):

    print(content)
    truck_age = content['truck_age']
    penaly_factor_age = 1.1 if truck_age == '>20 Years' else(1.05 if truck_age == '10-20 Years' else 1)

    truck_size = content['truck_size']
    penaly_factor_size = 1.1 if truck_age == '>5 tonnes' else(1.05 if truck_age == '3.5-5 tonnes' else 1)

    total_emissions_kg = param.truck_perkm * content['distance'] * 1000
    adjusted_emissions_kg = total_emissions_kg * penaly_factor_age * penaly_factor_size

    no_trips = content['load_weight'] / (content['total_units'] * content['weight_per_unit'])

    nett_emissions = adjusted_emissions_kg * no_trips

    emissions_perpart = nett_emissions / content['total_units'] 
    print(emissions_perpart)
    return emissions_perpart