import matplotlib.pyplot as plt


if __name__ == "__main__":
    coords = [198.760,310.410,265.200,257.120,262.390,253.610,195.940,306.900,266.260,262.040,272.570,248.330,257.820,251.510]
    coords = [(coords[i], coords[i+1]) for i in range(0, len(coords), 2)]
    ax = plt.gca()
    ax.set_xlim([0, 960])
    ax.set_ylim([0, 540])
    for x, y in coords:
        plt.plot(x, y, 'bo')
    plt.show()
