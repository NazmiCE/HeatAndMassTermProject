from dotenv import load_dotenv
import os 
from constants import *
from scipy import integrate

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# CP Functions with respect to temperature # 0.2 acetic acid, 0.8 water
acetic_acid_cp = lambda T:  ACETIC_ACID_CP_CONSTANTS[0] + ACETIC_ACID_CP_CONSTANTS[1]*T + ACETIC_ACID_CP_CONSTANTS[2]*T**2 + ACETIC_ACID_CP_CONSTANTS[3]*T**3
water_cp = lambda T:  WATER_CP_CONSTANTS[0] + WATER_CP_CONSTANTS[1]*T + WATER_CP_CONSTANTS[2]*T**2 + WATER_CP_CONSTANTS[3]*T**3
general_cp_of_solution = lambda T : 0.2 * acetic_acid_cp(T)/MOLAR_WEIGHT_OF_ACETIC_ACID * 1000 + 0.8 * water_cp(T)/ MOLAR_WEIGHT_OF_WATER * 1000 # Return J/kgK

# Calculating Q Required
func_to_integral = lambda T : FLOW_RATE*general_cp_of_solution(T)

Q = (-integrate.quad(func_to_integral, 373, 323)[0])/3600 # Result is stored in the first index 
print(Q) # J/s

