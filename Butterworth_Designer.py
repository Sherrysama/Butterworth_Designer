import tkinter as tk
from tkinter import messagebox
import math
import main_design

def input_check(omega_p, omega_s, H_p, H_s, H_0):
    if 0<omega_p<omega_s and (0<H_p<H_s or 0>H_p>H_s) and H_0>=0:
        return True
    else:
        return False

def order_calculating(omega_p, omega_s, H_p, H_s):
    order_num = math.log((math.pow(10,(H_s/10))-1)/(math.pow(10,(H_p/10))-1))
    order_den = 2*math.log(omega_s/omega_p)
    order = order_num/order_den
    order = math.ceil(order)
    return order

def main_view():
    window_input = tk.Tk()
    window_input.title('Butterworth Designer')
    window_input.geometry('400x300')

    # GUI界面
    label_title = tk.Label(window_input, text='请输入Butterworth低通滤波器的设计指标要求：', font=('宋体',12))
    label_title.place(x=5, y=10, anchor='nw')

    # 通带频率 ω_p(omega_p)
    label_omega_p = tk.Label(window_input, text='通带频率（Hz）', font=('宋体',12))
    label_omega_p.place(x=170, y=50, anchor='ne')
    entry_omega_p = tk.Entry(window_input, show=None)
    entry_omega_p.place(x=180, y=50, anchor='nw')

    # 阻带频率 ω_s(omega_s)
    label_omega_s = tk.Label(window_input, text='阻带频率（Hz）', font=('宋体',12))
    label_omega_s.place(x=170, y=80, anchor='ne')
    entry_omega_s = tk.Entry(window_input, show=None)
    entry_omega_s.place(x=180, y=80, anchor='nw')

    # 通带最大衰减 H_p
    label_H_p = tk.Label(window_input, text='通带最大衰减（dB）', font=('宋体',12))
    label_H_p.place(x=170, y=110, anchor='ne')
    entry_H_p = tk.Entry(window_input, show=None)
    entry_H_p.place(x=180, y=110, anchor='nw')
    
    # 阻带最小衰减 H_s
    label_H_s = tk.Label(window_input, text='阻带最小衰减（dB）', font=('宋体',12))
    label_H_s.place(x=170, y=140, anchor='ne')
    entry_H_s = tk.Entry(window_input, show=None)
    entry_H_s.place(x=180, y=140, anchor='nw')
    
    # 直流增益 H_0
    label_H_0 = tk.Label(window_input, text='直流增益（dB）', font=('宋体',12))
    label_H_0.place(x=170, y=170, anchor='ne')
    entry_H_0 = tk.Entry(window_input, show=None)
    entry_H_0.place(x=180, y=170, anchor='nw')

    # design按钮
    # 点击后获取输入并先进行数据检查，对不符合Butterworth滤波器要求的输入发出弹窗报错
    # 数据检查为True后，求出需要的滤波器阶数，阶数大于6时拒绝处理
    # 对于阶数小于等于6的情况，使用design()函数进行辅助设计
    def data_get():
        omega_p = float(entry_omega_p.get())
        omega_s = float(entry_omega_s.get())
        H_p = float(entry_H_p.get())
        H_s = float(entry_H_s.get())
        H_0 = float(entry_H_0.get())
        A_0 = math.pow(10, (H_0/20))
        if not(input_check(omega_p, omega_s, H_p, H_s, H_0)):
            tk.messagebox.showerror(title='ERROR', message='数据错误，请检查您的数据并重新输入！')
            return
        order = order_calculating(omega_p, omega_s, H_p, H_s);
        if order>6:
            tk.messagebox.showinfo(title='ATTENTION', message='设计指标要求过高，滤波器阶数超过6阶')
        if 0<order<=6:
            main_design.design(order, omega_p, omega_s, H_p, H_s, A_0)
        return
    button_1 = tk.Button(window_input, text='design', width=20, height=1, command=data_get)
    button_1.place(x=20, y=210, anchor='nw')

    # clear按钮，可以清空所有输入
    def clear():
        entry_omega_p.delete(0,tk.END)
        entry_omega_s.delete(0,tk.END)
        entry_H_p.delete(0,tk.END)
        entry_H_s.delete(0,tk.END)
        entry_H_0.delete(0,tk.END)
        return
    button_2 = tk.Button(window_input, text='clear', width=20, height=1, command=clear)
    button_2.place(x=200, y=210, anchor='nw')

    window_input.mainloop()
    return

def main():
    main_view()
    return

if __name__ == '__main__':
    main()