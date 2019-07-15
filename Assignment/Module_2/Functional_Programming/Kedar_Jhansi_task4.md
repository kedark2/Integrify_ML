## Task 4
***In your own words, describe what is functional programming and how you can write functional programming code in Python (start here:  [https://docs.python.org/3/library/functional.html](https://docs.python.org/3/library/functional.html))***


Functional programming is a programming paradigm that avoids state and mutable data and instead relies on function return values. This means a purely functional program written in python will not have things like variables, states etc

Functional code is characterised by one thing: the absence of side effects. It doesn’t rely on data outside the current function, and it doesn’t change data that exists outside the current function. Every other “functional” thing can be derived from this property.

Let's understand this by using already defined function.
#### Map

Map takes a function and a collection of items. It makes a new, empty collection, runs the function on each item in the original collection and inserts each return value into the new collection. It returns the new collection.

This is a simple map that takes a list of names and returns a list of the lengths of those names:

```
name_lengths = map(len, ["Mary", "Isla", "Sam"])

print name_lengths
# => [4, 4, 3]

```

This is a map that squares every number in the passed collection:

```
squares = map(lambda x: x * x, [0, 1, 2, 3, 4])

print squares
# => [0, 1, 4, 9, 16]

```

This map doesn’t take a named function. It takes an anonymous, inlined function defined with  `lambda`. The parameters of the lambda are defined to the left of the colon. The function body is defined to the right of the colon. The result of running the function body is (implicitly) returned.

The unfunctional code below takes a list of real names and replaces them with randomly assigned code names.

```
import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print names
# => ['Mr. Blonde', 'Mr. Blonde', 'Mr. Blonde']

```

(As you can see, this algorithm can potentially assign the same secret code name to multiple secret agents. Hopefully, this won’t be a source of confusion during the secret mission.)

This can be rewritten as a map:

```
import random

names = ['Mary', 'Isla', 'Sam']

secret_names = map(lambda x: random.choice(['Mr. Pink',
                                            'Mr. Orange',
                                            'Mr. Blonde']),
                   names)
```
Functional programming is beautiful and pure. Functional code can be clean. Some hardcore Python programmers dislike the functional paradigm in Python but you should use what you want to use, use the best tool for the job

### References
* [https://hackernoon.com/learn-functional-python-in-10-minutes-to-2d1651dece6f](https://hackernoon.com/learn-functional-python-in-10-minutes-to-2d1651dece6f)*
