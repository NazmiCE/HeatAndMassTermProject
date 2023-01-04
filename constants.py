from dotenv import load_dotenv
import os 

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# STATING INITIAL VARIABLES FROM ENVIRONMENT
# Flow Related Parameters
FLOW_RATE = float(os.environ.get('FLOW_RATE'))
T_HOT_IN = float(os.environ.get('T_HOT_IN'))
T_HOT_OUT = float(os.environ.get('T_HOT_OUT'))
T_COLD_IN = float(os.environ.get('T_COLD_IN'))
T_COLD_MAX = float(os.environ.get('T_HOT_IN'))
MAX_PRESSURE_DROP = float(os.environ.get('MAX_PRESSURE_DROP'))

# Design Parameters
MAX_NUMBER_OF_PLATES = int(os.environ.get('MAX_NUMBER_OF_PLATES'))
PORT_SIZE = float(os.environ.get('PORT_SIZE'))
PLATE_THICKNESS_MIN = float(os.environ.get('PLATE_THICKNESS_MIN'))
PLATE_THICKNESS_MAX = float(os.environ.get('PLATE_THICKNESS_MAX'))
PLATE_SPACING_MIN = float(os.environ.get('PLATE_SPACING_MIN'))
PLATE_SPACING_MAX = float(os.environ.get('PLATE_SPACING_MAX'))

# Molecular Weights of Components
MOLAR_WEIGHT_OF_WATER = 18.02 # g/mol
MOLAR_WEIGHT_OF_ACETIC_ACID = 60.052 # g/mol

# Physical Properties of Fluids
# Cp constants in the form of [A,B,C,D] -> A + BT + CT^2 + DT^3
# Cp's unit is J/molK
ACETIC_ACID_CP_CONSTANTS = [-18.944, 1.0971, -2.8921e-3, 2.9275e-6] # Valid Between 291 - 533
WATER_CP_CONSTANTS = [92.053, -3.9953e-02, -2.1103e-04, 5.3469e-07] # Valid Between 273 - 615

# Individual Flow Rates
WATER_FLOW_RATE = FLOW_RATE * 0.8 # kg/hr
ACETIC_ACID_FLOW_RATE = FLOW_RATE * 0.2 # kg/hr

# Cooling Water Parameters at 30+273 = 303
COOLING_SPESIFIC_HEAT= 4178.4 # J/kgK
COOLING_DENSITY = 995.82 #kg/m^3
COOLING_VISCOSITY = 0.8034 * 10**(-3) # Pas
COOLING_THERMAL_CONDUCTIVITY = 0.6172 # W/mK
PRANDT_NUMBER = round(COOLING_VISCOSITY*COOLING_SPESIFIC_HEAT/COOLING_THERMAL_CONDUCTIVITY,2)
