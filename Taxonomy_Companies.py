import pandas as pd
from pandas.api.types import CategoricalDtype
import seaborn as sns
import matplotlib.pyplot as plt
#sns.set_theme(style="whitegrid")


pd.set_option('display.max_columns', None)

companies_data = [{'Company Name': 'TikTok', 'UI Design & Accessibility': 'P-D',
                   'Community Guidelines and Policies': 'GISOIM',
                   'Content Moderation Practices': 'HAC'},
                  {'Company Name': 'YouTube', 'UI Design & Accessibility': 'NP',
                   'Community Guidelines and Policies': 'GISO',
                   'Content Moderation Practices': 'HAC'},
                  {'Company Name': 'Facebook', 'UI Design & Accessibility': 'P-D',
                   'Community Guidelines and Policies': 'GISO',
                   'Content Moderation Practices': 'HAC'},
                  {'Company Name': 'Twitter', 'UI Design & Accessibility': 'NP',
                   'Community Guidelines and Policies': 'GISOIM',
                   'Content Moderation Practices': 'HAC'},
                  {'Company Name': 'X', 'UI Design & Accessibility': 'NP',
                   'Community Guidelines and Policies': 'GISO',
                   'Content Moderation Practices': 'HAC'},
                  {'Company Name': 'Zoom', 'UI Design & Accessibility': 'P-D',
                   'Community Guidelines and Policies': 'GISO',
                   'Content Moderation Practices': 'HAC'},
                  {'Company Name': 'Instagram', 'UI Design & Accessibility': 'P-D',
                   'Community Guidelines and Policies': 'GISO',
                   'Content Moderation Practices': 'HAC'},
                  {'Company Name': 'Github', 'UI Design & Accessibility': 'P-D',
                   'Community Guidelines and Policies': 'GISOIM',
                   'Content Moderation Practices': 'M'}]

companies = pd.DataFrame(columns=['Company Name', 'UI Design & Accessibility',
                                  'Community Guidelines and Policies', 'Content Moderation Practices'],
                         data=companies_data)

cat_types_x = CategoricalDtype(categories=['NP', 'GI', 'GISO', 'GISOIM'], ordered=True)
cat_types_y = CategoricalDtype(categories=['P-D', 'P-T', 'P-B', 'NP'], ordered=True)

companies['Community Guidelines and Policies'] = companies['Community Guidelines and Policies'].astype(cat_types_x)
companies['UI Design & Accessibility'] = companies['UI Design & Accessibility'].astype(cat_types_y)
companies['Content Moderation Practices'] = companies['Content Moderation Practices'].astype('category')
# taxonomy_plot = sns.stripplot(data=companies, x= 'Community Guidelines and Policies', y='UI Design & Accessibility', hue= 'Content Moderation Practices')


g = sns.catplot(x="Community Guidelines and Policies", y="UI Design & Accessibility",
                col="Content Moderation Practices", data=companies, kind="strip", height=4, dodge=True, size = 7,
                hue='Company Name', edgecolor="gray")

plt.show()
print(companies.dtypes)
print(companies)
