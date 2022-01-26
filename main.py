from planet import *
import turtle


REFRESH_RATE = 3  #refresh rate in number of days
TOTAL_TIME = 3 #time observed in number of years

D_TO_CENTRE_INITIAL = 150000000000 #initial distance to the central mass
DISTANCE_SCALE = 10**(-9) #distances are scaled down by this factor

V_MAGN_INITIAL = 35000 #initial speed in m/s


def createPlanet(name, d_to_centre_init, v_magn_init):
    #Initializing the properties (distance to centre, velocity,
    #acceleration) of the planet
    d_i = d_to_centre_init
    pos_i = (0, d_i)

    v = (v_magn_init, 0)

    a_magn_i = (G*M_CENTRE)/(d_i**2)
    a = (0, -a_magn_i)

    p = Planet(name, pos_i, v, a)

    return p


def main():

    #Creating and positioning the central mass
    central_turtle = turtle.Turtle()
    central_turtle.goto(0,0)

    #Creating the earth planet object and creating
    #the associated turtle
    earth = createPlanet('earth', D_TO_CENTRE_INITIAL, V_MAGN_INITIAL)
    earth_turtle = turtle.Turtle()
    
    earth_turtle.speed(10)

    #Moving the turtle to the appropriate initial position
    earth_turtle.penup()
    earth_turtle.goto(earth.pos[0]*DISTANCE_SCALE, earth.pos[1]*DISTANCE_SCALE)
    earth_turtle.pendown()
    

    for Day in range(0, 365*TOTAL_TIME, REFRESH_RATE):
        print("Day",Day,":")
        if Day!=0:
            earth.update_all(3600*24*REFRESH_RATE)
        print("Position:",earth.pos)
        print("Distance to sun:", earth.d)
        print("Velocity:", earth.v, "m/s (Magnitude:", math.sqrt(earth.v[0]**2 + earth.v[1]**2),"m/s)")
        print("Acceleration:", earth.a, "m/s^2 (Magnitude:", math.sqrt(earth.a[0] ** 2 + earth.a[1] ** 2), "m/s^2)")

        earth_turtle.goto(earth.pos[0]*DISTANCE_SCALE, earth.pos[1]*DISTANCE_SCALE)

main()
