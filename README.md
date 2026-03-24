Aircraft Performance Analysis Tool

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

Screenshots
(Main menu)
<img width="407" height="230" alt="image" src="https://github.com/user-attachments/assets/0df2e813-2fa7-46fb-b166-9e5453afdb05" />
<img width="508" height="432" alt="image" src="https://github.com/user-attachments/assets/69ec2a15-e6f7-44cd-94d9-b62fd762cff7" />

(Lift and Drag calculation result)
<img width="536" height="570" alt="image" src="https://github.com/user-attachments/assets/4a6cac26-6c84-4caa-bc03-a8ffd58f7972" />

(Range calculation result)
<img width="591" height="339" alt="image" src="https://github.com/user-attachments/assets/f1d00593-a03c-447d-9a29-d472f5179c2c" />

(Drag vs Velocity graph)
<img width="797" height="678" alt="image" src="https://github.com/user-attachments/assets/10780051-a09b-4567-8f2a-8545df9c21ff" />
<img width="494" height="244" alt="image" src="https://github.com/user-attachments/assets/642eefdc-eda1-421d-8baa-6f6705f0483f" />

(Range vs Velocity graph)
<img width="830" height="1043" alt="image" src="https://github.com/user-attachments/assets/8c1d9a61-a8b1-44c9-ab98-a29a9e0cc1d0" />

(CSV file opened in Excel)
<img width="1919" height="1145" alt="image" src="https://github.com/user-attachments/assets/220f3c5c-529e-4ab5-9549-2377954aab51" />

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
