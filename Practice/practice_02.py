'''
PySWMM Code Example
添加for循环语句输出所有Subcatchments， Nodes， Links的名称集合和相关数据
Loop through and output the name collections and related data for all Subcatchments, Nodes, and Links.
Author: Hanwen Xu
Version: 1
Date: May 14, 2023
'''

from pyswmm import Simulation, Subcatchments, Nodes, Links
import matplotlib.pyplot as plt

# Simulation
sim = Simulation("../Jiangning.inp")
time_stamps = []
SS1 = []

# 创建Subcatchments，Nodes, Links集合
# 查找所有子汇水区 All Subcatchments
subcatchments = Subcatchments(sim)
for i in range (1, 3, 1):
    S1 = subcatchments.__getitem__('S{i}')
for step in sim:
    time_stamps.append(sim.current_time)
    SS1.append(S1.runoff)


'''subcatchment_names = [subcatchment.subcatchmentid for subcatchment in subcatchments]
print(subcatchment_names)
runoff_data = {}
for subcatchment_name in subcatchment_names:
    subcatchment = Subcatchments(sim)[subcatchment_name]
    runoff_data[subcatchment_name] = []'''


'''for subcatchment_name in subcatchment_names:
    # print(runoff_data[subcatchment_name])
    fig01 = plt.subplot(3, 1, 1)
    fig01.set_ylabel("Runoff volume (CMS)")  # label标签字号
    fig01.set_xlabel("Time")
    fig01.plot(time_stamps, runoff_data[subcatchment_name], label=f"{subcatchment_name}")
    fig01.grid("xy")
    fig01.legend()'''

fig = plt.figure(figsize=(8,4), dpi=300) #Inches Width, Height
fig.suptitle("Runoff Volume of Subcatchments")
fig.set_tight_layout(True)
# Plot from the results compiled during simulation time
plt.plot(time_stamps, SS1, '--g')
plt.show()
sim.close()