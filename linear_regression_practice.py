from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

df = pd.DataFrame({'demographic': ['African American', 'African American women', 'Hispanic/Latinx',
                                   'Asian', 'Native', 'LGBTQ', 'disabled', 'women', 'Hawaiian/ PI', 'veteran', 'African American men', 'other'],
                   'grants': [56, 1, 35, 3, 16, 10, 22, 85, 13, 16, 1, 1700],
                   'stem_grants': [4, 1, 4, 0, 0, 1, 2, 8, 1, 2, 0, 600]})

demo_df = pd.get_dummies(df, columns=['demographic'])

X = df[['grants']]
y = df['stem_grants']

reg = LinearRegression()

reg.fit(X, y)

#residuals = np.array(reg._residues)
#plt.scatter(x=range(len(residuals)), y=residuals)
# plt.show()

# Select the first column of the X dataframe
X_col = X.iloc[:, 0]

# Calculate the correlation coefficient between the first column of the X dataframe and the y array. So the corr coefficient of demographic and stem grants
corr, pval = pearsonr(X_col, y)

predictions = reg.predict(X)

df['predicted_stem_grants'] = predictions


def predict_stem_grants_percent(predicted_stem_grants, grants):
    # Calculate the percentage of stem grants
    stem_grants_percent = predicted_stem_grants / grants * 100

    # Return the percentage of stem grants
    return stem_grants_percent


# Apply the predict_stem_grants_percent function to the df DataFrame
df['predicted_stem_grants_percent'] = df.apply(lambda row: predict_stem_grants_percent(
    row['predicted_stem_grants'], row['grants']), axis=1)

# First, find the minimum value in the series
min_value = df['predicted_stem_grants'].min()

# Add the minimum value to all the values in the series
df['predicted_stem_grants'] = df['predicted_stem_grants'] + abs(min_value)

# Calculate the sum of all the values in the series
total = df['predicted_stem_grants'].sum()

# Divide each value in the series by the sum of all the values
df['predicted_stem_grants_total'] = df['predicted_stem_grants'] / total

# The resulting values should be between 0 and 1
print(df['predicted_stem_grants_total'])


# Create a figure and an axis
fig, ax = plt.subplots()

# Set the x-axis tick labels to be the values in the index
ax.set_xticklabels(df['demographic'], fontsize=7, rotation=90, ha='right')

plt.xticks(range(len(df)), df['demographic'])


# Use the `bar` function to plot the values in the `predicted_stem_grants` column as a bar graph
ax.bar(range(len(df)), df['predicted_stem_grants_total'])

# Show the plot
plt.show()


print(corr)
print(df)
print(X.shape)
print(y.shape)
print(reg.coef_)
print(reg.intercept_)
