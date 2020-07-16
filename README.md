# Computational-Calculus
An app that will perform basic computational calculus methods on general functions. These include
-Derivative
-Integration
-Bisection method
-Newton's method

The file Calc contains the definition for the Calc class and can be used independently by other programmers.
The file plots contains the class FunctionPlots, this class depends upon Calc and can also be used by other programmers.
The file Interface runs a GUI, which allows a front end user to input functions, plot them, and plot the derivative and integral. And run bisection and Newton's method on the function.


When running the interface program, again insure that you have the Calc and plot files in the same directory. 
If you close the plot window you must restart the program to bring it back up
You may type a function in the first text box. Only a single variable function may be used. Numpy commands will be recognized. For example sin(x) is not a python function, but np.sin(x) is recognized. Familiarity with numpy might be required.
The bounds Xmin and Xmax must be defined before the graph will show.

        	
class Calc(f, tolerance = 0.0001):
	#f is the function, must be passed in to the class constructor
	#tolerance will be used to determine when methods have converged.

	def bisection(a,b):
		#a and b are the bounds within which you can find a root. One bound must be above the axis, the other below.
	
	def newton(x)
		#x is the intial guess
		#Note that newton's will fail if the derivative ever equals 0

	def fp(x)
		#Calculate the derivative of f at x

	def trap(a,b,N)
		#Estimate the integral with trapezoid rule. a and b are the bounds and N is the number of trapezoids.


#Note at the moment this class is finicky and a sucessfull run depends upon the environment. This class was built to be used by the interface file.
class FunctionPlots(c)
	#c is an instance of a Calc class.

	def plotf(self, a, b, N = 100):
		#add a plot of the function between a and b with resolution N
        
    	def plotfp(self, a, b, N = 100):
		#add a plot of the derivative between a and b with resolution N
        
    	def plotInt(self, a, b, N=100):
		#adds an Integral plot where c is such that the integral passes through the origin

	def clearPlot():
		#Clears the plot
			
