def trajectory_calculator(velocity, angle):
    """
    function given velocity and angle and returned:
    max height of the object,
    the end loction object from the beginning,
    time till landing
    """

    import math
    from scipy.constants import g

    if velocity != 0:
        # horizontal_distance = V₀²sin(2α)/g
        horizontal_distance = ((velocity**2)) * \
            ((math.sin(math.radians(2*angle))))/g

        # time in the air formula
        total_time = ((2*velocity*math.sin(math.radians(angle)))/g)

        # maximum height of the object formula
        h = ((velocity**2)*(math.sin(math.radians(angle))**2))/(2*g)
    else:
        h = 0
        horizontal_distance = 0
        total_time = 0

    # format to 2 digit after decimel point and Attach units of measure
    h = "{:.2f} {}".format(h, 'm')
    horizontal_distance = "{:.2f} {}".format(horizontal_distance, 'm')
    total_time = "{:.2f} {}".format(total_time, 'sec')

    return h, horizontal_distance, total_time
