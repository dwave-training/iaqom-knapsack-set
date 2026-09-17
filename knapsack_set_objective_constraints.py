"""
Requirements:
    Objective: Maximize the total value of products in the shipping container.
    Constraints: 
        - The total weight of all selected products cannot exceed the weight limit of the shipping container.
        - Pack no more than a certain number of products in the shipping container.

Given constants:
    values (list): Values of the products.
    weights (list): Weights of the products.
    weight_limit (int): Weight limit of the shipping container.
    capacity (int): Total number of products the container can hold.
"""

# Import the packages
from dwave.optimization import Model
from dwave.system import StrideHybridSolver 

# Create the model.
# Initialize the nonlinear model object.
model = Model()

# Define the constants.
# Values of the products.
values = [10, 15, 20, 21, 25, 13, 19, 13, 22, 16] 

# Weights of the products.
weights = [13, 8, 11, 14, 15, 11, 14, 6, 10, 9] 

# Weight limit of shipping container.
weight_limit = 76 

# Total number of products the container can hold.
capacity = 8 

# Constants symbols.
product_values = model.constant(values)
product_weights = model.constant(weights)
container_weight_limit = model.constant(weight_limit)

# Decision variable.
selected_products = model.set(10, max_size = capacity) 

# Objective function: Maximize the total value of products in the shipping container.
model.minimize(-product_values[selected_products].sum()) 

# Add constraint: The total weight of all selected products cannot exceed the weight limit of the shipping container.
model.add_constraint(product_weights[selected_products].sum() <= container_weight_limit) 

# Test one initial state:
# Lock the model using a context manager. 


    # Define the number of states (test only one state).
    

    # Provide the following initial state: `[0,2,3,5,6,7]`.
    


# The best solution for the set variable symbol and its objective value:
# Lock the model explicitly to prevent changes. 


# Instantiate the nonlinear sampler.


# Submit the nonlinear model to the Stride hybrid solver.


# Print the index values of the selected products for the best solution and displays its objective value.
