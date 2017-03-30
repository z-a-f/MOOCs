"""
Machine Learning Online Class - Exercise 1: Linear Regression

  Instructions
  ------------
  This file contains code that helps you get started on the
  linear exercise. You will need to complete the following functions 
  in this exericse:
     warmUpExercise.m
     plotData.m
     gradientDescent.m
     computeCost.m
     gradientDescentMulti.m
     computeCostMulti.m
     featureNormalize.m
     normalEqn.m
  For this exercise, you will not need to change any code in this file,
  or any other files other than those mentioned above.
   refers to the population size in 10,000s
   refers to the profit in $10,000s
"""

import numpy as np
import pandas as pd

## ==================== Part 1: Basic Function ====================
# Complete warmUpExercise.m 
print('Running warmUpExercise ...')
print('5x5 Identity Matrix:')
warmUpExercise()

raw_input('Program paused. Press enter to continue.')

## ======================= Part 2: Plotting =======================
print('Plotting Data ...')
data = np.genfromtxt('ex1data1.txt', delimiter = ',')
X = data[:, 0]
y = data[:, 1]
m = len(y) # number of training examples

# Plot Data
# Note: You have to complete the code in plotData.m
plotData(X, y)

raw_input('Program paused. Press enter to continue.')

## =================== Part 3: Gradient descent ===================
print('Running Gradient Descent ...')

X = np.vstack((np.ones(m), data[:,1])).T # Add a column of ones to x
theta = np.zeros(2, 1) # initialize fitting parameters

# Some gradient descent settings
iterations = 1500
alpha = 0.01

# compute and display initial cost
computeCost(X, y, theta)

# run gradient descent
theta = gradientDescent(X, y, theta, alpha, iterations)

# print theta to screen
print('Theta found by gradient descent:'),
print('%.2f %.2f'%(theta[0], theta[1]))

# Plot the linear fit
plt.plot(X(:,2), np.dot(X,theta), '-')
plt.legend('Training data', 'Linear regression')

# Predict values for population sizes of 35,000 and 70,000
predict1 = [1, 3.5] * theta
print('For population = 35,000, we predict a profit of %f'%(predict1*10000))
predict2 = [1, 7] * theta
print('For population = 70,000, we predict a profit of %f'%(predict2*10000))

raw_input('Program paused. Press enter to continue.')

## ============= Part 4: Visualizing J(theta_0, theta_1) =============
print('Visualizing J(theta_0, theta_1) ...')

# Grid over which we will calculate J
theta0_vals = np.linspace(-10, 10, 100)
theta1_vals = np.linspace(-1, 4, 100)

# initialize J_vals to a matrix of 0's
J_vals = np.zeros(( len(theta0_vals), len(theta1_vals) ))

# Fill out J_vals
for i in range(len(theta0_vals)):
  for j in range(len(theta1_vals)):
    t = [theta0_vals[i], theta1_vals[j]]
    J_vals[i,j] = computeCost(X, y, t)

# Because of the way meshgrids work in the surf command, we need to 
# transpose J_vals before calling surf, or else the axes will be flipped
J_vals = J_vals.T
# Surface plot
plt.figure()
plt.surf(theta0_vals, theta1_vals, J_vals)
plt.xlabel('theta_0')
plt.ylabel('theta_1')

# Contour plot
plt.figure()
# Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
plt.contour(theta0_vals, theta1_vals, J_vals, logspace(-2, 3, 20))
plt.xlabel('theta_0')
plt.ylabel('theta_1')
plt.plot(theta[0], theta[1], 'rx', 'MarkerSize', 10, 'LineWidth', 2)
