import skfuzzy as fuzz
import numpy as np
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

x_dhumi_range = np.arange(-6, 101, 1, np.float32)
x_hc_range = np.arange(-1, 6, 1, np.float32)
y_output_range = np.arange(0, 101, 1, np.float32)

# 创建模糊控制变量

x_dhumi = ctrl.Antecedent(x_dhumi_range, 'dhumi')
x_hc = ctrl.Antecedent(x_hc_range, 'hc')
y_output = ctrl.Consequent(y_output_range, 'output')

# 定义模糊集和其隶属度函数

x_dhumi['N'] = fuzz.trimf(x_dhumi_range, [-6, -6, 47])
x_dhumi['M'] = fuzz.trimf(x_dhumi_range, [-6, 47,100])
x_dhumi['P'] = fuzz.trimf(x_dhumi_range, [47, 100, 100])

x_hc['N'] = fuzz.trimf(x_hc_range, [-1, -1, 2])
x_hc['M'] = fuzz.trimf(x_hc_range, [-1, 2, 5])
x_hc['P'] = fuzz.trimf(x_hc_range, [2, 5, 5])

y_output['N'] = fuzz.trimf(y_output_range, [0, 0, 50])
y_output['M'] = fuzz.trimf(y_output_range, [0, 50, 100])
y_output['P'] = fuzz.trimf(y_output_range, [50, 100, 100])

# 设定输出output的解模糊方法——质心解模糊方式
y_output.defuzzify_method = 'centroid'

# 输出为N的规则
rule0 = ctrl.Rule(antecedent=((x_dhumi['N'] & x_hc['P']) | (x_dhumi['M'] & x_hc['P']) | (x_dhumi['N'] & x_hc['M'])),
                  consequent=y_output['N'], label='rule N')

# 输出为M的规则
rule1 = ctrl.Rule(antecedent=((x_dhumi['M'] & x_hc['N']) | (x_dhumi['N'] & x_hc['N']) | (x_dhumi['M'] & x_hc['M']) |
                              (x_dhumi['P'] & x_hc['P']) ),
                  consequent=y_output['M'], label='rule M')

# 输出为P的规则
rule2 = ctrl.Rule(antecedent=((x_dhumi['P'] & x_hc['N']) | (x_dhumi['P'] & x_hc['M'])),
                  consequent=y_output['P'], label='rule P')

# 系统和运行环境初始化
system = ctrl.ControlSystem(rules=[rule0, rule1, rule2])
sim = ctrl.ControlSystemSimulation(system)
x_dhumi.view()
x_hc.view()
y_output.view()
plt.show()

# input
def fuzzyctrl(dhumi,hc):
    sim.input['dhumi'] = dhumi
    sim.input['hc'] = hc

    sim.compute()  # 运行系统
    output_output = sim.output['output']
    return output_output
#
# print(fuzzyctrl(4,8))
