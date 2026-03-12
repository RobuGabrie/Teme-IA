import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
order_days = ["Thur", "Fri", "Sat", "Sun"]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

ax1 = axes[0, 0]
culori_sex = {"Male": "#1f77b4", "Female": "#d62728"}
for sex, color in culori_sex.items():
    subset = tips[tips["sex"] == sex]
    ax1.scatter(subset["total_bill"], subset["tip"], label=sex, alpha=0.75, c=color)
ax1.set_title("Scatter: total_bill vs tip")
ax1.set_xlabel("total_bill")
ax1.set_ylabel("tip")
ax1.legend(title="sex")

ax2 = axes[0, 1]
sns.boxplot(data=tips, x="day", y="total_bill", order=order_days, ax=ax2)
ax2.set_title("Boxplot total_bill per day")
ax2.set_xlabel("day")
ax2.set_ylabel("total_bill")

ax3 = axes[1, 0]
sns.histplot(data=tips, x="tip", hue="time", kde=True, ax=ax3)
ax3.set_title("Histograma tip cu hue=time si KDE")
ax3.set_xlabel("tip")
ax3.set_ylabel("count")

ax4 = axes[1, 1]
sns.barplot(data=tips, x="day", y="tip", order=order_days, errorbar="ci", ax=ax4)
ax4.set_title("Bacsis mediu per day")
ax4.set_xlabel("day")
ax4.set_ylabel("tip mediu")

plt.tight_layout()
plt.savefig("dashboard_tips.png", dpi=300, bbox_inches="tight")
print("Figura a fost salvata ca dashboard_tips.png")
