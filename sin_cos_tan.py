print("Importing modules...")
import math
import time
from matplotlib import pyplot as plt
import sys
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


degrees = int(input("For how many degrees do you want to see Sinus, Cosinus and Tangens?: "))
xLimit = int(input("Where do you want to limit the X coordinate? (5 is recommended): "))
xLimitPositive = xLimit
xLimitNegative = -(xLimit)
x = 0
sinusvalues = []
cosinusvalues = []
tangensvalues = []
xvalues = []


while x <= degrees:
    progress(x, degrees, status=" calculating Sinus, Cosinus and Tangens")
    sinusvalues.append(math.sin(math.radians(x)))
    cosinusvalues.append(math.cos(math.radians(x)))
    if math.tan(math.radians(x)) < xLimitPositive and math.tan(math.radians(x)) > xLimitNegative:
        tangensvalues.append(math.tan(math.radians(x)))
    else:
        if math.tan(math.radians(x)) < xLimitNegative:
            tangensvalues.append(xLimitNegative)
        elif math.tan(math.radians(x)) > xLimitPositive:
            tangensvalues.append(xLimitPositive)
    xvalues.append(math.radians(x))
    x = x + 5

plt.plot(xvalues,sinusvalues)
plt.plot(xvalues,cosinusvalues)
plt.plot(xvalues,tangensvalues)
plt.title('Functions: Sinus, Cosinus and Tangens')
plt.show()
