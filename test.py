import requests

#Testing Transport
response = requests.get('http://127.0.0.1:5000/transport', json = {'distance': 1000, 'truck_age': '<10 Years', 'truck_size': '>5 tonnes', 
                                                                   'load_weight': 1000, 'weight_per_unit': 1, 'annual_tonnage': 100, 'yield_percent': 98, 
                                                                   'total_units': 1000})

response = requests.get('http://127.0.0.1:5000/scope3', json = {'weight_per_unit': 1, 'total_units': 1000, 'annual_tonnage': 100, 'yield_percent': 98,
                                                                'business_travel': {'passenger_car': {'passenger_distance': 2000}, 
                                                                                    'suv': {'passenger_distance': 1000}},
                                                                'commuting': {'passenger_car': {'average_daily_distance': 10, 'no_employees': 10},
                                                                              'motorcycle': {'average_daily_distance': 5, 'no_employees': 50}},
                                                                'upstream': {'truck': {'ton_kms': 10000}}})

response = requests.get('http://127.0.0.1:5000/scope2', json = {'electrity': {'units_consumed': 100, 'per_solar': 25, 'per_coal': 25, 'per_wind': 25, 
                                                                              'per_gas': 25, 'per_hydro': 0, 'per_oil': 0, 'per_nuclear': 0, 'per_biomass':0,
                                                                              'per_geothermal': 0, 'per_others': 0}, 
                                                                'steam': {'natural_gas': {'boiler_efficiency': 87, 'source_area': 'NA', 'steam_purchased': 100}, 
                                                                          'lpg': {'boiler_efficiency': 45, 'source_area': 'NA', 'steam_purchased': 100}}, 
                                                                          'weight_per_unit': 1, 'total_units': 1000, 'annual_tonnage': 100, 'yield_percent': 98})

response = requests.get('http://127.0.0.1:5000/scope1', json = {'stationary_combustion': {'coal_anthracite':{'quantity': 10, 'source_area': ''}, 
                                                                                          'coal_lignite': {'quantity': 10, 'source_area': ''}, 
                                                                                          'lpg': {'quantity': 10, 'source_area': ''}}, 
                                                                'mobile_combustion': {'passenger_car_diesel': {'on_road': {'year': 2019, 'distance': 10, 'fuel_usage': 1}}, 
                                                                                      'passenger_gas_gasonline': {'off_road': {'year': 2019, 'distance': 10, 'fuel_usage': 1}}, 
                                                                                      'light_duty_truck_cng': {'on_road': {'year': 2019, 'distance': 10, 'fuel_usage': 1}}},
                                                                'refridgeration': {'domestic_refridgeration': {'new_units': 50, 'operating_units': 100, 'disposed_units': 10}, 
                                                                                   'chillers': {'new_units': 50, 'operating_units': 100, 'disposed_units': 10}},
                                                                'fire_supression': {'co2': {'units_consumed': 10}, 'hfc_23': {'units_consumed': 12}}, 
                                                                'purchased_gases': {'co2': {'units_consumed': 10}, 'hfc_23': {'units_consumed': 12}}, 
                                                                          'weight_per_unit': 1, 'total_units': 1000, 'annual_tonnage': 100, 'yield_percent': 98})


print(response.content)

'''
{'weight_per_unit': 1, 'total_units': 1000, 'business_travel': {'passenger_car': {'passenger_distance': 2000}, 'suv': {'passenger_distance': 1000}}}
'''

{'data': 2.6, 'is_renewable': 'Yes'}