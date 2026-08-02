OPERATING_HOURS = 8000          

STEAM_COST = 15.0               
COOLING_WATER_COST = 0.50       

GCAL_TO_GJ = 4.184



def annual_utility_cost(condenser_duty, reboiler_duty):

    condenser = abs(condenser_duty)
    reboiler = abs(reboiler_duty)

    condenser_GJ = condenser * GCAL_TO_GJ
    reboiler_GJ = reboiler * GCAL_TO_GJ

    cooling_cost = (
        condenser_GJ *
        COOLING_WATER_COST *
        OPERATING_HOURS
    )

    steam_cost = (
        reboiler_GJ *
        STEAM_COST *
        OPERATING_HOURS
    )

    total_cost = cooling_cost + steam_cost

    return total_cost


def total_energy(condenser_duty, reboiler_duty):


    return abs(condenser_duty) + abs(reboiler_duty)