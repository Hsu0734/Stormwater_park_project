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

# Drawing plot
fig = plt.figure(figsize=(8, 12), dpi=300) #Inches Width, Height
fig.suptitle("Subcatchments, Nodes, Links data output")
fig.set_tight_layout(True)

# Simulation
sim = Simulation("../Jiangning.inp")
time_stamps = []

# 创建Subcatchments，Nodes, Links集合
# 查找所有子汇水区 All Subcatchments
subcatchments = Subcatchments(sim)
subcatchment_names = [subcatchment.subcatchmentid for subcatchment in subcatchments]
print(subcatchment_names)
runoff_data = {}
for subcatchment_name in subcatchment_names:
    subcatchment = Subcatchments(sim)[subcatchment_name]
    runoff_data[subcatchment_name] = []

# 查找所有节点 All Nodes
nodes = Nodes(sim)
node_names = [node.nodeid for node in nodes]
print(node_names)
inflow_data = {}
for node_name in node_names:
    node = Nodes(sim)[node_name]
    inflow_data[node_name] = []

# 查找所有链接 All Links
links = Links(sim)
link_names = [link.linkid for link in links] # 添加模型中的link name (这个模型node和link取名重合了，应注意避免）
print(link_names)
link_inflow_data = {}
for link_name in link_names:
    link = Links(sim)[link_name]
    link_inflow_data[link_name] = []

# 添加模拟数据
'''for step in sim:
    time_stamps.append(sim.current_time)
    for subcatchment_name in subcatchment_names:
        subcatchment = Subcatchments(sim)[subcatchment_name]
        runoff_data[subcatchment_name].append(subcatchment.runoff)   # choose your sub data

    for node_name in node_names:
        node = Nodes(sim)[node_name]
        inflow_data[node_name].append(node.total_inflow)   # choose your node data

    for link_name in link_names:
        link = Links(sim)[link_name]
        link_inflow_data[link_name].append(link.flow)   # choose your link data

for subcatchment_name in subcatchment_names:
    # print(runoff_data[subcatchment_name])
    fig01 = plt.subplot(3, 1, 1)
    fig01.set_ylabel("Runoff volume (CMS)")  # label标签字号
    fig01.set_xlabel("Time")
    fig01.plot(time_stamps, runoff_data[subcatchment_name], label=f"{subcatchment_name}")
    fig01.grid("xy")
    fig01.legend()

for node_name in node_names:
    # print(inflow_data[node_name])
    fig02 = plt.subplot(3, 1, 2)
    fig02.set_ylabel("Inflow volume (CMS)")  # label标签字号
    fig02.set_xlabel("Time")
    fig02.plot(time_stamps, inflow_data[node_name], label=f"{node_name}")
    fig02.grid("xy")
    fig02.legend()

for link_name in link_names:
    # print(link_inflow_data[link_name])
    fig03 = plt.subplot(3, 1, 3)
    fig03.set_ylabel("Inflow volume (CMS)")  # label标签字号
    fig03.set_xlabel("Time")
    fig03.plot(time_stamps, link_inflow_data[link_name], label=f"{link_name}")
    fig03.grid("xy")
    fig03.legend()

plt.show()
sim.close()'''