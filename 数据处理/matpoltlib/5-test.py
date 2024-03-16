import matplotlib.pyplot as mp

locators = ['mp.NullLocator()',
            'mp.MaxNLocator(nbins=4)',
            'mp.FixedLocator([x for x in range(11) if x%2==0])',
            'mp.AutoLocator()']
mp.figure('Test', facecolor='lightgray')
for i, locator in enumerate(locators):
    mp.subplot(len(locators), 1, i + 1)
    mp.xlim(0, 10)
    ax = mp.gca()
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position(('data', 0.5))
    mp.yticks([])
    loc = eval(locator)
    ax.xaxis.set_major_locator(loc)
    ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))

mp.show()
