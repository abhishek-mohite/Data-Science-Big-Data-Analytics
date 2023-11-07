#You are given a set of jobs, each with a deadline and a profit associated with it. 
#The goal is to schedule the jobs in a way that maximizes the total profit while ensuring 
#that each job is completed within its specified deadline. Each job can be scheduled only once.

# Define a class to represent a job with id, deadline, and profit
class Job:
    def __init__(self, id, dead, profit):
        self.id = id  # Job identifier  
        self.dead = dead  # Deadline for the job
        self.profit = profit  # Profit associated with completing the job

# Function to perform job scheduling
def jobScheduling(arr, n):
    # Sort the jobs in decreasing order of profit
    arr.sort(key=lambda x: x.profit, reverse=True)
    
    # Initialize result to store the scheduled jobs and slot to track time slots
    result = [-1] * n
    slot = [False] * n

    for i in range(n):
        # Find a suitable time slot for the current job
        for j in range(min(n, arr[i].dead) - 1, -1, -1):
            if not slot[j]:
                result[j] = i
                slot[j] = True
                break

    # Print the sequence of scheduled jobs
    for i in range(n):
        if slot[i]:
            print(arr[result[i]].id, end=" ")

if __name__ == '__main__':
    # Create a list of jobs with their respective attributes
    arr = [Job('a', 2, 100),
           Job('b', 1, 19),
           Job('c', 2, 27),
           Job('d', 1, 25),
           Job('e', 3, 15)]

    n = len(arr)
    print("Following is the maximum profit sequence of jobs")
    jobScheduling(arr, n)
