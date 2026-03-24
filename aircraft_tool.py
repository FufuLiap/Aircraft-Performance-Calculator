import math
import matplotlib.pyplot as plt
import numpy as np
import csv

print("1. A320")
print("2. B737")
print("3. Cessna 172")
choice = int(input("Select Aircraft: "))

if choice == 1:
    m = 73500
    S = 122.6
    CD = 0.024
    CL = 0.5
    print("You selected: A320")
    print("Mass: ", m, "kg")
    print("Wing Area: ", S, "m^2")
    print("CD: ", CD)
    print("CL: ", CL)
        
elif choice == 2:
    m = 70500
    S = 105.4
    CD = 0.025
    CL = 0.5
    print("You selected: B737")
    print("Mass: ", m, "kg")
    print("Wing Area: ", S, "m^2")
    print("CD: ", CD)
    print("CL: ", CL)
      
elif choice == 3:
    m = 1111
    S = 16.2
    CD = 0.03
    CL = 0.4
    print("You selected: Cessna 172")
    print("Mass: ", m, "kg")
    print("Wing Area: ", S, "m^2")
    print("CD: ", CD)
    print("CL: ", CL)
       
while True:      
       
    print("\n === Aircraft Performance Analysis Tool ===")
    print("1 - Calculate Lift & Drag")
    print("2 - Calculate Range")
    print("3 - Plot Drag vs Velocity Graph")
    print("4 - Plot Range vs Velocity Graph")
    print("5 = Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
    
        print("\n === Aircraft Calculator Tool === ")
    
        rho = float(input("Air density: "))
        v = float(input("Velocity: "))
        
        # Calculate lift using lift equation
        Lift = 0.5 * rho * v * v * S * CL
        # Calculate drag using drag equation 
        Drag = 0.5 * rho * v * v * S * CD

        print("\nResults:")
        print("Lift = ", Lift, "N" )
        print("Drag = ", Drag, "N")
        print("L/D =", CL / CD)

    elif choice == 2:

        print("\n === Range Calculator === " )
    
        CD0 = 0.02  # parasitic drag
        k = 0.04    # induced drag factor
    
        v = float(input("Enter flight speed (m/s): "))
        rho = float(input("Air density: "))
        S = float(input("Wing Area: "))
        c = float(input("Enter fuel consumption (1/s): "))
        Wi = float(input("Initial weight (N): "))
        Wf = float(input("Final weight (N): "))
    
        CL = (2 * Wi) / (rho * v * v * S )
        CD = CD0 + k * CL * CL

        Range = ( v / c ) * ( CL / CD ) * math.log (Wi / Wf)
        Range_km = Range / 1000

        print("Estimated Range =", Range_km, "km")
    
    elif choice == 3:

        velocity = np.linspace( 20, 120, 100)
        drag_list = []
    
        rho = float(input("Air density: "))
        
        # Loop through velocity range to calculate range for each velocities
        for v in velocity:
            # Calculate drag at this velocity 
            drag = 0.5 * rho * v * v * S * CD
            
            # Store results for plotting
            drag_list.append(drag)
   
        # Plot Drag vs Velocity graph
        plt.plot(velocity, drag_list)
        plt.title("Drag vs Velocity")
        plt.xlabel("Velocity (m/s)")
        plt.ylabel("Drag (N)")
        plt.savefig("drag_vs_velocity.png")
        plt.show()
        
        # Find the velocity that gives the minimum drag 
        min_drag = min(drag_list)
        min_drag_velocity = velocity[drag_list.index(min_drag)]
        
        print("\n=== Minimum Drag Performance ===")
        print("Minimum drag speed =", round(min_drag_velocity, 2), "m/s")

    elif choice == 4:
    
        velocity = np.linspace(20, 120, 100)
        range_list = []
        max_range = 0
        optimal_velocity = 0

        CD0 = 0.02 #parasitic drag
        k = 0.04 #induced drag factor
        
        Wi = float(input("Initial weight (N): "))
        Wf = float(input("Final weight (N): "))
        rho = float(input("Air density: "))
        c = float(input("Enter fuel consumption (1/s): "))
        
        # Loop through velocity range to calculate range for each velocities
        for v in velocity:
                
            CL_dynamic = (2 * Wi) / ( rho * v * v * S)
            CD_dynamic = CD0 + k * CL_dynamic * CL_dynamic
            LD = CL_dynamic / CD_dynamic
    
            range_val = ( v / c ) * LD * math.log(Wi/ Wf)
            range_km = range_val / 1000
            
            # Store results for plotting
            range_list.append(range_km)
            
            # Find the velocity that gives the maximum range
            if range_km > max_range:
                max_range = range_km
                optimal_velocity = v
            
        print("\n=== Maximum Range Performance === ")
        print("Optimal velocity =", round(optimal_velocity,2),"m/s")
        print("Maximum range =", round(max_range,2),"km")
        
        # Plot Drag vs Velocity Graph
        plt.plot(velocity, range_list)
        plt.title("Range vs Velocity")
        plt.xlabel("Velocity (m/s)")
        plt.ylabel("Range (km)")
        plt.savefig("range_vs_velocity.png")
        
        with open("range_vs_velocity.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Velocity (m/s)", "Range (km)"])
            
            for i in range(len(velocity)):
                writer.writerow([velocity[i], range_list[i]])
                
        print("Data exported to range_vs_velocity.csv")
        
        plt.show()

    elif choice == 5:
    
        print("Program ended")
        break

    else:
    
        print("Invalid choice")
    

