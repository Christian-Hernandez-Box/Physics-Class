# Data Points
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Function Returning Farenheit to Celsius Conversion
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = "100 degrees Farenheit converts to: " + str(f_to_c(100)) + " Celsius."

print(f100_in_celsius)

# Function Returning Celsius to Farenheit Conversion
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = "0 degrees Celsius converts to: " + str(c_to_f(0)) + " Farenheit."

print(c0_in_fahrenheit)

# Funtion Returning Force Given (Mass X Acceleration)
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Function Returning Energy Given (Mass X Constant)
def get_energy(mass, c = 3*10**8):
  return mass * c**2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Function Returning Work Given (Mass X Acceleration X Distance)
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
