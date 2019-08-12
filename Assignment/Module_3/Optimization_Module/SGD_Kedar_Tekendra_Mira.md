## Differences between GD and SGD

-   In GD the error is summed over all examples before updating weights, in SGD weights are updated upon examining each training example
-   Summing over multiple examples in GD requires more computation per weight update step. But since it uses the True gradient, it is often used with a larger step size
-   If there are multiple local minima with respect to  ![tex2html_wrap9053](https://www.cs.auckland.ac.nz/~pat/706_98/ln/img225.gif)  , SGD can sometimes avoid falling into these local minima
- 
## Comparison how Gradient Descent and Stochastic Gradient Descent differ in

-   Convergence (convergence speed)

In both gradient descent (GD) and stochastic gradient descent (SGD), you update a set of parameters in an iterative manner to minimize an error function.

While in GD, you have to run through ALL the samples in your training set to do a single update for a parameter in a particular iteration, in SGD, on the other hand, you use ONLY ONE or SUBSET of training sample from your training set to do the update for a parameter in a particular iteration. If you use SUBSET, it is called Minibatch Stochastic gradient Descent.

Thus, if the number of training samples are large, in fact very large, then using gradient descent may take too long because in every iteration when you are updating the values of the parameters, you are running through the complete training set. On the other hand, using SGD will be faster because you use only one training sample and it starts improving itself right away from the first sample.

SGD often converges much faster compared to GD but the error function is not as well minimized as in the case of GD. Often in most cases, the close approximation that you get in SGD for the parameter values are enough because they reach the optimal values and keep oscillating there.

## Use case (when to use which algorithm)
### Gradient Descent Algorithm

-   if training examples are not linearly separable, the delta rule converges toward a best-fit approximation
-   use  _gradient descent_  to find the weights that best fit the training examples - basis of Backpropagation Algorithm
-   assume an unthresholded perceptron, then the training error is  ![tex2html_wrap9023](https://www.cs.auckland.ac.nz/~pat/706_98/ln/img218.gif)  where  ![tex2html_wrap8292](https://www.cs.auckland.ac.nz/~pat/706_98/ln/img49.gif)  is the set of training examples,  ![tex2html_wrap9025](https://www.cs.auckland.ac.nz/~pat/706_98/ln/img219.gif)  is the target output for the training example  ![tex2html_wrap8347](https://www.cs.auckland.ac.nz/~pat/706_98/ln/img58.gif)  and  ![tex2html_wrap9027](https://www.cs.auckland.ac.nz/~pat/706_98/ln/img220.gif)  is the output of the linear unit for training example  ![tex2html_wrap8347](https://www.cs.auckland.ac.nz/~pat/706_98/ln/img58.gif)  .
-   Given above error definition, the error surface must be parabolic with a single global minimum.
### Stochastic gradient descent Algorithm
- It is used when the training data size is huge because GD may be infeasible in such case.
- If the training data set has many redundant data instances, stochastic gradients may be so close to the true gradient ∇𝑓(𝐱)∇f(x) that a small number of iterations will find useful solutions to the optimization problem.


## Their difference from Optimization point of view.

**_Gradient descent_**  is most commonly used and popular **_iterative_** machine learning algorithm. It is also the foundation for other optimization algorithms.  _Gradient descent_  has the following  _update rule_  for  _weight_parameter

![](https://miro.medium.com/max/329/1*faTF4_-a7qMAzw3y27wzOw.png)

Since during  _backpropagation_  for updating the parameters, the  _derivative of loss_  w.r.t. a parameter is calculated. This  _derivative_  can be dependent on more than one variable so for its calculation  **_multiplication chain rule_**  is used. For this purpose, a  **_Gradient_**  is required. A  **_gradient_**  is a vector indicating the direction of increase.

**For gradient calculation, we need to calculate  _derivatives of loss_  w.r.t the  _parameters_  and update the  _parameters_  in the opposite direction of the  _gradient._**


![](https://miro.medium.com/max/460/1*jYQYuHpHdkZqNFQKJSuDTw.png)

The above ideal convex curve image displays the  _weight update_  in the opposite direction of the  _gradient_. As we can notice for too large and small values of  _weights_  the  _loss_  is maximum and our goal is to  _minimize_  the  _loss_  so the  _weights_ are updated. If the  _gradient_  is negative then  **_descent_**(dive) towards the positive side and if the  _gradient_  is positive then descent towards the negative side until the minimal value of  _gradient_  is found.

Algorithm for  **_Gradient descent_**  using a single neuron with  _sigmoid_activation function in Python

def sigmoid(w,b,x):  
    return 1.0 / (1.0 + np.exp(-w*x + b))def grad_w(w,b,x,y):  
    fx = sigmoid(w,b,x)  
    return (fx — y) * fx * (1-fx) * xdef grad_b(w,b,x,y):  
    fx = sigmoid(w,b,x)  
    return (fx — y) * fx * (1-fx)def do_gradient_descent():  
    w,b,eta = -2, -2, 1.0  
    max_epochs = 1000  
    for i in range(max_epochs):  
        dw,db = 0,0  
        for x,y in zip(X,Y):  
            dw += grad_w(w,b,x,y)  
            db += grad_b(w,b,x,y)  
        w = w — eta * dw  
        b = b — eta * db

![](https://miro.medium.com/max/480/1*nuoD-tQylhMj-SF8WJfUjg.gif)

The above  _animation_  represents how the algorithm converges after 1000  _epochs_. The error surface used in this  _animation_  is as per the input. This error surface is animated in 2D space. For 2D, a  _contour map_  is used where the contours represent the third dimension i.e.  **_error_**. The red regions represent the high values of error, more the intensity of the red region more the error. Similarly, the blue regions represent the low values of error, less the intensity of the blue region less the error.

**_Standard Gradient descent_**  updates the  _parameters_  only after each epoch i.e. after calculating the  _derivatives_  for all the observations it updates the  _parameters_. This phenomenon may lead to the following  **_caveats_**.

-   It can be very slow for very large datasets because only one-time  _update_for each  _epoch_  so large number of  **_epochs_**  is required to have a substantial number of  _updates_.
-   For large datasets, the vectorization of data doesn’t fit into  **_memory_**.
-   For  _non-convex_  surfaces, it may only find the  **_local minimums._**

Now let see how  **_different variations of gradient descent_**  can address these challenges.

# Stochastic gradient descent

**_Stochastic gradient descent_**  updates the  _parameters_  for  _each observation_ which leads to more number of updates_._ So it is a faster approach which helps in quicker decision making.

Algorithm for  _Stochastic_  _Gradient descent_  using a single neuron with  _sigmoid_activation function in Python

def do_stochastic_gradient_descent():  
    w,b,eta = -2, -2, 1.0  
    max_epochs = 1000  
    for i in range(max_epochs):  
        dw,db = 0,0  
        for x,y in zip(X,Y):  
            dw += grad_w(w,b,x,y)  
            db += grad_b(w,b,x,y)  
            w = w — eta * dw  
            b = b — eta * db

![](https://miro.medium.com/max/480/1*eqbCPD7Yx_nRchmP6YtjYA.gif)

**_Quicker updates_**  in different directions can be noticed in this animation. Here, lots of oscillations take place which causes the  _updates_  with  **_higher variance_**  i.e.  **_noisy_**  **_updates_**. These noisy updates help in finding  **_new_** and  **_better local minima_**.

**Disadvantages of SGD**

-   Because of the  **_greedy approach_**, it only  **_approximates (stochastics)_**  the gradient.
-   Due to  **_frequent fluctuations_**, it will keep  **_overshooting_**  near to the desired  **_exact minima_**.

Now let see how another  **_variant of gradient descent_**  can address these challenges.
