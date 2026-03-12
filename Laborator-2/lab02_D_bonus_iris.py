import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")

pair = sns.pairplot(iris, hue="species", diag_kind="kde")
pair.figure.suptitle("Pairplot Iris (hue=species)", y=1.02)
pair.savefig("iris_pairplot.png", dpi=300, bbox_inches="tight")

numeric_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

for ax, col in zip(axes, numeric_cols):
    sns.violinplot(
        data=iris,
        x="species",
        y=col,
        hue="species",
        split=False,
        dodge=False,
        legend=False,
        ax=ax,
    )
    ax.set_title(f"Violinplot {col}")
    ax.set_xlabel("species")
    ax.set_ylabel(col)
    ax.tick_params(axis="x", rotation=20)

fig.suptitle("Distributii Iris - Violinplot pe variabile numerice", y=1.05)
plt.tight_layout()
fig.savefig("iris_violinplots.png", dpi=300, bbox_inches="tight")

print("Figurile au fost salvate ca iris_pairplot.png si iris_violinplots.png")
