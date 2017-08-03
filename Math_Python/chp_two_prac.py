from pylab import plot, show

# x_numbs = [1, 2, 3]
# y_numbs = [2, 4, 6]
# plot(x_numbs, y_numbs, marker='o')
# show()

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
years = range(2000, 2013)
plot(years, nyc_temp, marker='+')
show()
# left off on page 38