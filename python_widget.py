from tkinter import *
import math

zipline = Tk()
zipline.title('Zipline Calculator')
grav= 9.81

def Velocity():

    distance=float(distance_entry.get())
    length=float(distance*(0.305))  ##convert ft into meters

    angle=float(angle_entry.get()) 
    theta=float(math.radians(angle))    ##convert degrees into radians
    

    Final_speed= math.sqrt(2*grav*(math.sin(theta))*length) ##equation for final speed
    Fspeed_mph= (Final_speed*2.237) ## convert m/s to mph
    Felev= distance*math.tan(theta) ## calc elevation drop
    
## Clear previous values
    blank_ang.delete(0, END)
    blank_speed.delete(0, END)
    blank_elev.delete(0, END)
## Display output for Veocity function 
    blank_ang.insert(0, angle)
    blank_speed.insert(0,Fspeed_mph)
    blank_elev.insert(0, Felev)

def Ang_Degree():
    distance=float(distance_entry.get())
    length=(distance*(0.305))   ##convert ft into meters

    f_speed=float(speed_entry.get())
    speed=float((f_speed*0.447))    ##convert mph into m/s

    Final_angle=math.asin((speed**2)/(2*grav*length))   ##equation for final angle
    Fangle_deg = math.degrees(Final_angle)  ##convert radians to degrees
    Felev= distance*math.tan(Final_angle)   ##calc elevation drop

## Clear previous values
    blank_ang.delete(0, END)
    blank_speed.delete(0, END)
    blank_elev.delete(0, END)
## Display output for Ang_Degree function 
    blank_ang.insert(0, Fangle_deg)
    blank_speed.insert(0,f_speed)
    blank_elev.insert(0, Felev)


top_frame =  Frame(zipline)
top_frame.pack()

## Establishing Labels
welcome_label = Label(top_frame, text='Welcome the the Zipline Calculator')
distance_label = Label(top_frame, text='Distance of the Zipline(ft):')
angle_label = Label(top_frame, text='Angle Desired(deg):')
speed_label = Label(top_frame, text='Final Speed Desired(mph):')
need_label = Label(top_frame, text="Parameter's Needed:")
needang_label= Label(top_frame, text='Angle:')
needspeed_label= Label(top_frame, text='Final Speed:')
mph_label= Label(top_frame, text='mph')
deg_label= Label(top_frame, text='degrees')
elev_label= Label(top_frame, text= 'Elevation drop')
ft_label= Label(top_frame, text= 'feet')

## Placing Labels
welcome_label.grid(row=0,columnspan=3) 
distance_label.grid(row=2, column=0)
angle_label.grid(row=4, column=0, sticky=E)
speed_label.grid(row=5, column=0, sticky=E)
need_label.grid(row=6, column=0, columnspan=3)
needang_label.grid(row=7, column=0, sticky=E)
deg_label.grid(row=7, column=2, sticky=W)
needspeed_label.grid(row=8, column=0, sticky=E)
mph_label.grid(row=8, column=2, sticky=W)
elev_label.grid(row=9, column=0, sticky=E)
ft_label.grid(row=9, column=2, sticky=W)

##Establishing Entry Fields
distance_entry = Entry(top_frame)
angle_entry = Entry(top_frame)                    
speed_entry = Entry(top_frame)
blank_ang = Entry(top_frame)
blank_speed = Entry(top_frame)
blank_elev = Entry(top_frame)

##Placing Entry Fields
distance_entry.grid(row=2, column=1)
angle_entry.grid(row=4, column=1)
speed_entry.grid(row=5, column=1)
blank_ang.grid(row=7, column=1)
blank_speed.grid(row=8, column=1)
blank_elev.grid(row=9, column=1)

## Establishing Buttons
angle_button = Button(top_frame, text='Calc Final Speed', bg='red', fg='black',command=Velocity)
speed_button = Button(top_frame, text='Calc Angle Needed', bg='blue', fg='white',command=Ang_Degree)

## Placing Buttons
angle_button.grid(row=4, column=2, sticky=W)
speed_button.grid(row=5, column=2, sticky=W)


    
zipline.mainloop()

