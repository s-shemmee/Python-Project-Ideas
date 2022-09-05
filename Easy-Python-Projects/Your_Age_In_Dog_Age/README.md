# The input function

*At some point in your programming career, you will write software that takes input from the user and processes it. This lesson covers how to do this. You will learn how to read and utilize user input. User input usually comes in the form of strings. Sometimes this isn't what your code needs and so we will show you how to cast this into an appropriate type.*
 
*We're going to practice collecting inputs from users. Create a file called `input.py`.*

*You can create variables which require the user to add information, the input, before printing the result. You can also create an interpolated string with the variables inside.*

*The thing about user input is that it always comes in the form of a string. So, if you wanted to calculate a user's age in dog years, you need to convert the user input into a number you can multiply by seven.* 

*You could use the `int()` function to convert your string into an integer.* 

*So one of the easiest ways to fix this inside your script is to wrap `int()` your age input variable, like so: `int(input("How old are you?"))`. You could also theoretically do it for `age_in_dog_years =`  as well.* 