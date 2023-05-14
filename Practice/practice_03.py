'''
PySWMM Code Example
查找指定汇水区、节点、链接、整个系统在指定时间的所有属性 Output
Author: Hanwen Xu
Version: 1
Date: May 15, 2023
'''

from pyswmm import Output
from datetime import datetime

with Output("../Jiangning.out") as out:

# the whole model information
    print(len(out.subcatchments))
    #查看汇水区数量
    print(len(out.nodes))
    # 查看节点数量
    print(len(out.links))
    # 查看链接数量


# 查找具体某个subcatchment, node, link, system在某一时刻的信息
# specific subcatchment, node, link, system information

    # Subcatchment
    data = out.subcatch_result('S1', datetime(2018, 5, 2, 1, 5, 59)) #年，月，日，时，分，秒
    for attribute in data:
        print(attribute, data[attribute])
    print()

    # Node
    data2 = out.node_result('j1', datetime(2018, 5, 2, 1, 5, 59))
    for attribute in data2:
        print(attribute, data2[attribute])
    print()

    # Link
    data3 = out.link_result('gq1', datetime(2018, 5, 2, 1, 5, 59))
    for attribute in data3:
        print(attribute, data3[attribute])
    print()

    # system
    system_data = out.system_result(datetime(2018, 5, 2, 1, 5, 59))
    for attribute in system_data:
        print(attribute, system_data[attribute])