import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Meshgrid for vectors
x, y = np.meshgrid(np.linspace(-10, 10, 20),
				np.linspace(-10, 10, 20))

# Meshgrid for colors
xc, yc = np.meshgrid(np.linspace(-10, 10, 100),
				np.linspace(-10, 10, 100))

scaled_kwargs = {'scale_units':'xy', 'scale':1, 'angles':'xy'}
default_kwargs = {'scale_units':None, 'scale':None, 'angles':'uv'}

# Inputs are the direction at each x, y point
def plot_vector_field(u, v, zc=None, kwargs=default_kwargs, x=x, y=y, xc=xc, yc=yc, figure=None, cbar=True):
    # Creating figure

    if figure is None:
        fig, ax = plt.subplots(figsize=(10,8))
    else:
        fig = figure[0]
        ax = figure[1]

    # If color input is not None, plot the color map
    if(zc is not None):
        cmap = cm.spring
        cs = ax.pcolor(xc, yc, zc, cmap=cmap)
        if cbar:
            cbar = fig.colorbar(cs, ax=ax, label=r'$\sqrt{v_x^2 + v_y^2}$')

    # Plot the arrows using quiver
    plt.quiver(x, y, u, v, color='black', **kwargs)
    plt.scatter(x,y, color='blue', marker='x')
    plt.title('Vector Field')
    plt.xlabel('x')
    plt.ylabel('y')

    # Setting x, y boundary limits
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    # Show plot with grid
    plt.grid()
    # plt.show()

# Plot 3D line by giving 3D coordinates
def plot_3D_line(xline, yline, zline):
    # 3D projection
    fig = plt.figure(figsize=(8,8))
    ax = plt.axes(projection='3d')
    ax.set_box_aspect(aspect=None, zoom=0.94)

    # Data for 3D lines
    ax.plot(xline, yline, zline)

    plt.xlabel('x')
    plt.ylabel('y')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()