# Program to find the maximum profit
# job sequence from a given array
# of jobs with deadlines and profits

# function to schedule the jobs take 2
# arguments array and no of jobs to schedule

import heapq

# O(n^2)


def print_job_scheduling(arr, t):

    # length of array
    n = len(arr)

    # Sort all jobs according to
    # decreasing order of profit
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # To keep track of free time slots
    result = [False] * t

    # To store result (Sequence of jobs)
    job = ['-1'] * t

    # Iterate through all given jobs
    for i in range(len(arr)):

        # Find a free slot for this job
        # (Note that we start from the
        # last possible slot)
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):

            # Free slot found
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break

    # print the sequence
    print(job)


# arr[i][0] = job_id, arr[i][1] = deadline, arr[i][2] = profit
arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]


print("Following is maximum profit sequence of jobs")

# Function Call
print_job_scheduling(arr, 3)


####################################################################

# O(n log n)

def print_job_scheduling(arr):
    n = len(arr)

    # arr[i][0] = job_id, arr[i][1] = deadline, arr[i][2] = profit

    # sorting the array on the
    # basis of their deadlines
    arr.sort(key=lambda x: x[1])

    # initialise the result array and maxHeap
    result = []
    maxHeap = []

    # starting the iteration from the end
    for i in range(n - 1, -1, -1):

        # calculate slots between two deadlines
        if i == 0:
            slots_available = arr[i][1]
        else:
            slots_available = arr[i][1] - arr[i - 1][1]

        # include the profit of job(as priority), deadline
        # and job_id in maxHeap
        # note we push negative value in maxHeap to convert
        # min heap to max heap in python
        heapq.heappush(maxHeap, (-arr[i][2], arr[i][1], arr[i][0]))

        while slots_available and maxHeap:

            # get the job with max_profit
            profit, deadline, job_id = heapq.heappop(maxHeap)

            # reduce the slots
            slots_available -= 1

            # include the job in the result array
            result.append([job_id, deadline])

    # jobs included might be shuffled
    # sort the result array by their deadlines
    result.sort(key=lambda x: x[1])

    for job in result:
        print(job[0], end=" ")
    print()


# Driver COde
arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

print("Following is maximum profit sequence of jobs")

# Function Call
print_job_scheduling(arr)

# This code is contributed
# by Shivam Bhagat


# This code is contributed
# by Anubhav Raj Singh
