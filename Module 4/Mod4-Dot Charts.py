import pandas as pd
import matplotlib.pyplot as plt

# Load the new dataset
data = pd.read_csv('constituents.csv')

# Dot chart for the number of companies per GICS Sector
sector_counts = data['GICS Sector'].value_counts()

# Plot the count of companies in each GICS Sector
plt.plot(sector_counts, 'o', alpha=0.7)
plt.title('Dot Chart: Number of Companies in Each Sector')
plt.xlabel('Sector Index')
plt.ylabel('Number of Companies')
plt.xticks(rotation=90)  # Rotate the x-axis labels for better visibility
plt.show()
