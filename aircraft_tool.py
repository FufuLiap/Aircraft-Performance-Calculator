import math
import matplotlib.pyplot as plt
import numpy as np

while True:
    
    print(" === Aircraft Performance Analysis Tool ===")
    print("1 - Calculate Lift & Drag")
    print("2 - Calculate Range")
    print("3 - Plot Drag vs Velocity Graph")
    print("4 - Plot Range vs Velocity Graph")
    print("5 = Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
    
        print(" === Aircraft Calculator Tool === ")
    
        rho = float(input("Air density: "))
        v = float(input("Velocity: "))
        S = float(input("Wing Area: "))
        CL = float(input("CL: "))
        CD = float(input("CD: "))

        Lift = 0.5 * rho * v * v * S * CL
        Drag = 0.5 * rho * v * v * S * CD

        print("\nResults:")
        print("Lift = ", Lift, "N" )
        print("Drag = ", Drag, "N")
        print("L/D =", CL / CD)

    elif choice == 2:

        print("\n === Range Calculator === " )
    
        CD0 = 0.02 #parasitic drag
        k = 0.04 #induced drag factor
    
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

        velocity = np.linspace( 20, 100, 50)
        drag_list = []
    
        rho = float(input("Air density: "))
        v = float(input("Velocity: "))
        S = float(input("Wing Area: "))
        CL = float(input("CL: "))
        CD = float(input("CD: "))

        for v in velocity:
            drag = 0.5 * rho * v * v * S * CD
            drag_list.append(drag)
   
        plt.plot(velocity, drag_list)
        plt.title("Drag vs Velocity")
        plt.xlabel("Velocity (m/s)")
        plt.ylabel("Drag (N)")
        plt.savefig("drag_vs_velocity.png")
        plt.show()

    elif choice == 4:
    
        range_list = []

        CD0 = 0.02 #parasitic drag
        k = 0.04 #induced drag factor

        for v in velocity:
    
            CL_dynamic = (2 * Wi) / ( rho * v * v * S)
            CD_dynamic = CD0 + k * CL_dynamic * CL_dynamic
            LD = CL_dynamic / CD_dynamic
    
            range_val = ( v / c ) * LD * math.log(Wi/ Wf)
            range_list.append(range_val / 1000 )
    
        plt.plot(velocity, range_list)
        plt.title("Range vs Velocity")
        plt.xlabel("Velocity (m/s)")
        plt.ylabel("Range (km)")
        plt.savefig("range_vs_velocity.png")
        plt.show()

    elif choice == 5:
    
        print("Program ended")
        break

    else:
    
        print("Invalid choice")
    
