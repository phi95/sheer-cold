import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style



style.use('fivethirtyeight')

fig = plt.figure()
'''
plt.xlabel('Time (s)')
plt.ylabel('Temperature (F)')
plt.title("Your drink's current temperature")
'''
ax1 = fig.add_subplot(1,1,1)
fig.subplots_adjust(bottom=0.1)




def animate(i):
    ax1.set_ylabel('what')
    ax1.set_title('hi')

    graph_data = open('plot.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.set_ylabel("Temperature (F)")
    ax1.set_title("Drink Temperatures")
    ax1.set_xlabel("Time (s)")
    ax1.plot(xs,ys)

ani = animation.FuncAnimation(fig, animate,  interval=1000)

plt.show()
