import math
import mymath
import matplotlib.pyplot as plt
from matplotlib.patheffects import PathPatchEffect, SimpleLineShadow, Normal

plt.style.use('dark_background')

t = input("mobile or desktop wallpaper? m/d").lower()

colors = [
    'lime', 'aqua', 'blue', 'crimson', 'darkviolet', 'aquamarine', 'yellow',
    'cyan', 'orange', 'mediumspringgreen', 'blueviolet', 'white', 'deepskyblue',
    'lawngreen', 'royalblue', 'violet'
]

iarr = []
# number of calcs per int change
precision = 1000
# to either side
r = 3
bv = 0 - r
bv = bv * precision
tv = r * precision

for x in range(bv, tv, 1):
    iarr.append(x / precision)


def makeplotarray(func):
    global iarr
    global t
    tr = []
    for i in iarr:
        try:
            ifr = func(i)
            # add to plot array
            if ifr < r * 16 / 9 and ifr > -(r * 16 / 9):
                tr.append(tuple([i, ifr]))
        except:
            # dont add, math error
            pass

    return tr


# lnames = ['acos', 'asin', 'atan', 'acosh', 'asinh', 'atanh', 'cos', 'sin', 'tanh', 'asec', 'acsc', 'acot', 'asech', 'acsch', 'acoth', 'sech']

results = []
results.append(makeplotarray(math.acos))
results.append(makeplotarray(math.asin))
results.append(makeplotarray(math.atan))

results.append(makeplotarray(math.acosh))
results.append(makeplotarray(math.asinh))
results.append(makeplotarray(math.atanh))

results.append(makeplotarray(math.cos))
results.append(makeplotarray(math.sin))

results.append(makeplotarray(math.tanh))

results.append(makeplotarray(mymath.asec))
results.append(makeplotarray(mymath.acsc))
results.append(makeplotarray(mymath.acot))

results.append(makeplotarray(mymath.asech))
results.append(makeplotarray(mymath.acsch))
results.append(makeplotarray(mymath.acoth))

results.append(makeplotarray(mymath.sech))

# results.append(makeplotarray(math.tan))
# results.append(makeplotarray(math.sinh))
# results.append(makeplotarray(math.cosh))
# results.append(makeplotarray(mymath.csch))
# results.append(makeplotarray(mymath.coth))
# results.append(makeplotarray(mymath.sec))
# results.append(makeplotarray(mymath.csc))
# results.append(makeplotarray(mymath.cot))

for a in range(len(results)):
    # print(a)
    plt.plot(*zip(*results[a]), color=colors[a], path_effects=[
             SimpleLineShadow(shadow_color=colors[a], linewidth=6), Normal()])

plt.grid(False)
plt.axis('off')
if t == "m":
    plt.gcf().set_size_inches(10.8, 24.0)
else:
    plt.gcf().set_size_inches(19.2, 10.8)
plt.savefig(f"{t}_wallpaper.png", bbox_inches="tight", dpi=500, pad_inches=0)
plt.show()
