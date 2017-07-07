# Introduction to Control Flow

Control flow is the sacred art of telling your program what to do and when to do it.

While teaching a robot to love is nearly impossible, teaching your code how to act in different situations isn't so bad!

But how?

You can start by describing how you want your program to act in English. 

```
If you give a cat some catnip, the cat will probably go crazy.
Otherwise, the cat will probably just be lazy and clean itself.
```

Then, you can translate that into python, use `if`, `elif`, and `else` statements in python used to denote the different cases of how your program would act. You give each of these statements a condition that has to be met for the code indented below it to be executed. The `if` statement is for the first possible condition,  `elif` (can have zero or more `elif` statements) is for all the other potential conditions, and `else` is if none of those conditions are met.

And now you can go to real python code!

```
if catnip == True:
  # cat goes crazy
else:
  # cat cleans itself
```

That's the first part of control flow!

## Reading material

* [Chapter 2](https://automatetheboringstuff.com/chapter2/) from Automate the Boring Stuff with Python (Read up until while loops)
* (Optional) [Control Flow](https://python.swaroopch.com/control_flow.html) from A Byte of Python (Only the stuff on if statements)
