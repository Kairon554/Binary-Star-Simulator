import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

print ("This is the animation of binary star system")

print("Please select a scenario")
print("1.Two stars with the same mass")
print("2.One heavier one lighter(Like the earth and the sun)")
print("3.Extreme mass difference")
print("4.Very elliptical orbit(With high initial velocity)")
print("5.Hyberbolic Orbit(escape orbit)")
print("6.Circular orbit")

scenario=int(input("Please select a scenerio between 1 and 6"))

if scenario==1:
    #Setting phyiscs constants and parametres
    G=1.00  #Gravitational constant, we do not use the actual value as it is too small and we are not able to see the motion
    dt=0.001    #Times steps（Smaller dt makes the graph more accurate)
    total_time= 10.00    #Total Time
    #Setting two initial stars
    m1=10.0 #Mass of the first star
    r1= np.array([-0.5,0.0])    #Initial position, left
    v1=np.array([0.0,-2.0])     #Initital velocity, towards bottom
    #Setting the second star
    m2=10.0
    r2=np.array([0.5,0.0])
    v2=np.array([0.0,2.0])


elif scenario==2:
    G=1.00  
    dt=0.001    
    total_time= 12.00    
    m1=5.0  
    r1= np.array([-0.0,0.0])   
    v1=np.array([0.0,-0.0])     
    m2=0.1
    r2=np.array([1.5,0.0])
    v2=np.array([0.0,0.9])

    
elif scenario==3:
    G=1.00  
    dt=0.0001
    total_time= 12
    m1=10000.0
    r1= np.array([0.0,0.0])    
    v1=np.array([0.0,0.0])     
    m2=1.0
    r2=np.array([-0.4,0.3])
    speed=80     #Here, If we set the value 141.4, the trial will be a perfect circle because Gravity equals to centripatal force.
    v2=np.array([0.6,0.8])*speed
    

elif scenario==4:
    G=1.00  
    dt=0.0005
    total_time= 12.00
    m1=1000.0
    r1= np.array([-0.0,0.0])    
    v1=np.array([0.0,-0.0])     
    m2=5.0
    r2=np.array([1.0,0.0])
    v2=np.array([-1.0,43.5])

elif scenario==5:
    G=1.00  
    dt=0.0005
    total_time= 3.0
    m1=100.0
    r1= np.array([-0.0,0.0])    
    v1=np.array([0.0,-0.0])     
    m2=1.0
    r2=np.array([0.8,0.6])
    speed=15
    v2=np.array([-0.6,0.8])*speed

elif scenario==6:
    G=1.00  
    dt=0.0005
    total_time= 3.0
    m1=10000.0
    r1= np.array([-0.0,0.0])    
    v1=np.array([0.0,-0.0])     
    m2=1.0
    r2=np.array([0.8,0.6])
    v2=np.array([60.0,-80.0])

else:
    print("Sorry, no valid number is detected. Now demonstrate the default scenario")
    G=1.00  
    dt=0.001    
    total_time= 10.00    
    m1=1.0
    r1= np.array([-0.8,0.0])   
    v1=np.array([0.0,-0.6])     
    m2=1.0
    r2=np.array([0.8,0.0])
    v2=np.array([0.0,0.6])





      

#Total Momentum, which is always conserved
total_momentum=m1*v1+m2*v2
print("Total momentum is", total_momentum, "kgm/s")

#Preparing the arrays of the trails for sketching the graphs
trail1_x, trail1_y=[], []   #Star1
trail2_x, trail2_y=[], []   #Star2

#Time steps, making the stars to move
steps=int(total_time/dt)    #In this case, steps are 5000. Meaning there are 5000 images need to be calculated

for i in range (steps):
    dr=r2-r1    #The vector of the distance between two stars
    dist=np.linalg.norm(dr)     #Magnitude of the distance(Scalor)
    if i%1000 ==0:
        print(f"step{i}: distance={dist:.6f}")  #Print the distacebetween two stars

    if dist<0.0000001:
        break           #Prevent the distance getting too close to make the code crash

    #Using Newton's Second Law to  calculate the acceleration
    a1=G*m2*dr/dist**3  #Acceleration due to the gravity of Star1
    a2=-G*m1*dr/dist**3  #Acceleration due to the gravity of Star2 with opposite direction

    #Now Using the acceleration to calculate the velocity
    v1+=a1*dt
    v2+=a2*dt

    #And the position as well
    r1+=v1*dt
    r2+=v2*dt

    #Record the trail, save for every 5 steps
    if i % 1 ==0:
        trail1_x.append(r1[0])
        trail1_y.append(r1[1])
        trail2_x.append(r2[0])
        trail2_y.append(r2[1])

#Output the trails, make the stars move
#Calculate the range of the figures, make sure stars are in the middle
all_x = trail1_x + trail2_x
all_y = trail1_y + trail2_y
max_range = max(max(all_x) - min(all_x), max(all_y) - min(all_y)) / 2
center_x = (max(all_x) + min(all_x)) / 2
center_y = (max(all_y) + min(all_y)) / 2
limit = max(max_range, 0.5) * 1.6  

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(center_x - limit, center_x + limit)
ax.set_ylim(center_y - limit, center_y + limit)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title('Binary star trail animation')

#Create 2 trails+ 2stars
trail1, = ax.plot([], [], '-', color='orange', linewidth=1.5, alpha=0.6, label='star1 trail')
trail2, = ax.plot([], [], '-', color='blue', linewidth=1.5, alpha=0.6, label='star2 trail')
star1, = ax.plot([], [], 'o', color='red', markersize=12, label='star1 position')
star2, = ax.plot([], [], 'o', color='cyan', markersize=12, label='star2 position')
ax.legend()

def init():
    trail1.set_data([], [])
    trail2.set_data([], [])
    star1.set_data([], [])
    star2.set_data([], [])
    return trail1, trail2, star1, star2

def update(frame):
    #Update the trails
    trail1.set_data(trail1_x[:frame], trail1_y[:frame])
    trail2.set_data(trail2_x[:frame], trail2_y[:frame])
    # Update the position of the stars
    if frame < len(trail1_x):
        star1.set_data([trail1_x[frame]], [trail1_y[frame]])
        star2.set_data([trail2_x[frame]], [trail2_y[frame]])
    return trail1, trail2, star1, star2

ani = animation.FuncAnimation(fig, update, frames=len(trail1_x), 
                              init_func=init, blit=True, interval=20, repeat=True)

plt.show()


