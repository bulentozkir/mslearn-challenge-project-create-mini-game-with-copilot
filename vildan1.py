import numpy as np
import matplotlib.pyplot as plt
import gurobipy as gp
from gurobipy import GRB, quicksum

rnd = np.random
rnd.seed(1)

n = 8  # number of customers
xc = rnd.rand(n + 1) * 200
yc = rnd.rand(n + 1) * 100

# Sets
V = [k for k in range(1, 3)]  # set of vehicles
N = [i for i in range(1, n + 1)]  # set of customers
N_all = [0] + N  # set of all nodes
A = [(i, j, k) for i in N for j in N for k in V if i != j]  # set of arcs
B = [(i, k) for i in V for k in V]  # set linking nodes and vehicles

# Parameters
Vehicle_Capacity = 5000
Demand = {i: rnd.randint(1000, 3000) for i in N}
distance = {(i, j, k): np.hypot(xc[i] - xc[j], yc[i] - yc[j]) for i, j, k in A}
Penalty = 99

# Create Gurobi model
m = gp.Model('CVRP_with_Penalty')

# Decision variables
x = m.addVars(A, vtype=GRB.BINARY, name='x')  # Binary variable if vehicle k travels directly from node i to node j
y = m.addVars(N, V, vtype=GRB.BINARY, name='y')
z = m.addVars(N, lb=0.0, ub=1, vtype=GRB.CONTINUOUS, name='z')  # The fraction of satisfied demand
u = m.addVars(B, vtype=GRB.CONTINUOUS, name='u')  # satisfied demand at node i by vehicle k


# Objective function
m.setObjective(quicksum(distance[i, j, k] * x[i, j, k] for i, j, k in A) + Penalty * quicksum(z[i] for i in N),
               GRB.MINIMIZE)

# Each customer must be visited at most once by one of the vehicles
m.addConstrs(quicksum(x[i, j, k] for k in V for j in N if i != j) == 1 for i in N)
m.addConstrs(quicksum(x[i, j, k] for k in V for i in N if i != j) == 1 for j in N)
# Flow conservation for each intermediate node for each vehicle
m.addConstrs(quicksum(x[i, j, k] for j in N if i != j) - quicksum(x[j, i, k] for j in N if i != j) == 0 
             for i in N for k in V)
# Each vehicle must leave and arrive at the depot
m.addConstrs(quicksum(x[i, j, k] for i in N if i == 0) == 1 for j in N for k in V)
m.addConstrs(quicksum(x[i, j, k] for j in N if i == 0) == 1 for i in N for k in V)
# Each vehicle must must be assigned at least one customer
m.addConstrs(quicksum(y[i, k] for k in V) == 1 for i in N)
# A customer is visited only if assigned by one of the vehicles
m.addConstrs(y[j, k] + y[i, k] <= 2* x[i, j, k] for i in N for j in N for k in V)
# Capacity constraint for each vehicle and demand satisfaction
m.addConstrs(quicksum(u[i, k] for k in V) == Demand[i] * (1-z[i]) for i in N)
m.addConstrs(u[i, k] <= Vehicle_Capacity * y[i, k] for i in N for k in V)
#m.addConstrs(quicksum(u[i, k] for i in N) <=  Vehicle_Capacity * (1 - x[i, j, k]) for i in N for j in N for k in V)

# Solve the model
m.Params.MIPGap = 0.1
m.Params.TimeLimit = 100  # seconds
m.optimize()

# Access the solution
if m.status == GRB.OPTIMAL:
    print('Optimal solution found')
    # Access the values of decision variables, e.g., x[i, j, k].x
else:
    print('No optimal solution found')
