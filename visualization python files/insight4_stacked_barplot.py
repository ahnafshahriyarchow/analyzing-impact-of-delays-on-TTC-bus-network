#DIVYANSH AGRAWAL
#Ahnaf Shahriyar Chowdhury

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('cleaned_ttc_bus_delay_data.xlsx')
route_incident_delay = df.groupby(['Route', 'Incident'])['Min Delay'].sum().unstack().fillna(0)

top_10_routes = route_incident_delay.sum(axis=1).sort_values(ascending=False).head(10).index
top_10_route_incident_delay = route_incident_delay.loc[top_10_routes]
fig, ax = plt.subplots(figsize=(16, 8))
top_10_route_incident_delay.plot(kind='bar', stacked=True, figsize=(16, 8), colormap='Set3', ax=ax)

ax.set_title('Total Delays by Route and Incident Type (Top 10 Routes)', fontsize=16)
ax.set_xlabel('Route', fontsize=12)
ax.set_ylabel('Total Min Delay (Minutes)', fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.legend(title="Incident Types", loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
plt.tight_layout()
plt.show()
