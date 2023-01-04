from constants import *
from scipy import integrate
import math

def log_mean_temp(Tic : float, Tih : float, Toc : float, Toh : float, countercurrent = True) -> float:
    """
    Tic : Inlet Cold Fluid
    Tih : Inlet Hot Fluid
    Toc : Outlet Cold Fluid
    Toh : Outlet Hot Fluid
    countercurrent : Flow direction with respect to each other if True(default) countercurrent 
    if false cocurrent flow

    This function takes the logarithmic mean between inlet streams and outlet streams
    """
    if countercurrent == True:
        return ((Tih-Toc)-(Toh - Tic))/ math.log((Tih-Toc)/(Toh - Tic)) 
    else:
        return ((Tih-Tic)-(Toh - Toc))/ math.log((Tih-Tic)/(Toh - Toc)) 

def correlation_name(*args) -> float:
    # TODO
    # Change the function name with a suitable one
    # Implement the behaviour
    # return <h>
    # Change *args with appropriate values for the correlation 
    pass



def calculate_total_area(number_of_plates: int, area_of_plates: float) -> float:
    """
    number_of_plates : Number of plates
    area_of_plates: Area of one plate that is used

    return: total_area
    """
    # return total_area
    # Calculate the total area for our design
    # If there is some other parameters like thickness include them as well  
    return number_of_plates * area_of_plates

def calculate_friction_coefficient(*args) -> float:
    """
    return: friction factor f
    """
    # TODO
    # Replace *args with related parameters
    # Use an appropriate correlation
    # return f friction factor
    pass


def calculate_pressure_drop(*args)-> float:
    # TODO
    # Replace *args with required parameters
    # Use an appropriate form of pressure drop equation
    # return pressure drop  
    pass




def main():
    filee = open("Design_Results.txt", 'w')


    # Check this by hand calculation
    # Created lambda functions in a form of A + BT + CT^2 + DT^3 for acetic acid and water
    # And a general cp for solution by including their mass ratios (before the units are corrected by multiplying with 1000/MOLAR_WEIGHT_X)
    # CP Functions with respect to temperature # 0.3 acetic acid, 0.7 water
    acetic_acid_cp = lambda T:  ACETIC_ACID_CP_CONSTANTS[0] + ACETIC_ACID_CP_CONSTANTS[1]*T + ACETIC_ACID_CP_CONSTANTS[2]*T**2 + ACETIC_ACID_CP_CONSTANTS[3]*T**3 # J/molK
    water_cp = lambda T:  WATER_CP_CONSTANTS[0] + WATER_CP_CONSTANTS[1]*T + WATER_CP_CONSTANTS[2]*T**2 + WATER_CP_CONSTANTS[3]*T**3 # J/molK
    general_cp_of_solution = lambda T : (0.3 * acetic_acid_cp(T)*1000/MOLAR_WEIGHT_OF_ACETIC_ACID) + (0.7 * water_cp(T)*1000/ MOLAR_WEIGHT_OF_WATER) # Return J/kgK

    # Calculating Q Required
    # m' indicated flow rate
    func_to_integral = lambda T : FLOW_RATE*general_cp_of_solution(T) # m'CpdT
    Q = round((-integrate.quad(func_to_integral, 373, 323)[0])/3600,2) # Result is stored in the first index 
    #


    filee.write(f"Heat Transfer: {str(Q)} J\n")
    filee.close()


if __name__ == "__main__":
    main()
    
