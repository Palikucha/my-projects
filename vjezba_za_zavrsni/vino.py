import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

white_wine = pd.read_csv("https://www.kaggle.com/datasets/danielpanizzo/wine-quality?select=wineQualityWhites.csv")
red_wine = pd.read_csv("https://www.kaggle.com/datasets/danielpanizzo/wine-quality?select=wineQualityReds.csv")

white_correlations = white_wine.corr()["density"].sort_values()
red_correlations = red_wine.corr()["density"].sort_values()

max_white_corr = white_correlations.idxmax() if abs(white_correlations.max()) > abs(white_correlations.min()) else white_correlations.idxmin()

max_red_corr = red_correlations.idxmax() if abs(red_correlations.max()) > abs(red_correlations.min()) else red_correlations.idxmin()

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.hist(white_wine[max_white_corr], bins=20, color="lightgrey")
plt.title("Histogram of " + max_white_corr + " in White wine")
plt.xlabel(max_white_corr)
plt.ylabel("Frequency")

plt.subplot(1,2,2)
plt.hist(red_wine[max_red_corr], bins=20, color="Darkred")
plt.title("Histogram of " + max_red_corr + " in Red wine")
plt.xlabel(max_red_corr)
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

print("Najveća korelacija s gustoćom za bijelo vino je parametar", max_white_corr, "s vrijednošću:", red_correlations[max_red_corr])