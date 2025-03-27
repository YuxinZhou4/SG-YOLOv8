import matplotlib.pyplot as plt
import numpy as np

# 数据
num = np.arange(1, 11)
precision = [90.82, 91.02, 91.47, 90.90, 91.37, 91.50, 91.19, 90.88, 91.19, 91.57]
recall = [83.94, 84.32, 84.84, 83.18, 84.44, 84.49, 84.27, 83.87, 83.35, 83.16]
map_05 = [91.08, 91.28, 91.63, 90.27, 91.56, 91.50, 91.36, 91.13, 90.78, 90.71]
map_095 = [69.07, 69.10, 69.56, 71.18, 69.44, 69.35, 69.02, 68.87, 68.40, 68.43]

# 计算每个指标的平均值和标准差
precision_mean = np.mean(precision)
recall_mean = np.mean(recall)
map_05_mean = np.mean(map_05)
map_095_mean = np.mean(map_095)

precision_std = np.std(precision)
recall_std = np.std(recall)
map_05_std = np.std(map_05)
map_095_std = np.std(map_095)

# 设置字体为Times New Roman
plt.rcParams.update({'font.family': 'Times New Roman'})

# 绘制柱状图并更新置信区间线段和数据点大小
plt.figure(figsize=(8, 6))

# 绘制Precision柱状图
plt.bar(1, precision_mean, yerr=precision_std, capsize=5, color='lightcoral', label='Precision', edgecolor='black', alpha=0.7, width=0.35)
plt.errorbar(1, precision_mean, yerr=precision_std, fmt='none', ecolor='red', capsize=5, capthick=2, elinewidth=3)
plt.scatter(np.repeat(1, 10), precision, color='black', marker='o', alpha=0.7, s=25)

# 绘制Recall柱状图
plt.bar(2, recall_mean, yerr=recall_std, capsize=5, color='lightblue', label='Recall', edgecolor='black', alpha=0.7, width=0.35)
plt.errorbar(2, recall_mean, yerr=recall_std, fmt='none', ecolor='red', capsize=5, capthick=2, elinewidth=3)
plt.scatter(np.repeat(2, 10), recall, color='black', marker='o', alpha=0.7, s=25)

# 绘制mAP0.5柱状图
plt.bar(3, map_05_mean, yerr=map_05_std, capsize=5, color='mediumturquoise', label='mAP0.5', edgecolor='black', alpha=0.7, width=0.35)
plt.errorbar(3, map_05_mean, yerr=map_05_std, fmt='none', ecolor='red', capsize=5, capthick=2, elinewidth=3)
plt.scatter(np.repeat(3, 10), map_05, color='black', marker='o', alpha=0.7, s=25)

# 绘制mAP@[0.5:0.95]柱状图
plt.bar(4, map_095_mean, yerr=map_095_std, capsize=5, color='gold', label='mAP@[0.5:0.95]', edgecolor='black', alpha=0.7, width=0.35)
plt.errorbar(4, map_095_mean, yerr=map_095_std, fmt='none', ecolor='red', capsize=5, capthick=2, elinewidth=3)
plt.scatter(np.repeat(4, 10), map_095, color='black', marker='o', alpha=0.7, s=25)

# 设置标签和标题
plt.xticks([1, 2, 3, 4], ['Precision', 'Recall', 'mAP0.5', 'mAP@[0.5:0.95]'], fontsize=14, weight='bold')
plt.ylabel('Scores (%)', fontsize=14, weight='bold')
plt.title('Experiment Results with Confidence Intervals', fontsize=16, weight='bold')

# 设置纵轴范围
plt.ylim(65, 95)

# 添加图例
plt.legend(fontsize=12)

# 显示图表
plt.tight_layout()
plt.show()
