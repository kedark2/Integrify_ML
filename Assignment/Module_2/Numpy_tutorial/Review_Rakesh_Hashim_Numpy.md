
# Module_2

## Feedback of Rakesh & muhammad_hashim

## [ Github link](https://github.com/rmahato64/Numpy_Module2)

The basic Task of the assignment was to try out the Pair Programming in the google colab and learn the basic functionality of the numpy module.


**Basic Task Carried out** :
* creating an numpy array
* creating special array
* reshaping, Transpose
* Flatten, Ravel
* Selection, Slicing
*vectorized operations
*Boardcasting

The Basic command were well executed. The code were commented so they can be understood what they are supposed to work.
I think they were well learned by the individual and can be implemented for the further use.

**assignment**

Two of the assignment were done by the group

 The first assignment was to find the row index of the column of minimum value.

```python
X = np.random.randn(4,2)
X.argmin(axis = 0),X.argmin(axis = 1)
```

This code was used for creating a standardize() function to return an array whose column as centred and scaled.
```python
def standardize(X):
    norm_X =( X-np.mean(X))/np.std(X)
    return norm_X
```

overall the assignment is executing it should be.

# Google Colab Experience

We did our assignment on google colab. in the beginning it was little bit difficult but later on we figured out how the colab works and what are the functionalities. Colab did work but not in the efficient way. We had to refresh the page in certain interval to see the changes done by each other. It was not live and interactive.
On the other hand we found out some cool functionality.
There was possibility to add a form on the cell we work. Meaning in the form we had possibility to add from field where it was possible to add comment, report on md format or input. If we add input form field it was easier to change the input also and it changes the code automatically.
Though Google Colab is not that interactive as I expected to be, it is a good option to do work in single file with multiple user. Just that the users has to set the rule beforehand so that the changes they made would not erase the work done by other.
