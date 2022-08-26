import CoolProp.CoolProp as CP
import time as TM
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def rodaeconta():
    visc = CP.PropsSI('VISCOSITY', 'P', 101325.0, 'T', 293.15, 'WATER')
    #
    inc = 3
    timespan = 10
    count = 0
    for i in range(0,inc):
        TM.sleep(timespan)
        count = count + timespan
    return count