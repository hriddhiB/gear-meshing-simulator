import numpy as np


def gear_ratio(teeth1, teeth2):

    return teeth2 / teeth1


def generate_gear(radius, teeth, center=(0,0), rotation=0):

    theta = np.linspace(0, 2*np.pi, 200)

    x_circle = center[0] + radius*np.cos(theta)
    y_circle = center[1] + radius*np.sin(theta)

    teeth_shapes = []

    tooth_angle = 2*np.pi / teeth

    for i in range(teeth):

        angle = i*tooth_angle + rotation

        a1 = angle - tooth_angle/3
        a2 = angle
        a3 = angle + tooth_angle/3

        r_inner = radius
        r_outer = radius*1.18

        x = [
            center[0] + r_inner*np.cos(a1),
            center[0] + r_outer*np.cos(a2),
            center[0] + r_inner*np.cos(a3),
            center[0] + r_inner*np.cos(a1)
        ]

        y = [
            center[1] + r_inner*np.sin(a1),
            center[1] + r_outer*np.sin(a2),
            center[1] + r_inner*np.sin(a3),
            center[1] + r_inner*np.sin(a1)
        ]

        teeth_shapes.append((x,y))

    return x_circle, y_circle, teeth_shapes