# # Python Code Challenge #7: Schedule a Function

# Your goal is to implement a function, `schedule_function()`, that takes three inputs arguments for the time at which to run a specified function, the function you want to execute, and a variable number (zero or more) of arguments which are passed to the schedule function to use. 

# When your `schedule_function()` is called, it should immediately print a message indicating which function was scheduled and when it will execute.

# ## Example Test Output
# ```console
# >>> schedule_function(time.time() + 1, print, 'Howdy!')
# print() scheduled for Sun Aug 14 20:39:28 2022
# ```
# Then one second later...
# ```console
# Howdy!
# ```

# ## Constraints
# - You can assume that the first argument is a valid time in the future.
# - The function to be scheduled will always be a valid function.
# - The number of arguments passed to the function can be zero or more.

import time

def schedule_function(time_to_run, function, *args):
    args_str = ', '.join(map(str, args))
    print(f"{function.__name__}() with args = [{args_str}] scheduled for {time.ctime(time_to_run)}")
    time.sleep(time_to_run - time.time())
    function(*args)

if __name__ == "__main__":
    schedule_function(time.time() + 2, print, 'Howdy!')  # Output: print() scheduled for Sun Aug 14 20:39:28 2022
    # Howdy