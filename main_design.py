import tkinter as tk
import circuit_design
import schemdraw as schem
import time
import matplotlib

def design(order, omega_p, omega_s, H_p, H_s, A_0):
    window_design = tk.Tk()
    window_design.title('Design')
    window_design.geometry('500x600')
    order = int(order)
    label_order = tk.Label(window_design, text='需要设计的低通滤波器为'+str(order)+'阶，请点击按钮查看电路结构和频响特性。', font=('宋体',10))
    label_order.place(x=10, y=20, anchor='nw')

    # 电路设计
    circuit = circuit_design.circuit(order, A_0)
    def circuit_drawing():
        circuit.draw()
        return
    button_circuit = tk.Button(window_design, text='点击查看电路结构', width=20, height=1, command=circuit_drawing)
    button_circuit.place(x=10, y=60, anchor='nw')

    # 频响特性
    def bode_drawing():
        circuit_design.Bode_Plot(order, omega_s, H_s, A_0)
        return
    button_bode = tk.Button(window_design,text='点击查看频响特性', width=20, height=1, command=bode_drawing)
    button_bode.place(x=200, y=60, anchor='nw')
    
    # 电路参数和敏感度分析
    paramenters = circuit_design.parameter(order, omega_s, H_s, A_0)
    text_para = tk.Text(window_design, height=35)
    text_para.place(x=10, y=100, anchor='nw')
    text_para.insert('insert', paramenters)

    window_design.mainloop()

    return