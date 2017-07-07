# Introduction to Functions

Functions are great!

They are like bite-sized programs in your code that can be executed to perform operations for you. You can combine them or reuse them in your code to do some pretty wonderful things!

The usually receive data as input and `return` a result as output.

Functions are built like this:

```
# Function Defintion
def my_function(parameter1, parameter2):
  # do something
  return result
```

`def` tells python that you are defining a function. Then you give it a name (my_function in this example).

In parenthesis, you see two parameters. You can have as many or as few as you want. Note that order matters (has to match the order of the function call). These are parameters the function receives as input to process. Note the keyword `return` in the function defintion. That means this function is going to have an output.

The function call is going to look similar to the function definition.

```
# Function Call
# This is a function call, where we tell python to run our function. 
# It's storing the function output that is returned in a new variable called function_result
function_result = my_function(argument1, argument2)

# Or you can give literal arguments and just send numbers instead of variables
function_result = my_function(1, "bob")
```

You use the functions name, and pass it arguments (function inputs). They are called arguments in a function call and parameters in a function definition. Note the difference.

These arguments are sent to the function defintion and are saved using the parameter names. When we run the first function call below, argument1 is stored in a variable called parameter1 and argument2 is stored in a variable called parameter2 in the function definition when it runs.

Then the code executes and we see the return statement, telling python our function has output. That output can be stored in a new variable when we call the function. We store it in a variable called function_result.

Those are the basics. 

Functions are generally used if some code is repeated or to break code down into smaller chunks that are easier to handle. Good luck!

Read up on functions in more detail in the following readings.

## Reading material

* [Chapter 3](https://automatetheboringstuff.com/chapter3/) from Automate the Boring Stuff
* [Functions](https://python.swaroopch.com/functions.html) from A Byte of Python

Optional Readings:
* [Intro](http://thelivingpearl.com/2013/12/23/introduction-to-functions-in-python/) from the living pearl
* Syntax, return, and param sections of [Python Course](http://www.python-course.eu/python3_functions.php)
