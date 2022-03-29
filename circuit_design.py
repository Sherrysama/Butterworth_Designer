import schemdraw as schem
import schemdraw.elements as elm
import math
import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal

# 电路图绘制
# order = 1,3,5时考虑过A_0<1的情况，但在最终成果中未考虑，故将相应代码注视掉
def circuit(order, A_0):
    
    if order==1 and A_0>=1:
        cir_1_1 = schem.Drawing()
        op_1_1 = cir_1_1.add(elm.Opamp(leads=True))
        cir_1_1.add(elm.Line().up().at(op_1_1.in1).length(1.5).dot())
        cir_1_1.push()
        cir_1_1.add(elm.Resistor().left().label('$R_3$'))
        cir_1_1.add(elm.Ground())
        cir_1_1.pop()
        cir_1_1.add(elm.Resistor().tox(op_1_1.out).label('$R_2$'))
        cir_1_1.add(elm.Line().toy(op_1_1.out).dot())
        cir_1_1.add(elm.Line().right().at(op_1_1.out).length(1.0).label('$V_{out}$', loc='right'))
        cir_1_1.add(elm.Resistor().left().at(op_1_1.in2).label('$R_1$'))
        cir_1_1.add(elm.Line().left().length(0.5).label('$V_{in}$', loc='left'))
        cir_1_1.add(elm.Dot().at(op_1_1.in2))
        cir_1_1.add(elm.Capacitor().down().label('$C_1$'))
        cir_1_1.add(elm.Ground())
        return cir_1_1
    '''
    if order==1 and A_0<1:
        cir_1_2 = schem.Drawing()
        op_1_2 = cir_1_2.add(elm.Opamp(leads=True))
        cir_1_2.add(elm.Ground().at(op_1_2.in2))
        cir_1_2.add(elm.Dot().at(op_1_2.in1))
        cir_1_2.add(elm.Resistor().left().label('$R_1$'))
        cir_1_2.add(elm.Line().left().length(0.1).label('$V_{in}$', loc='left'))
        cir_1_2.add(elm.Line().at(op_1_2.in1).up().length(1.5))
        cir_1_2.add(elm.Dot())
        cir_1_2.push()
        cir_1_2.add(elm.Line().up().length(1.5))
        cir_1_2.add(elm.Capacitor().tox(op_1_2.out).label('$C_1$'))
        cir_1_2.add(elm.Line().toy(op_1_2.out).dot())
        cir_1_2.pop()
        cir_1_2.add(elm.Resistor().tox(op_1_2.out).label('$R_2$'))
        cir_1_2.add(elm.Line().at(op_1_2.out).length(1.0).label('$V_{out}$', loc='right'))
        return cir_1_2
    '''
    if order==2 and A_0>=1:
        cir_2 = schem.Drawing()
        op_2 = cir_2.add(elm.Opamp(leads=True))
        cir_2.add(elm.Line().at(op_2.in2).left().length(1.0))
        cir_2.add(elm.Dot())
        R_2_2 = cir_2.add(elm.Resistor().left().label('$R_2$'))
        cir_2.add(elm.Dot())
        cir_2.add(elm.Resistor().left().label('$R_1$'))
        cir_2.add(elm.Line().left().length(0.1).label('$V_{in}$', loc='left'))
        cir_2.add(elm.Capacitor().at(R_2_2.start).toy(op_2.in1).label('$C_1$'))
        cir_2.add(elm.Line().tox(R_2_2.end))
        cir_2.add(elm.Ground())
        cir_2.add(elm.Line().at(R_2_2.end).down().length(1.0))
        cir_2.add(elm.Capacitor().tox(op_2.out).label('$C_1$'))
        cir_2.add(elm.Line().toy(op_2.out).dot())
        cir_2.add(elm.Line().at(op_2.out).right().length(1.0).label('$V_{out}$', loc='right'))
        cir_2.add(elm.Line().at(op_2.in1).up().length(1.0))
        cir_2.add(elm.Dot())
        R_2_3 = cir_2.add(elm.Resistor().left().label('$R_3$'))
        cir_2.add(elm.Ground())
        cir_2.add(elm.Resistor().at(R_2_3.start).tox(op_2.out).label('$R_4$'))
        cir_2.add(elm.Line().toy(op_2.out))
        return cir_2
    
    if order==3 and A_0>=1:
        cir_3_1 = schem.Drawing()
        op_3_1_1 = cir_3_1.add(elm.Opamp(leads=True))
        cir_3_1.add(elm.Resistor().at(op_3_1_1.in2).left().label('$R_{11}$'))
        cir_3_1.add(elm.Line().left().length(0.1).label('$V_{in}$', loc='left'))
        cir_3_1.add(elm.Capacitor().at(op_3_1_1.in2).down().label('$C_{11}$'))
        cir_3_1.add(elm.Ground())
        cir_3_1.add(elm.Line().at(op_3_1_1.in1).up().length(1.0))
        cir_3_1.add(elm.Dot())
        R_3_1_13 = cir_3_1.add(elm.Resistor().left().label('$R_{13}$'))
        cir_3_1.add(elm.Ground())
        cir_3_1.add(elm.Resistor().at(R_3_1_13.start).tox(op_3_1_1.out).label('$R_{12}$'))
        cir_3_1.add(elm.Line().toy(op_3_1_1.out).dot())
        cir_3_1.add(elm.Resistor().at(op_3_1_1.out).right().label('$R_{21}$').dot())
        R_3_1_22 = cir_3_1.add(elm.Resistor().right().label('$R_{22}$'))
        cir_3_1.add(elm.Line().right().length(0.5))
        op_3_1_2 = cir_3_1.add(elm.Opamp(leads=True).anchor('in2'))
        cir_3_1.add(elm.Line().at(R_3_1_22.start).down().length(1.0))
        cir_3_1.add(elm.Capacitor().tox(op_3_1_2.out).label('$C_{22}$'))
        cir_3_1.add(elm.Line().toy(op_3_1_2.out).dot())
        cir_3_1.add(elm.Capacitor().at(R_3_1_22.end).toy(op_3_1_2.in1).label('$C_{21}$'))
        cir_3_1.add(elm.Line().tox(R_3_1_22.start))
        cir_3_1.add(elm.Ground())
        cir_3_1.add(elm.Line().at(op_3_1_2.out).right().length(1.0).label('$V_{out}$', loc='right'))
        return cir_3_1
    '''
    if order==3 and A_0<1:
        cir_3_2 = schem.Drawing()
        op_3_2_1 = cir_3_2.add(elm.Opamp(leads=True))
        cir_3_2.add(elm.Ground().at(op_3_2_1.in2))
        cir_3_2.add(elm.Resistor().at(op_3_2_1.in1).left().label('$R_{11}$'))
        cir_3_2.add(elm.Line().left().length(0.1).label('$V_{in}$', loc='left'))
        cir_3_2.add(elm.Line().at(op_3_2_1.in1).up().length(1.0))
        R_3_2_12 = cir_3_2.add(elm.Resistor().tox(op_3_2_1.out).label('$R_{12}$'))
        cir_3_2.add(elm.Line().toy(op_3_2_1.out).dot())
        cir_3_2.add(elm.Line().at(R_3_2_12.start).up().length(1.5))
        cir_3_2.add(elm.Capacitor().tox(op_3_2_1.out).label('$C_{11}$'))
        cir_3_2.add(elm.Line().toy(R_3_2_12.end).dot())
        cir_3_2.add(elm.Resistor().at(op_3_2_1.out).right().label('$R_{21}$'))
        cir_3_2.add(elm.Dot())
        R_3_2_22 = cir_3_2.add(elm.Resistor().right().label('$R_{22}$'))
        op_3_2_2 = cir_3_2.add(elm.Opamp(leads=True).anchor('in2'))
        cir_3_2.add(elm.Capacitor().at(op_3_2_2.in2).down().label('$C_{21}$'))
        cir_3_2.add(elm.Ground())
        cir_3_2.add(elm.Line().at(R_3_2_22.start).up().length(3.0))
        cir_3_2.add(elm.Capacitor().tox(op_3_2_2.out).label('$C_{22}$'))
        cir_3_2.add(elm.Line().toy(op_3_2_2.out).dot())
        cir_3_2.add(elm.Line().at(op_3_2_2.in1).up().length(1.0))
        cir_3_2.add(elm.Line().tox(op_3_2_2.out).dot())
        cir_3_2.add(elm.Line().at(op_3_2_2.out).right().length(1.0).label('$V_{out}$', loc='right'))
        return cir_3_2
    '''
    if order==4 and A_0>=1:
        cir_4 = schem.Drawing()
        op_4_1 = cir_4.add(elm.Opamp(leads=True))
        cir_4.add(elm.Line().at(op_4_1.in2).left().length(0.5))
        cir_4.add(elm.Dot())
        R_4_12 = cir_4.add(elm.Resistor().left().label('$R_{12}$'))
        cir_4.add(elm.Dot())
        cir_4.add(elm.Resistor().left().label('$R_{11}$'))
        cir_4.add(elm.Line().left().length(0.1).label('$V_{in}$', loc='left'))
        cir_4.add(elm.Capacitor().at(R_4_12.start).toy(op_4_1.in1).label('$C_{11}$'))
        cir_4.add(elm.Line().tox(R_4_12.end))
        cir_4.add(elm.Ground())
        cir_4.add(elm.Line().at(R_4_12.end).down().length(1.0))
        cir_4.add(elm.Capacitor().tox(op_4_1.out).label('$C_{12}$'))
        cir_4.add(elm.Line().toy(op_4_1.out).dot())
        cir_4.add(elm.Line().at(op_4_1.in1).up().length(1.0))
        cir_4.add(elm.Dot())
        R_4_13 = cir_4.add(elm.Resistor().tox(R_4_12.end).label('$R_{13}$'))
        cir_4.add(elm.Ground())
        cir_4.add(elm.Resistor().at(R_4_13.start).tox(op_4_1.out).label('$R_{14}$'))
        cir_4.add(elm.Line().toy(op_4_1.out))
        cir_4.add(elm.Resistor().at(op_4_1.out).right().label('$R_{21}$'))
        cir_4.add(elm.Dot())
        R_4_22 = cir_4.add(elm.Resistor().right().label('$R_{22}$'))
        cir_4.add(elm.Dot())
        op_4_2 = cir_4.add(elm.Opamp(leads=True).anchor('in2'))
        cir_4.add(elm.Capacitor().at(op_4_2.in2).down().label('$C_{21}$'))
        cir_4.add(elm.Ground())
        cir_4.add(elm.Line().at(R_4_22.start).up().length(3.0))
        cir_4.add(elm.Capacitor().tox(op_4_2.out).label('$C_{22}$'))
        cir_4.add(elm.Line().toy(op_4_2.out).dot())
        cir_4.add(elm.Line().at(op_4_2.in1).up().length(1.0))
        cir_4.add(elm.Line().tox(op_4_2.out).dot())
        cir_4.add(elm.Line().at(op_4_2.out).right().length(1.0).label('$V_{out}$', loc='right'))
        return cir_4

    if order==5 and A_0>=1:
        cir_5_1 = schem.Drawing()
        op_5_1_1 = cir_5_1.add(elm.Opamp(leads=True))
        cir_5_1.add(elm.Resistor().at(op_5_1_1.in2).left().label('$R_{11}$'))
        cir_5_1.add(elm.Line().left().length(0.1).label('$V_{in}$', loc='left'))
        cir_5_1.add(elm.Capacitor().at(op_5_1_1.in2).down().label('$C_{11}$'))
        cir_5_1.add(elm.Ground())
        cir_5_1.add(elm.Line().at(op_5_1_1.in1).up().length(1.0))
        cir_5_1.add(elm.Dot())
        R_5_1_13 = cir_5_1.add(elm.Resistor().left().label('$R_{13}$'))
        cir_5_1.add(elm.Ground())
        cir_5_1.add(elm.Resistor().at(R_5_1_13.start).tox(op_5_1_1.out).label('$R_{12}$'))
        cir_5_1.add(elm.Line().toy(op_5_1_1.out).dot())
        cir_5_1.add(elm.Resistor().at(op_5_1_1.out).right().label('$R_{21}$'))
        cir_5_1.add(elm.Dot())
        R_5_1_22 = cir_5_1.add(elm.Resistor().right().label('$R_{22}$'))
        op_5_1_2 = cir_5_1.add(elm.Opamp(leads=True).anchor('in2'))
        cir_5_1.add(elm.Capacitor().at(op_5_1_2.in2).down().label('$C_{21}$'))
        cir_5_1.add(elm.Ground())
        cir_5_1.add(elm.Line().at(R_5_1_22.start).up().length(3.5))
        cir_5_1.add(elm.Capacitor().tox(op_5_1_2.out).label('$C_{22}$'))
        cir_5_1.add(elm.Line().toy(op_5_1_2.out).dot())
        cir_5_1.add(elm.Line().at(op_5_1_2.in1).up().length(1.0))
        cir_5_1.add(elm.Line().tox(op_5_1_2.out).dot())
        cir_5_1.add(elm.Resistor().at(op_5_1_2.out).right().label('$R_{31}$'))
        cir_5_1.add(elm.Dot())
        R_5_1_32 = cir_5_1.add(elm.Resistor().right().label('$R_{32}$'))
        op_5_1_3 = cir_5_1.add(elm.Opamp(leads=True).anchor('in2'))
        cir_5_1.add(elm.Capacitor().at(op_5_1_3.in2).down().label('$C_{31}$'))
        cir_5_1.add(elm.Ground())
        cir_5_1.add(elm.Line().at(R_5_1_32.start).up().length(3.5))
        cir_5_1.add(elm.Capacitor().tox(op_5_1_3.out).label('$C_{32}$'))
        cir_5_1.add(elm.Line().toy(op_5_1_3.out).dot())
        cir_5_1.add(elm.Line().at(op_5_1_3.in1).up().length(1.0))
        cir_5_1.add(elm.Line().tox(op_5_1_3.out).dot())
        cir_5_1.add(elm.Line().at(op_5_1_3.out).right().length(1.0).label('$V_{out}$', loc='right'))
        return cir_5_1
    '''
    if order==5 and A_0<1:
        cir_5_2 = schem.Drawing()
        op_5_2_1 = cir_5_2.add(elm.Opamp(leads=True))
        cir_5_2.add(elm.Ground().at(op_5_2_1.in2))
        cir_5_2.add(elm.Resistor().at(op_5_2_1.in1).left().label('$R_{11}$'))
        cir_5_2.add(elm.Line().left().length(0.1).label('$V_{in}$'))
        cir_5_2.add(elm.Line().at(op_5_2_1.in1).up().length(1.0))
        cir_5_2.add(elm.Dot())
        R_5_2_12 = cir_5_2.add(elm.Resistor().tox(op_5_2_1.out).label('$R_{12}$'))
        cir_5_2.add(elm.Line().toy(op_5_2_1.out).dot())
        cir_5_2.add(elm.Line().at(R_5_2_12.start).up().length(1.5))
        cir_5_2.add(elm.Capacitor().tox(op_5_2_1.out).label('$C_{11}$'))
        cir_5_2.add(elm.Line().toy(R_5_2_12.end).dot())
        cir_5_2.add(elm.Resistor().at(op_5_2_1.out).right().label('$R_{21}$'))
        cir_5_2.add(elm.Dot())
        R_5_2_22 = cir_5_2.add(elm.Resistor().right().label('$R_{22}$'))
        op_5_2_2 = cir_5_2.add(elm.Opamp(leads=True).anchor('in2'))
        cir_5_2.add(elm.Capacitor().at(op_5_2_2.in2).down().label('$C_{21}$'))
        cir_5_2.add(elm.Ground())
        cir_5_2.add(elm.Line().at(R_5_2_22.start).up().length(3.5))
        cir_5_2.add(elm.Capacitor().tox(op_5_2_2.out).label('$C_{22}$'))
        cir_5_2.add(elm.Line().toy(op_5_2_2.out).dot())
        cir_5_2.add(elm.Line().at(op_5_2_2.in1).up().length(1.0))
        cir_5_2.add(elm.Line().tox(op_5_2_2.out).dot())
        cir_5_2.add(elm.Resistor().at(op_5_2_2.out).right().label('$R_{31}$'))
        cir_5_2.add(elm.Dot())
        R_5_2_32 = cir_5_2.add(elm.Resistor().right().label('$R_{32}$'))
        op_5_2_3 = cir_5_2.add(elm.Opamp(leads=True).anchor('in2'))
        cir_5_2.add(elm.Capacitor().at(op_5_2_3.in2).down().label('$C_{31}$'))
        cir_5_2.add(elm.Ground())
        cir_5_2.add(elm.Line().at(R_5_2_32.start).up().length(3.5))
        cir_5_2.add(elm.Capacitor().tox(op_5_2_3.out).label('$C_{32}$'))
        cir_5_2.add(elm.Line().toy(op_5_2_3.out).dot())
        cir_5_2.add(elm.Line().at(op_5_2_3.in1).up().length(1.0))
        cir_5_2.add(elm.Line().tox(op_5_2_3.out).dot())
        cir_5_2.add(elm.Line().at(op_5_2_3.out).right().length(1.0).label('$V_{out}$', loc='right'))
        return cir_5_2
    '''
    if order==6 and A_0>=1:
        cir_6 = schem.Drawing()
        op_6_1 = cir_6.add(elm.Opamp(leads=True))
        cir_6.add(elm.Line().at(op_6_1.in2).left().length(0.5))
        R_6_12 = cir_6.add(elm.Resistor().left().label('$R_{12}$'))
        cir_6.add(elm.Dot())
        cir_6.add(elm.Resistor().left().label('$R_{11}$'))
        cir_6.add(elm.Line().left().length(0.1).label('$V_{in}$', loc='left'))
        cir_6.add(elm.Capacitor().at(R_6_12.start).toy(op_6_1.in1).label('$C_{11}$'))
        cir_6.add(elm.Line().tox(R_6_12.end))
        cir_6.add(elm.Ground())
        cir_6.add(elm.Line().at(R_6_12.end).down().length(1.0))
        cir_6.add(elm.Capacitor().tox(op_6_1.out).label('$C_{12}$'))
        cir_6.add(elm.Line().toy(op_6_1.out).dot())
        cir_6.add(elm.Line().at(op_6_1.in1).up().length(1.0))
        cir_6.add(elm.Dot())
        R_6_13 = cir_6.add(elm.Resistor().tox(R_6_12.end).label('$R_{13}$'))
        cir_6.add(elm.Ground())
        cir_6.add(elm.Resistor().at(R_6_13.start).tox(op_6_1.out).label('$R_{14}$'))
        cir_6.add(elm.Line().toy(op_6_1.out).dot())
        cir_6.add(elm.Resistor().at(op_6_1.out).right().label('$R_{21}$'))
        cir_6.add(elm.Dot())
        R_6_22 = cir_6.add(elm.Resistor().right().label('$R_{22}$'))
        op_6_2 = cir_6.add(elm.Opamp(leads=True).anchor('in2'))
        cir_6.add(elm.Capacitor().at(op_6_2.in2).down().label('$C_{21}$'))
        cir_6.add(elm.Ground())
        cir_6.add(elm.Line().at(R_6_22.start).up().length(3.5))
        cir_6.add(elm.Capacitor().tox(op_6_2.out).label('$C_{22}$'))
        cir_6.add(elm.Line().toy(op_6_2.out).dot())
        cir_6.add(elm.Line().at(op_6_2.in1).up().length(1.0))
        cir_6.add(elm.Line().tox(op_6_2.out).dot())
        cir_6.add(elm.Resistor().at(op_6_2.out).right().label('$R_{31}$'))
        cir_6.add(elm.Dot())
        R_6_32 = cir_6.add(elm.Resistor().right().label('$R_{32}$'))
        op_6_3 = cir_6.add(elm.Opamp(leads=True).anchor('in2'))
        cir_6.add(elm.Capacitor().at(op_6_3.in2).down().label('$C_{31}$'))
        cir_6.add(elm.Ground())
        cir_6.add(elm.Line().at(R_6_32.start).up().length(3.5))
        cir_6.add(elm.Capacitor().tox(op_6_3.out).label('$C_{32}$'))
        cir_6.add(elm.Line().toy(op_6_3.out).dot())
        cir_6.add(elm.Line().at(op_6_3.in1).up().length(1.0))
        cir_6.add(elm.Line().tox(op_6_3.out).dot())
        cir_6.add(elm.Line().at(op_6_3.out).right().length(1.0).label('$V_{out}$', loc='right'))
        return cir_6

# 频响特性
def Bode_Plot(order, omega_s, H_s, A_0):
    omega_c = 2*math.pi*omega_s/math.pow((math.pow(10,(H_s/(10)))-1),1/(2*order))
    if order==1:
        sys = ctrl.tf([A_0],[1/omega_c,1])
    if order==2:
        sys = ctrl.tf([A_0],[1/(omega_c*omega_c),1/omega_c,1])
    if order==3:
        sys = ctrl.tf([A_0],[1/math.pow(omega_c,3),2/math.pow(omega_c,2),2/omega_c,1])
    if order==4:
        sys = ctrl.tf([A_0],[1/math.pow(omega_c,4),2/math.pow(omega_c,3),3/math.pow(omega_c,2),2/omega_c,1])
    if order==5:
        sys = ctrl.tf([A_0],[1/math.pow(omega_c,5),3/math.pow(omega_c,4),5/math.pow(omega_c,3),5/math.pow(omega_c,2),3/omega_c,1])
    if order==6:
        sys = ctrl.tf([A_0],[1/math.pow(omega_c,6),3/math.pow(omega_c,5),6/math.pow(omega_c,4),7/math.pow(omega_c,3),6/math.pow(omega_c,2),3/omega_c,1])
    mag,phase,omega = ctrl.bode(sys, omega = np.logspace(start=math.log(omega_c)-15, stop=math.log(omega_c)-5, num=2000), dB=True, deg=False)
    
    plt.show()
    return

# 电路参数和灵敏度计算
def parameter(order, omega_s, H_s, A_0):
    omega_c = 2*math.pi*omega_s/math.pow((math.pow(10,(H_s/(10)))-1),1/(2*order))

    if order==1 and A_0>=1:
        C_1_1_1 = math.pow(10,-9)
        R_1_1_1 = round(1/(C_1_1_1*omega_c),2)
        R_1_1_2 = round((A_0-1)*100,2)
        R_1_1_3 = 100
        parameter_1_1 = '滤波器的电路参数如下：\n'
        parameter_1_1 += 'R_1='+str(R_1_1_1)+'Ω'+'\n'
        parameter_1_1 += 'C_1=1nF\n'
        parameter_1_1 += 'R_2='+str(R_1_1_2)+'Ω'+'\n'
        parameter_1_1 += 'R_3=100Ω\n'
        parameter_1_1 += '对该滤波器进行灵敏度分析：\n'
        s_A0_R2 = round(R_1_1_2/(A_0*R_1_1_3),2)
        parameter_1_1 += 'A_0对R_2的灵敏度为'+str(s_A0_R2)+'\n'
        s_A0_R3 = round(-R_1_1_2/(A_0*R_1_1_3),2)
        parameter_1_1 += 'A_0对R_3的灵敏度为'+str(s_A0_R3)+'\n'
        parameter_1_1 += 'f_-3dB对R_1的灵敏度为-1\n'
        parameter_1_1 += 'f_-3dB对C_1的灵敏度为-1\n'

        return parameter_1_1

    if order==1 and A_0<1:
        R_1_2_2 = round(1/(math.pow(10,-9)*omega_c),2)
        parameter_1_2 = 'R_1=100Ω\n'
        parameter_1_2 += 'R_2='+str(R_1_2_2)+'Ω'+'\n'
        parameter_1_2 += 'C_1=1nF\n'
        parameter_1_2 += '对该滤波器进行灵敏度分析：\n'
        parameter_1_2 += 'A_0对R_2的灵敏度为1\n'
        parameter_1_2 += 'A_0对R_1的灵敏度为-1\n'
        parameter_1_2 += 'f_-3dB对C_1的灵敏度为-1\n'
        parameter_1_2 += 'f_-3dB对R_2的灵敏度为-1\n'
        
        return parameter_1_2

    if order==2 and A_0>=1:
        C_2_1 = math.pow(10,-9)
        C_2_2 = 2*C_2_1
        k = 2*A_0-1 + math.sqrt((2*A_0-1)*(2*A_0-1)-(3-2*A_0)*(3-2*A_0))
        R_2_1 = round(1/(math.sqrt(2*k)*omega_c*C_2_1),2)
        R_2_2 = round(k*R_2_1,2)
        R_2_3 = 100
        R_2_4 = round((A_0-1)*R_2_3,2)
        
        parameter_2 = '滤波器的电路参数如下：\n'
        parameter_2 += 'R_1='+str(R_2_1)+'Ω\n'
        parameter_2 += 'R_2='+str(R_2_2)+'Ω\n'
        parameter_2 += 'R_3='+str(R_2_3)+'Ω\n'
        parameter_2 += 'R_4='+str(R_2_4)+'Ω\n'
        parameter_2 += 'C_1='+str(C_2_1)+'F\n'
        parameter_2 += 'C_2='+str(C_2_2)+'F\n'
        
        parameter_2 += '对该滤波器进行灵敏度分析：\n'
        s_A0_R4 = round(R_2_4/(A_0*R_2_3),2)
        parameter_2 += 'A_0对R_4的灵敏度为'+str(s_A0_R4)+'\n'
        s_A0_R3 = round(-R_2_4/(A_0*R_2_3),2)
        parameter_2 += 'A_0对R_3的灵敏度为'+str(s_A0_R3)+'\n'
        parameter_2 += 'f_-3dB对R_1的灵敏度为-1\n'
        parameter_2 += 'f_-3dB对C_1的灵敏度为-1\n'
        s_fc_R2 = round(-k/(1+k-2*(R_2_4/R_2_3)),2)
        parameter_2 += 'f_-3dB对R_2的灵敏度为'+str(s_fc_R2)+'\n'
        s_fc_R3 = round(-(2*(R_2_4/R_2_3))/(1+k-2*(R_2_4/R_2_3)),2)
        parameter_2 += 'f_-3dB对C_2的灵敏度为'+str(s_fc_R3)+'\n'
        s_fc_R4 = round((2*(R_2_4/R_2_3))/(1+k-2*(R_2_4/R_2_3)),2)
        parameter_2 += 'f_-3dB对R_4的灵敏度为'+str(s_fc_R4)+'\n'
        s_fc_C2 = round((2*(R_2_4/R_2_3))/(1+k-2*(R_2_4/R_2_3)),2)
        parameter_2 += 'f_-3dB对R_3的灵敏度为'+str(s_fc_C2)+'\n'

        return parameter_2

    if order==3:
        R_3_13 = 100
        R_3_12 = round((A_0-1)*R_3_13,2)
        C_3_11 = math.pow(10,-9)
        R_3_11 = round(1/(C_3_11*omega_c),2)
        C_3_21 = math.pow(10,-9)
        C_3_22 = 4*C_3_21
        R_3_21 = round(1/(2*omega_c*C_3_21),2)
        R_3_22 = round(R_3_21,2)

        parameter_3 = '滤波器的电路参数如下：\n'
        parameter_3 += 'R_11='+str(R_3_11)+'Ω\n'
        parameter_3 += 'R_12='+str(R_3_12)+'Ω\n'
        parameter_3 += 'R_13='+str(R_3_13)+'Ω\n'
        parameter_3 += 'R_21='+str(R_3_21)+'Ω\n'
        parameter_3 += 'R_22='+str(R_3_22)+'Ω\n'
        parameter_3 += 'C_11='+str(C_3_11)+'F\n'
        parameter_3 += 'C_21='+str(C_3_21)+'F\n'
        parameter_3 += 'C_22='+str(C_3_22)+'F\n'

        parameter_3 += '对该滤波器进行灵敏度分析：\n'
        s_A0_R12 = round(R_3_12/(A_0*R_3_13),2)
        parameter_3 += 'A_0对R_12的灵敏度为'+str(s_A0_R12)+'\n'
        s_A0_R13 = round(-R_3_12/(A_0*R_3_13),2)
        parameter_3 += 'A_0对R_13的灵敏度为'+str(s_A0_R13)+'\n'
        parameter_3 += 'f_-3dB对R_11的灵敏度为'+str(-1.0/3.0)+'\n'
        parameter_3 += 'f_-3dB对C_11的灵敏度为'+str(-1.0/3.0)+'\n'
        s_fc_R21 = round(-(2.0/3.0)*R_3_21/(R_3_21+R_3_22),2)
        parameter_3 += 'f_-3dB对R_21的灵敏度为'+str(s_fc_R21)+'\n'
        parameter_3 += 'f_-3dB对R_22的灵敏度为'+str(-1.0/3.0)+'\n'
        parameter_3 += 'f_-3dB对C_22的灵敏度为0\n'
        parameter_3 += 'f_-3dB对C_21的灵敏度为'+str(-2.0/3.0)+'\n'

        return parameter_3

    if order==4:        
        C_4_11 = math.pow(10,-9)
        C_4_12 = 1.41422*math.pow(10,-9)
        k = math.sqrt(2.0)*A_0 + math.sqrt(2*A_0*A_0+math.sqrt(2.0)*(A_0-1)*(A_0-1)-1)
        R_4_11 = round(1/(math.sqrt(math.sqrt(2.0)*k)*omega_c*C_4_11),2)
        R_4_12 = round(k*R_4_11,2)
        R_4_13 = 100
        R_4_14 = round((A_0-1)*R_4_13,2)
        C_4_21 = math.pow(10,-9)
        C_4_22 = 9*math.pow(10,-9)
        R_4_21 = round(1/(math.sqrt(9*0.3412)*omega_c*C_4_21),2)
        R_4_22 = round(0.3412*R_4_21,2)

        parameter_4 = '滤波器的电路参数如下：\n'
        parameter_4 += 'R_11='+str(R_4_11)+'Ω\n'
        parameter_4 += 'R_12='+str(R_4_12)+'Ω\n'
        parameter_4 += 'R_13='+str(R_4_13)+'Ω\n'
        parameter_4 += 'R_14='+str(R_4_14)+'Ω\n'
        parameter_4 += 'R_21='+str(R_4_21)+'Ω\n'
        parameter_4 += 'R_22='+str(R_4_22)+'Ω\n'
        parameter_4 += 'C_11='+str(C_4_11)+'F\n'
        parameter_4 += 'C_12='+str(C_4_12)+'F\n'
        parameter_4 += 'C_21='+str(C_4_21)+'F\n'
        parameter_4 += 'C_22='+str(C_4_22)+'F\n'

        parameter_4 += '对该滤波器进行灵敏度分析：\n'
        s_A0_R14 = round(R_4_14/(A_0*R_4_13),2)
        parameter_4 += 'A_0对R_14的灵敏度为'+str(s_A0_R14)+'\n'
        s_A0_R13 = round(-R_4_14/(A_0*R_4_13),2)
        parameter_4 += 'A_0对R_13的灵敏度为'+str(s_A0_R13)+'\n'
        s_fc_R21 = round(-2*R_4_21/(R_4_21+R_4_22),2)
        parameter_4 += 'f_-3dB对R_21的灵敏度为'+str(s_fc_R21)+'\n'
        s_fc_R22 = round(-2*R_4_22/(R_4_21+R_4_22),2)
        parameter_4 += 'f_-3dB对R_22的灵敏度为'+str(s_fc_R22)+'\n'
        parameter_4 += 'f_-3dB对C_21的灵敏度为-0.5\n'
        parameter_4 += 'f_-3dB对C_22的灵敏度为-0.5\n'
        s_fc_R11 = round((C_4_11-(A_0-1)*C_4_12)*omega_c*R_4_11/0.7654,2)
        parameter_4 += 'f_-3dB对R_11的灵敏度为'+str(s_fc_R11)+'\n'
        s_fc_R12 = round(-R_4_12*C_4_11*omega_c/0.7654,2)
        parameter_4 += 'f_-3dB对R_12的灵敏度为'+str(s_fc_R12)+'\n'
        s_fc_R13 = round(-(R_4_14/R_4_13)*R_4_11*C_4_12*omega_c/0.7654,2)
        parameter_4 += 'f_-3dB对R_13的灵敏度为'+str(s_fc_R13)+'\n'
        s_fc_R14 = round((R_4_14/R_4_13)*R_4_11*C_4_12*omega_c/0.7654,2)
        parameter_4 += 'f_-3dB对R_14的灵敏度为'+str(s_fc_R14)+'\n'
        s_fc_C11 = round(-(R_4_11+R_4_12)*C_4_11*omega_c/0.7654,2)
        parameter_4 += 'f_-3dB对C_11的灵敏度为'+str(s_fc_C11)+'\n'
        s_fc_C12 = round((R_4_14/R_4_13)*R_4_11*C_4_12*omega_c/0.7654,2)
        parameter_4 += 'f_-3dB对C_12的灵敏度为'+str(s_fc_C12)+'\n'

        return parameter_4

    if order==5:
        C_5_11 = math.pow(10,-9)
        R_5_11 = round(1/(omega_c*C_5_11),2)
        R_5_13 = 100
        R_5_12 = round((A_0-1)*R_5_13,2)
        C_5_21 = math.pow(10,-9)
        C_5_22 = 2*C_5_21
        R_5_21 = round(1/(math.sqrt(2*0.3460)*omega_c*C_5_21),2)
        R_5_22 = round(0.3460*R_5_21,2)
        C_5_31 = math.pow(10,-9)
        C_5_32 = 16*C_5_31
        R_5_31 = round(1/(math.sqrt(16*0.2597)*omega_c*C_5_31),2)
        R_5_32 = round(0.2597*R_5_31,2)

        parameter_5_1 = '滤波器的电路参数如下：\n'
        parameter_5_1 += 'R_11='+str(R_5_11)+'Ω\n'
        parameter_5_1 += 'R_12='+str(R_5_12)+'Ω\n'
        parameter_5_1 += 'R_13='+str(R_5_13)+'Ω\n'
        parameter_5_1 += 'R_21='+str(R_5_21)+'Ω\n'
        parameter_5_1 += 'R_22='+str(R_5_22)+'Ω\n'
        parameter_5_1 += 'R_31='+str(R_5_31)+'Ω\n'
        parameter_5_1 += 'R_32='+str(R_5_32)+'Ω\n'
        parameter_5_1 += 'C_11='+str(C_5_11)+'F\n'
        parameter_5_1 += 'C_21='+str(C_5_21)+'F\n'
        parameter_5_1 += 'C_22='+str(C_5_22)+'F\n'
        parameter_5_1 += 'C_31='+str(C_5_31)+'F\n'
        parameter_5_1 += 'C_32='+str(C_5_32)+'F\n'

        parameter_5_1 += '对该滤波器进行灵敏度分析：\n'
        s_A0_R12 = round(R_5_12/(A_0*R_5_13),2)
        parameter_5_1 += 'A_0对R_12的灵敏度为'+str(s_A0_R12)+'\n'
        s_A0_R13 = round(-R_5_12/(A_0*R_5_13),2)
        parameter_5_1 += 'A_0对R_13的灵敏度为'+str(s_A0_R13)+'\n'
        parameter_5_1 += 'f_-3dB对R_11的灵敏度为-0.2\n'
        parameter_5_1 += 'f_-3dB对C_11的灵敏度为-0.2\n'
        s_fc_R21 = round(-(2.0/3.0)*R_5_21/(R_5_21+R_5_22),2)
        parameter_5_1 += 'f_-3dB对R_21的灵敏度为'+str(s_fc_R21)+'\n'
        s_fc_R22 = round(-(2.0/3.0)*R_5_22/(R_5_21+R_5_22),2)
        parameter_5_1 += 'f_-3dB对R_22的灵敏度为'+str(s_fc_R22)+'\n'
        parameter_5_1 += 'f_-3dB对C_21的灵敏度为'+str(2.0/3.0)+'\n'
        parameter_5_1 += 'f_-3dB对C_22的灵敏度为0\n'
        s_fc_R31 = round(-(2.0/3.0)*R_5_31/(R_5_31+R_5_32),2)
        parameter_5_1 += 'f_-3dB对R_31的灵敏度为'+str(s_fc_R31)+'\n'
        s_fc_R32 = round(-(2.0/3.0)*R_5_32/(R_5_31+R_5_32),2)
        parameter_5_1 += 'f_-3dB对R_32的灵敏度为'+str(s_fc_R32)+'\n'
        parameter_5_1 += 'f_-3dB对C_31的灵敏度为'+str(2.0/3.0)+'\n'
        parameter_5_1 += 'f_-3dB对C_32的灵敏度为0\n'

        return parameter_5_1

    if order==6:
        C_6_11 = math.pow(10,-9)
        C_6_12 = 2*C_6_11
        k = 2*A_0+math.sqrt(3.0)-1 + math.sqrt((2*A_0+math.sqrt(3.0)-1)*(2*A_0+math.sqrt(3.0)-1)-(3-2*A_0)*(3-2*A_0))
        R_6_11 = round(1/(math.sqrt(k*2)*omega_c*C_6_11),2)
        R_6_12 = round(k*R_6_11,2)
        R_6_13 = 100
        R_6_14 = round((A_0-1)*R_6_13,2)
        C_6_21 = math.pow(10,-9)
        C_6_22 = 2*C_6_21
        R_6_21 = round(1/(math.sqrt(2.0)*omega_c*C_6_21),2)
        R_6_22 = round(R_6_21,2)
        C_6_31 = math.pow(10,-9)
        C_6_32 = 16*C_6_31
        R_6_31 = round(1/(math.sqrt(16*0.5888)*omega_c*C_6_31),2)
        R_6_32 = round(0.5888*R_6_31,2)

        parameter_6 = '滤波器的电路参数如下：\n'
        parameter_6 += 'R_11='+str(R_6_11)+'Ω\n'
        parameter_6 += 'R_12='+str(R_6_12)+'Ω\n'
        parameter_6 += 'R_13='+str(R_6_13)+'Ω\n'
        parameter_6 += 'R_14='+str(R_6_14)+'Ω\n'
        parameter_6 += 'R_21='+str(R_6_21)+'Ω\n'
        parameter_6 += 'R_22='+str(R_6_22)+'Ω\n'
        parameter_6 += 'R_31='+str(R_6_31)+'Ω\n'
        parameter_6 += 'R_32='+str(R_6_32)+'Ω\n'
        parameter_6 += 'C_11='+str(C_6_11)+'F\n'
        parameter_6 += 'C_12='+str(C_6_12)+'F\n'
        parameter_6 += 'C_21='+str(C_6_21)+'F\n'
        parameter_6 += 'C_22='+str(C_6_22)+'F\n'
        parameter_6 += 'C_31='+str(C_6_31)+'F\n'
        parameter_6 += 'C_32='+str(C_6_32)+'F\n'

        parameter_6 +=  '对该滤波器进行灵敏度分析：\n'
        s_A0_R14 = round(R_6_14/(A_0*R_6_13),2)
        parameter_6 += 'A_0对R_14的灵敏度为'+str(s_A0_R14)+'\n'
        s_A0_R13 = round(-R_6_14/(A_0*R_6_13),2)
        parameter_6 += 'A_0对R_13的灵敏度为'+str(s_A0_R13)+'\n'
        s_fc_R21 = round(-R_6_21/(2*(R_6_21+R_6_22)),2)
        parameter_6 += 'f_-3dB对R_21的灵敏度为'+str(s_fc_R21)+'\n'
        s_fc_R22 = round(-R_6_22/(2*(R_6_21+R_6_22)),2)
        parameter_6 += 'f_-3dB对R_22的灵敏度为'+str(s_fc_R22)+'\n'
        parameter_6 += 'f_-3dB对C_21的灵敏度为-0.5\n'
        parameter_6 += 'f_-3dB对C_22的灵敏度为0\n'
        s_fc_R31 = round(-R_6_31/(2*(R_6_31+R_6_32)),2)
        parameter_6 += 'f_-3dB对R_31的灵敏度为'+str(s_fc_R31)+'\n'
        s_fc_R32 = round(-R_6_32/(2*(R_6_31+R_6_32)),2)
        parameter_6 += 'f_-3dB对R_32的灵敏度为'+str(s_fc_R32)+'\n'        
        parameter_6 += 'f_-3dB对C_31的灵敏度为-0.5\n'
        parameter_6 += 'f_-3dB对C_32的灵敏度为0\n'
        s_fc_R11 = round(-0.5*(omega_c/0.5176)*(C_6_11-((R_6_14/R_6_13)*C_6_12)*R_6_11),2)
        parameter_6 += 'f_-3dB对R_21的灵敏度为'+str(s_fc_R11)+'\n'
        s_fc_R12 = round(-0.5*(omega_c/0.5176)*R_6_12*C_6_11,2)
        parameter_6 += 'f_-3dB对R_21的灵敏度为'+str(s_fc_R12)+'\n'
        s_fc_R13 = round(-0.5*(omega_c/0.5176)*(-R_6_14*R_6_11*C_6_12/R_6_13),2)
        parameter_6 += 'f_-3dB对R_21的灵敏度为'+str(s_fc_R13)+'\n'
        s_fc_R14 = round(-0.5*(omega_c/0.5176)*(R_6_14*R_6_11*C_6_12/R_6_13),2)
        parameter_6 += 'f_-3dB对R_21的灵敏度为'+str(s_fc_R14)+'\n'
        s_fc_C11 = round(-0.5*(omega_c/0.5176)*(R_6_11+R_6_12)*C_6_11,2)
        parameter_6 += 'f_-3dB对R_21的灵敏度为'+str(s_fc_C11)+'\n'
        s_fc_C12 = round(-0.5*(-R_6_14*R_6_11*C_6_12/R_6_13),2)
        parameter_6 += 'f_-3dB对R_21的灵敏度为'+str(s_fc_C12)+'\n'

        return parameter_6