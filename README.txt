Aircraft Performance Calculator

This project is a Python-based engineering tool developed to analyse basic aircraft performance.
It calculates  lift, drag, and range for different aircraft at different velocities.
The program also determines the optimal velocity for maximum rannge and generate performance graphs.

This project was built as part of my learning in Aerospace Engineering to apply aerodynamics and programming concepts into a practical engineering tool.

Features:
- Aircraft selection (A320, B737, Cessna 172)
- Calculates Lift and Drag using aerodynamic equations
- Computes Lift-to-Drag ratio
- Estimates aircraft range using the Breguet Range Equation
- Pilots Drag vs Velocity graph
- Pilots Range vs Velocity graph
- Uses drag polar model to analyse optimum range speed
- Optimal velocity calculation for maximum range
- Export results to CSV file

Concepts used:
- Lift equation ( L = 0.5 * rho * v * v * S * CL )
- Drag equation ( D = 0.5 * rho * v * v * S * CD ) 
- Lift-to-Drag ratio
- Breguet Range Equation ( R = ( v / c ) * ( L / D ) * ln ( Wi / Wo ) )
- Drag polar ( CD = CD0 + kCL^2 )
- Parametric analysis

Example Output:

Selected Aircraft: B737
Optimal Velocity: 24.04 m/s
Maximum Range: 4074.57 km

Results exported to results.csv

How to Run:
1. Install Python
2. Install mmatplotlib: pip install matplotlib
3. Run the Python file
4. Select aircraft
5. Choose calculation from menu

Run the program:
python aircraft_tool.py

Tools used:
- Python
- Matplotlib
- NumPy

What I learned:
- Self-studied and applied basic Python programming to solve engineering problems 
- Learned how to model aircraft performance using mathematic formulae
- Implemented data visualization for graphs using Matplotlib
- Understood relationship between drag, velocity, and range

Future improvements:
- Add mroe aircraft models
- Add graphical user interface (GUI)
- Add fuel consumption model
- Add real aircraft performance data

Liap Jin Fu
Diploma in Aerospace Engineering
Ngee Ann Polytechnic
