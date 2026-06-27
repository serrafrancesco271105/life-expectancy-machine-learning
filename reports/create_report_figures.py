from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "reports" / "figures_report"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# -----------------------------
# Load data
# -----------------------------
final_model_dataset = pd.read_csv(
    DATA_DIR / "final_absolute_healthcare_environment_model_dataset.csv"
)

model_audit = pd.read_csv(DATA_DIR / "model_audit.csv")

feature_importance_audit = pd.read_csv(
    DATA_DIR / "feature_importance_audit.csv"
)


# -----------------------------
# Global plot style
# -----------------------------
plt.rcParams.update({
    "figure.figsize": (9, 5.5),
    "figure.dpi": 120,
    "savefig.dpi": 300,
    "font.size": 11,
    "axes.titlesize": 15,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "grid.linestyle": "--",
})


MAIN_COLOR = "#1f77b4"
SECONDARY_COLOR = "#4c78a8"
ACCENT_COLOR = "#2ca02c"
TEXT_COLOR = "#333333"


def save_figure(filename: str):
    output_path = OUTPUT_DIR / filename
    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# -----------------------------
# 1. GDP per capita vs life expectancy
# -----------------------------
plt.figure()

plt.scatter(
    final_model_dataset["gdp_per_capita"],
    final_model_dataset["life_expectancy"],
    alpha=0.75,
    s=42,
    color=MAIN_COLOR,
    edgecolor="white",
    linewidth=0.4,
)

plt.title("GDP per Capita vs Life Expectancy", color=TEXT_COLOR)
plt.xlabel("GDP per capita")
plt.ylabel("Life expectancy")
save_figure("01_gdp_vs_life_expectancy.png")


# -----------------------------
# 2. Log GDP per capita vs life expectancy
# -----------------------------
plot_data = final_model_dataset[
    final_model_dataset["gdp_per_capita"] > 0
].copy()

plot_data["log_gdp_per_capita"] = np.log10(plot_data["gdp_per_capita"])

plt.figure()

plt.scatter(
    plot_data["log_gdp_per_capita"],
    plot_data["life_expectancy"],
    alpha=0.75,
    s=42,
    color=MAIN_COLOR,
    edgecolor="white",
    linewidth=0.4,
)

plt.title("Log GDP per Capita vs Life Expectancy", color=TEXT_COLOR)
plt.xlabel("Log10 GDP per capita")
plt.ylabel("Life expectancy")
save_figure("02_log_gdp_vs_life_expectancy.png")


# -----------------------------
# 3. Air pollution vs life expectancy
# -----------------------------
plt.figure()

plt.scatter(
    final_model_dataset["air_pollution"],
    final_model_dataset["life_expectancy"],
    alpha=0.75,
    s=42,
    color=MAIN_COLOR,
    edgecolor="white",
    linewidth=0.4,
)

plt.title("PM2.5 Air Pollution vs Life Expectancy", color=TEXT_COLOR)
plt.xlabel("PM2.5 air pollution")
plt.ylabel("Life expectancy")
save_figure("03_air_pollution_vs_life_expectancy.png")


# -----------------------------
# 4. Model comparison by R squared
# -----------------------------
plt.figure(figsize=(10, 5.5))

bars = plt.bar(
    model_audit["Model_ID"],
    model_audit["R_squared"],
    color=SECONDARY_COLOR,
)

plt.title("Model Comparison by R²", color=TEXT_COLOR)
plt.xlabel("Model")
plt.ylabel("R²")
plt.ylim(0, 1)

for bar, value in zip(bars, model_audit["R_squared"]):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.025,
        f"{value:.3f}",
        ha="center",
        va="bottom",
        fontsize=9,
        color=TEXT_COLOR,
    )

save_figure("04_model_comparison_r2.png")


# -----------------------------
# 5. Model comparison by MAE
# -----------------------------
plt.figure(figsize=(10, 5.5))

bars = plt.bar(
    model_audit["Model_ID"],
    model_audit["MAE_years"],
    color=SECONDARY_COLOR,
)

plt.title("Model Comparison by Mean Absolute Error", color=TEXT_COLOR)
plt.xlabel("Model")
plt.ylabel("MAE in years")

for bar, value in zip(bars, model_audit["MAE_years"]):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.08,
        f"{value:.2f}",
        ha="center",
        va="bottom",
        fontsize=9,
        color=TEXT_COLOR,
    )

save_figure("05_model_comparison_mae.png")


# -----------------------------
# 6. M9 feature importance
# -----------------------------
m9_importance = feature_importance_audit[
    feature_importance_audit["Model_ID"] == "M9"
].sort_values("Importance", ascending=True)

plt.figure(figsize=(9, 5.5))

plt.barh(
    m9_importance["Feature"],
    m9_importance["Importance"],
    color=ACCENT_COLOR,
)

plt.title("M9 Feature Importance", color=TEXT_COLOR)
plt.xlabel("Importance")
plt.ylabel("Feature")

for index, value in enumerate(m9_importance["Importance"]):
    plt.text(
        value + 0.01,
        index,
        f"{value:.3f}",
        va="center",
        fontsize=9,
        color=TEXT_COLOR,
    )

plt.xlim(0, max(m9_importance["Importance"]) + 0.12)

save_figure("06_m9_feature_importance.png")


print("\nAll report figures created successfully.")
