import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
points = np.array([[0,0], [1,0], [0.5, np.sqrt(1-0.5*0.5)]])
new_points = np.array([[0.1, 0.1]])

for i in range(500000):
    chosen_point = points[np.random.choice(points.shape[0])]
    new_points = np.vstack([new_points, [(chosen_point[0] + new_points[-1][0]) / 2, (chosen_point[1] + new_points[-1][1]) / 2]])

ax.plot(points[:, 0], points[:, 1], 'k,', markersize=1)
ax.plot(new_points[:, 0], new_points[:, 1], 'k,', markersize=1)
fig.savefig("sierpinski.png", dpi=400)