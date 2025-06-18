import matplotlib.colors
import matplotlib.pyplot as plt


plt.style.use("FST.mplstyle")

colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

color_map = matplotlib.colors.get_named_colors_mapping()

colornames = ["blue","yellow","red","lightgreen","grey","green","orange"]
for idx in range(len(colornames)):
    color_map[colornames[idx]] = colors[idx]

