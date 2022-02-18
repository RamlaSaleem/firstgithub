# steps invloved in data visualization
# step-1 import liabraries
import seaborn as sns
import matplotlib.pyplot as plt

# step-2 set a theme
sns.set_theme(style="ticks", color_codes=True)

# stpe-3 import data set, you can also imprt your own data
kashti = sns.load_dataset("titanic")
#print(kashti)

# #step-4 plot basic graph with 2 varibale (count plot)
p = sns.countplot(x="sex", data=kashti, hue="class")
p.set_title("Baba_aammar ka count plot for kashti")
plt.show()
