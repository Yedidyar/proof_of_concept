def trajectory_calculator(velocity, angle):
    """
    function given velocity and angle and returned:
    max height of the object,
    the end loction object from the beginning,
    time till landing
    """

    import math
    from scipy.constants import g

    # y = h + xtan(α) - gx²/2V₀²cos²(α)
    # I am spliting the equation. 'b' represent the  first part
    #  c the part of divsion and 'a' the -g
    b = (math.tan(math.radians(angle)))
    c = (2*(velocity**2))*(math.cos(math.radians(angle)))**2
    a = - (g/c)

    # solving using quadratic formula
    d = (b**2) - (4*a)
    solution1 = (-b-math.sqrt(d))/(2*a)
    solution2 = (-b+math.sqrt(d))/(2*a)

    # time in the air formula
    total_time = ((2*velocity*math.sin(math.radians(angle)))/g)

    # maximum height of the object formula
    h = ((velocity**2)*(math.sin(math.radians(angle))**2))/(2*g)

    # format to 1 digit after decimel point and Attach units of measure
    h = "{:.1f} {}".format(h, 'm')
    solution1 = "{:.1f} {}".format(solution1, 'm')
    total_time = "{:.1f} {}".format(total_time, 'sec')

    return h, solution1, total_time
