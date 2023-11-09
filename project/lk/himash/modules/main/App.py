# Modules :
# Below contains modules creation and its behavior.
# This calls customer modules / user defined modules.

# import modules.Calculation # Alternative
# import modules.Calculation as Calculation # Alternative
from modules import Calculation

print(Calculation.addition(1,4))
print(Calculation.subtraction(1,4))
print(Calculation.multiply(1,4))