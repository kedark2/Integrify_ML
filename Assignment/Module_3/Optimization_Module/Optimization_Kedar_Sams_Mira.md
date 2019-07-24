## 1. Outline
### a.  What are the basic elements of optimization? Give some examples.
    
### b.  Why is optimization important in machine learning? Give some examples.

## a. Elements of Optimization

There are three basic elements for any optimization regardless the field from where the optimization problems come.

1. Variables - free parameters which the algorithm, a set of functions, can run.

2. Constraints - the boundaries for the variables in which the variables must fall.

3. Objective function - the goal towards the algorithm drives the solution.


## Optimization for Linear Regression


![enter image description here](https://lh3.googleusercontent.com/Jnd3g5iSWQmNzcnO_QlE8lmk1VplEAK0-dtea9i1Mk2_AucyqaP7fDc-wz5vzlOnLvF5eCLRpjgUlg)

## b. Importance of Optimization in Machine Learning

In Machine Learning, Machine learns from the data to build a model which can be deployed for making an analysis for unseen or unused data. However, optimization is is the part which tunes the model to get accurate prediction, but in reality, it is quiet impossible to get the accurate prediction. It means there are errors always. But through the optimization the errors are being kept as low as possible to get a best goodness of the model. Actually, in ML, optimization process fit a curve with a low errors (the sum of squared errors.) 


Optimization helps for 

    - using the data effectively
    
    - estimating the computational load for a large data set processing, and 
    
    - avoiding local minima and search a good solution from a complex multi-dimensional space. 

## 2. Recollect : What is a  loss function / cost function? Give examples

Loss function / Cost function both shows how wrong we would be if we use model to make prediction on X when correct output it Y. Both can also be known as error function meaning in a way both are used to find the error on our prediction. There is no universal Loss function that works for all data.

The small difference between Loss and Cost function is that Loss function is usually on a data point, whereas cost function is more general. Cost function might be sum of loss functions over the training sed plus some model complexity. 

Usage area of loss function is mostly on parameter estimation whereas cost function is used in optimisation problems

## 3. What is a gradient operator? **Trick question :What are its possible eigenfunctions and eigenvalues?
The _Gradient_ (also called the _Hamilton_ operator) is a vector operator for any N-dimensional scalar function ![$f(x_1,\cdots, x_N)=f({\bf x})$](http://fourier.eng.hmc.edu/e161/lectures/gradient/img14.png), where ![${\bf x}=[x_1,\cdots,x_N]^T$](http://fourier.eng.hmc.edu/e161/lectures/gradient/img15.png) is an N-D vector variable. For example, when ![$N=3$](http://fourier.eng.hmc.edu/e161/lectures/gradient/img16.png), ![$f({\bf x})$](http://fourier.eng.hmc.edu/e161/lectures/gradient/img17.png) may represent temperature, concentration, or pressure in the 3-D space. The gradient of this N-D function is a vector composed of  ![$N$](http://fourier.eng.hmc.edu/e161/lectures/gradient/img18.png)components for the  ![$N$](http://fourier.eng.hmc.edu/e161/lectures/gradient/img18.png)  partial derivatives:  

![enter image description here](http://fourier.eng.hmc.edu/e161/lectures/gradient/img19.png)


![
](https://lh3.googleusercontent.com/F8Ih99kSJktL_vfV4-2isASGDg8TXDpJ779pnBvAZr6PakL8w9vwiZnIb1LksXsmJJJYA9OsH74uMg "Gradient Operator")
![
](https://lh3.googleusercontent.com/2ylCu8SGBpC2RgPkE49BmsNi89aMPvuFFLwKpXrB1dbtEtqICurtjavCxmlLkghuueev2W6kam8-Qg "Gradient Operator1")

## 4. How is Hessian related to the gradient, eigenvalues, optimization and convergence?

Derivative - It measures the rate of changes of a function due to the changes between x and y variables. 

Gradient - is the rate of changes of some function (in deep learning, this is generally the loss function) in various directions. A gradient is simply a collection of the derivatives of the function for each direction. Each element of the gradient is simply the slope of the function in each direction.

Hessian - is the derivative of the Gradient. Or we can say, it is the secondary derivative of the changing rate of slope.

If the eigenvalues are larger then the Gradient is also larger. When the eigenvalues are larger then there is a larger curvature. The larger curvature with less optimization leads to faster convergence.    

## 6. What is momentum and what problem is it solving?

Momentum is very popular technique that is used along with SGD. Instead of using only the gradient of the current step to guide the search, momentum also accumulates the gradient of the past step to determine the direction to go. The equations of gradient descent are revised as follows.

![enter image description here](https://blog.paperspace.com/content/images/2018/06/momentum.png)

The first equations has two parts. The first term is the gradient that is retained from previous iterations. This retained gradient is multiplied by a value called 'Coefficient of Momentum' which is the percentage of the gradient retained every iteration.

![enter image description here](https://blog.paperspace.com/content/images/2018/06/momentum2-1.png)


If we set the initial value for  _v_  to 0 and chose our coefficient as 0.9, the subsequent update equations would look like.

![update_eq-1](https://blog.paperspace.com/content/images/2018/06/update_eq-1.png)

We see that the previous gradients are also included in subsequent updates, but the weightage of the most recent previous gradients is more than the less recent ones. (For the mathematically inclined, we are taking an exponential average of the gradient steps)
