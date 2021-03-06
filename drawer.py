from math import pi

import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider


N = 512


def draw_plots(title, signal, params_builder, variable_parameter):
    for parameter_value in variable_parameter:
        plt.plot(list(signal(params_builder(parameter_value), N)), label='${}={}$'.format(title, round(parameter_value, 2)))
    plt.legend(loc='center left')


def draw_plot(signal, params):
    plt.plot(list(signal(params, N)))


def draw_polyharmonic(signal, params):
    def update(_):
        phases = list(map(lambda x: x.val, sliders))
        new_params = [x._replace(**{'phase':phases[i]}) for i, x in enumerate(params)]
        plot.set_ydata(list(signal(new_params, N)))

    def reset(_):
        for slider in sliders:
            slider.reset()

    fig = plt.figure()
    plt.subplots_adjust(bottom=0.3)

    plot, = plt.plot(list(signal(params, N)))
    plt.ylim([-5, 5])

    resetax = plt.axes([0.8, 0.025, 0.1, 0.03])
    button = Button(resetax, 'Reset')
    button.on_clicked(reset)

    sliders = []
    for i, param in enumerate(params):
        axes = plt.axes([0.17, 0.1+i*0.03, 0.65, 0.01])
        slider = Slider(axes, '$f={}$'.format(param.frequency), 0, pi*2, valinit=param.phase, valfmt=r'$\phi=%1.2f$')
        slider.on_changed(update)
        sliders.append(slider)

    return sliders + [button]
