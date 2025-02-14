'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2025-02-14 09:47:58
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2025-02-14 09:49:40
FilePath: \undefinedc:\Users\Administrator\Desktop\timer_config.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import pandas as pd
#required clk freq
Freq = 255*2488.32/25/238
str_print = "Freq = {}".format(Freq)
print(str_print)
N = 1
Fref = 122.88
VCO_flag = 100
N_list = []
for N in range(1,1024):
    Fvco = Freq * N
    if Fvco >= 2440 and Fvco <= 2580:
        VCO_flag = 0
        str_print = "VCO{}, N = {}, Fvco = {}".format(VCO_flag, N, Fvco)
        print(str_print)
        N_list.append(N)
    if Fvco >= 2945 and Fvco <= 3255:
        VCO_flag = 1
        str_print = "VCO{}, N = {}, Fvco = {}".format(VCO_flag, N, Fvco)
        print(str_print)
        N_list.append(N)
#分解质因数网站：https://www.imathtool.com/jisuanqi/zhiyinshu/
for P in range(2,9):
    for N2 in range(1,262144):
        for R2 in range(1,4096):
            for N in N_list:
                Freq_config = 122.88*P*N2/N/R2
                Freq_error =  abs(Freq_config - Freq)
                if Freq_error<1e-10:
                    str_print = "P={}, N2={}, R2={}, N={}, Freq_error = {}".format(P,N2,R2,N, Freq_error)
                    print(str_print)
                    N_list.remove(N)
                    if len(N_list) == 0: 
                        break