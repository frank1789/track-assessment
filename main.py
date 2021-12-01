import sys
import os

import matplotlib.pyplot as plt

from parser import ParseData


def compute_mean_variance_all(data: ParseData) -> tuple:
    """
        Compute mean, variance, std-dev
        return an tuple
        :var
        """
    mean, variance, std_dev = data.Speed.mean(), data.Speed.var(), data.Speed.std()
    return mean, variance, std_dev


def compute_mean_variance_single_lap(data: ParseData) -> list:
    """
    Compute mean, variance, std-dev
    return an array o dictionary for each lap
    :var
    """
    single_lap = [
        {
            "lap": 1,
            "mean": data.Speed[0:1970].mean(),
            "variance": data.Speed[0:1970].var(),
            "std-dev": data.Speed[0:1970].std(),
            "top-speed": max(data.Speed[0:1970]),
            "low-speed": min(data.Speed[0:1970])
        },
        {
            "lap": 2,
            "mean": data.Speed[1971:3943].mean(),
            "variance": data.Speed[1971:3943].var(),
            "std-dev": data.Speed[1971:3943].std(),
            "top-speed": max(data.Speed[1971:3943]),
            "low-speed": min(data.Speed[1971:3943])
        },
        {
            "lap": 3,
            "mean": data.Speed[3943:-1].mean(),
            "variance": data.Speed[3943:-1].var(),
            "std-dev": data.Speed[3943:-1].std(),
            "top-speed": max(data.Speed[3943:-1]),
            "low-speed": min(data.Speed[3943:-1])
        },
    ]

    return single_lap


if __name__ == '__main__':
    # path to the resource
    filename = os.getcwd() + "/Trackdata.csv"

    # import data
    data = ParseData()
    data.load_from_file(filename)

    # Access data as dataframe
    print(data.get_as_datadrame().head())

    # Try to compute average speed for all laps
    # very simple analysis extract only mean, variance and std-dev
    print("Speed average among 3 laps\n{}".format("-" * 79))
    mean, variance, std_dev = compute_mean_variance_all(data)
    print("mean: {:2.5}\tvariance: {:2.5}\t std-dev: {:2.5}".format(mean, variance, std_dev))
    print("max speed: {:2.5}\tmin speed: {:2.5}".format(max(data.Speed), min(data.Speed)))
    print("{}".format("-" * 79))

    # Try to compute average speed for each laps
    # very simple analysis extract only mean, variance and std-dev
    laps = compute_mean_variance_single_lap(data)
    print("lap:\n{}".format("-" * 79))
    for lap in laps:
        print("lap {}:".format(lap["lap"]))
        print("mean: {:2.5}\tvariance: {:2.5}\t std-dev: {:2.5}".format(lap["mean"], lap["variance"], lap["std-dev"]))
        print("max speed: {:2.5}\tmin speed: {:2.5}".format(lap["top-speed"], lap["low-speed"]))
        print("{}\n".format("-" * 79))

    # Use boxplot to show the result previous computed
    # in this case collect information about speed for each lap and plot information
    # seems that the boxplot graph reflect the previous results
    d = [data.Speed[0:1970], data.Speed[1971:3943], data.Speed[3943:-1]]
    fig, ax = plt.subplots()
    ax.set_title('Visual comparison average speed for 3 laps')
    ax.boxplot(d, 1)
    print("close the figure window to continue...")
    plt.show()

    ####################################################################################################################
    # Combine plots to show physical dimensions on track
    # lap 1
    fig_lap_one = plt.figure(1001, figsize=(10, 7))
    plt.title(u"Lap: {:2}/{}".format(1, 3))
    ax = plt.axes(projection="3d")
    ax.plot(data.GPSLatCoord[0:1970], data.GPSLongCoord[0:1970], 'gray', label="Track")
    scatter_plot = ax.scatter3D(data.GPSLatCoord[0:1970], data.GPSLongCoord[0:1970], data.Speed[0:1970],
                                c=data.Speed[0:1970], cmap='plasma', label="Speed")
    plt.colorbar(scatter_plot, label='Speed')
    plt.legend(loc="upper left")
    ax.set_xlabel("GPSLatCoord")
    ax.set_ylabel("GPSLongCoord")
    ax.set_zlabel("Speed")

    # lap 2
    fig_lap_two = plt.figure(1002, figsize=(10, 7))
    plt.title(u"Lap: {:2}/{}".format(2, 3))
    ax = plt.axes(projection="3d")
    ax.plot(data.GPSLatCoord[1971:3943], data.GPSLongCoord[1971:3943], 'gray', label="Track")
    scatter_plot = ax.scatter3D(data.GPSLatCoord[1971:3943], data.GPSLongCoord[1971:3943], data.Speed[1971:3943],
                                c=data.Speed[1971:3943], cmap='plasma', label="Speed")
    plt.colorbar(scatter_plot, label='Speed')
    plt.legend(loc="upper left")
    ax.set_xlabel("GPSLatCoord")
    ax.set_ylabel("GPSLongCoord")
    ax.set_zlabel("Speed")

    # lap 3
    fig_lap_three = plt.figure(1003, figsize=(10, 7))
    plt.title(u"Lap: {:2}/{}".format(3, 3))
    ax = plt.axes(projection="3d")
    ax.plot(data.GPSLatCoord[3943:-1], data.GPSLongCoord[3943:-1], 'gray', label="Track")
    scatter_plot = ax.scatter3D(data.GPSLatCoord[3943:-1], data.GPSLongCoord[3943:-1], data.Speed[3943:-1],
                                c=data.Speed[3943:-1], cmap='plasma', label="Speed")
    plt.colorbar(scatter_plot, label='Speed')
    plt.legend(loc="upper left")
    ax.set_xlabel("GPSLatCoord")
    ax.set_ylabel("GPSLongCoord")
    ax.set_zlabel("Speed")
    print("close all the figure window to continue...")
    plt.show()

    ####################################################################################################################
    # Animation on lap
    # show the car's position on track, added notation about speed(v), steer(s), brake force(b)
    # track change color and line for each lap
    for i in range(0, len(data.LapDistance)):
        # plot
        plt.cla()
        plt.title(u"Lap: {:2}/{}".format(int(data.LapNumber[i]), int(max(data.LapNumber))))
        if data.LapNumber[i] == 1.0:
            plt.plot(data.GPSLatCoord[0:1970], data.GPSLongCoord[0:1970], "-", c="gray", label="Track Lap 1")
        if data.LapNumber[i] == 2.0:
            plt.plot(data.GPSLatCoord[1971:3943], data.GPSLongCoord[1971:3943], "-", c="gray", label="Track Lap 2")
        if data.LapNumber[i] == 3.0:
            plt.plot(data.GPSLatCoord[3943:-1], data.GPSLongCoord[3943:-1], "-", c="gray", label="Track Lap 3")

        plt.plot(data.GPSLatCoord[i], data.GPSLongCoord[i], ".r", label="Car")
        plt.text(data.GPSLatCoord[i], data.GPSLongCoord[i], "v: {:1.2} s: {:1.2} b: {:1.2}".format(
            data.Speed[i],
            data.Steer[i],
            data.BrakeForce[i],
        ), horizontalalignment='right')
        plt.axis("equal")
        plt.grid(True)

        plt.legend(loc="upper left")
        plt.pause(0.0001)

    sys.exit(0)
