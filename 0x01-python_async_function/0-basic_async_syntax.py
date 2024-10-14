#!/usr/bin/env python3
""" Basics of async """
# Import necessary libraries
import asyncio  # Provides support for asynchronous I/O and concurrency
import random  # Used to generate random numbers

# Define an asynchronous function 'wait_random'
async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that takes an integer argument 'max_delay'
        and waits for a random number of seconds (between 0 and max_delay).
        
        Args:
            max_delay (int): The maximum number of seconds to wait.
                             Defaults to 10 seconds.
                             
        Returns:
            float: The random number of seconds waited (a float value).
    """
    # Generate a random floating-point number between 0 and max_delay
    k = random.uniform(0, max_delay)
    
    # Asynchronously wait (non-blocking) for 'i' seconds
    await asyncio.sleep(k)
    
    # Return the random float value
    return k
