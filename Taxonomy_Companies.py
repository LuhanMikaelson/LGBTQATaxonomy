import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#sns.set_theme(style="whitegrid")


pd.set_option('display.max_columns', None)

companies_data = [{'Company Name': 'TikTok', 'UI Design & Accessibility': 3,
                   'Community Guidelines and Policies': 3,
                   'Content Moderation Practices': 4},
                  {'Company Name': 'YouTube', 'UI Design & Accessibility': 0,
                   'Community Guidelines and Policies': 2,
                   'Content Moderation Practices': 4},
                  {'Company Name': 'Facebook', 'UI Design & Accessibility': 3,
                   'Community Guidelines and Policies': 2,
                   'Content Moderation Practices': 4},
                  {'Company Name': 'Twitter', 'UI Design & Accessibility': 0,
                   'Community Guidelines and Policies': 3,
                   'Content Moderation Practices': 4},
                  {'Company Name': 'X', 'UI Design & Accessibility': 0,
                   'Community Guidelines and Policies': 2,
                   'Content Moderation Practices': 4},
                  {'Company Name': 'Zoom', 'UI Design & Accessibility': 3,
                   'Community Guidelines and Policies': 2,
                   'Content Moderation Practices': 4},
                  {'Company Name': 'Instagram', 'UI Design & Accessibility': 3,
                   'Community Guidelines and Policies': 2,
                   'Content Moderation Practices': 4},
                  {'Company Name': 'Github', 'UI Design & Accessibility': 3,
                   'Community Guidelines and Policies': 3,
                   'Content Moderation Practices': 5}]

companies = pd.DataFrame(columns=['Company Name', 'UI Design & Accessibility',
                                  'Community Guidelines and Policies', 'Content Moderation Practices'],
                         data=companies_data)
plt.figure(figsize = (5, 4))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(companies['UI Design & Accessibility'], companies['Community Guidelines and Policies'],
             companies['Content Moderation Practices'])
ax.set_xlabel('UI Design & Accessibility')
ax.set_ylabel('Community Guidelines and Policies')
ax.set_zlabel('Content Moderation Practices')
ax.set_zticks([ 0, 1, 2, 3, 4, 5, 6])
plt.show()


print(companies.dtypes)
print(companies)
