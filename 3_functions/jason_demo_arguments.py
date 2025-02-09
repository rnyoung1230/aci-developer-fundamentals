# parameterless:
def initiate_countdown():
    for i in range(10, 0, -1):
        print(i)
    print("Liftoff!")

# Sequential parameters:
def configure_launch_vehicle(destination, fuel_amount):
    print(f"Launching rocket to {destination} with {fuel_amount} liters of fuel.")

# keyword/optional parameters:
def plan_mission(destination, duration, crew_size=3, vehicle_type="orbiter"):
    print(f"Planning a {duration}-day mission to {destination}")
    print(f"Crew size: {crew_size}")
    print(f"Vehicle type: {vehicle_type}")

# *args
def pack_supplies(*items):
    print("Packing the following supplies:")
    for item in items:
        print(f"- {item}")

# **kwargs
def assign_roles(**crew_roles):
    print("Crew role assignments:")
    for astronaut, role in crew_roles.items():
        print(f"{astronaut}: {role}")

# mixed parameter types
def prepare_spacecraft(name, capacity, *equipment, propulsion="chemical", **systems):
    print(f"Preparing {name} mission:")
    print(f"Capacity: {capacity} crew")
    print(f"Propulsion type: {propulsion}")
    print("Equipment:")
    for item in equipment:
        print(f"- {item}")
    print("Systems:")
    for system, status in systems.items():
        print(f"- {system}: {status}")

# mixed parameter types with optional parameters
def plan_space_station(name, modules, *experiments, gravity=False, **staff):
    print(f"Planning space station: {name}")
    print(f"Number of modules: {modules}")
    print(f"Artificial gravity: {'Yes' if gravity else 'No'}")
    print("Experiments:")
    for exp in experiments:
        print(f"- {exp}")
    print("Staff:")
    for role, count in staff.items():
        print(f"- {role}: {count}")




# parameterless:
initiate_countdown()

# Sequential parameters:
configure_launch_vehicle("Mars", 1000000)

# keyword/optional parameters:
plan_mission("Moon", 7)  # Uses default crew_size and vehicle_type
plan_mission("Venus", 500, crew_size=5)  # Specifies crew_size, uses default vehicle_type
plan_mission("Europa", 1000, crew_size=4, vehicle_type="submersible probe")

# *args
pack_supplies("EVA suit", "food rations", "water", "tools")

# **kwargs
assign_roles(Jason="Commander", Steve="Pilot", Krishna="Engineer")

# mixed parameter types
'''
**kwargs cannot be presented before *args in a function definition. 
Python requires that parameters be defined in a specific order:

Regular positional parameters
Parameters with default values (optional parameters)
*args (if present)
**kwargs (if present)

####
Python determines the contents of *args based on how the function is called. 
Here's how it works:

Python first assigns values to all the regular positional parameters.
If there are any remaining positional arguments, they are collected into a 
tuple and assigned to *args.
Any keyword arguments that don't match defined parameters are collected 
into a dictionary and assigned to **kwargs.

Python knows where *args ends because it collects all remaining positional 
arguments after the regular parameters have been filled. Then, any keyword 
arguments that don't match defined parameters go into **kwargs.

This ordering system allows Python to unambiguously determine which arguments 
belong to which parameters, even with a mix of regular, *args, and **kwargs 
parameters.
'''
prepare_spacecraft("Explorer", 4, 
                   "life support", "communication array", "landing gear",
                   propulsion="ion drive",
                   navigation="calibrated", shields="engaged")

# mixed parameter types with optional parameters
plan_space_station("Horizon", 6, 
                   "Microgravity plant growth", "Cosmic ray detection", "Dark matter observation",
                   gravity=True,
                   scientists=20, engineers=15, medical_staff=5)


'''
Note about the "dangling" gravity in the last example:
In Python, it is indeed allowed and sometimes useful to have default parameters 
(like gravity=False in this case) after *args but before **kwargs. This is a 
special case in Python's function parameter syntax.

Here's the complete order of parameters that Python allows in function definitions:

Regular positional parameters
Parameters with default values (optional parameters)
*args (if present)
Parameters with default values after *args (optional keyword-only parameters)
**kwargs (if present)
In the function definition:

def plan_space_station(name, modules, *experiments, gravity=False, **staff):

name and modules are regular positional parameters
*experiments is for collecting any additional positional arguments
gravity=False is an optional keyword-only parameter
**staff is for collecting any additional keyword arguments

The gravity parameter, coming after *experiments, becomes a keyword-only argument. 
This means it can only be specified using its keyword when calling the function. 
It cannot be set using a positional argument.
'''