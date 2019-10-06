import matplotlib.pyplot as plt


def my_bar_chart(title, x_label, y_label, x_list, y_list):
    """
    plot a bar chart
    title: str
        the title of the graph
    x_label: str
        the labels of the x axis
    y_label: str
        the labels of the y axis
    x_tuples: list
        values to be displayed in x axis, normally str here
    y_tuples: list
        values to be displayed in y axis
    """
    plt.bar(x_list, y_list)  # plot the bar

    bias_x, bias_y = 0.08, 0.1
    for x, y in zip(range(len(x_list)), y_list):
        plt.text(x, y, "%.2f" % y, ha='center', va='bottom')

    # adjust the display range
    plt.ylim((min(y_list) * 0.8, max(y_list) * 1.2))

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.title(title)
    plt.show()

