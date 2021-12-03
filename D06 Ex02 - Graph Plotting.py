def graph_plotting (x):
    return int(4 * int(x)**2 - 12)
x = int(input("x :"))
if int(x) > 0:
    x = -x
    for gp in range(x, -(x-1)):
        x = int(gp)
        graph_plotting(x)
        print("(" + str(x) + "),(" + str(graph_plotting (x)) + ")")
else:
    for gp in range(x, -(x-1)):
        x = int(gp)
        graph_plotting(x)
        print("(" + str(x) + "),(" + str(graph_plotting (x)) + ")")