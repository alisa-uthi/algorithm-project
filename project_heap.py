import heapq


class Student:
    def __init__(self, name, time_slot):
        self.name = name
        self.time_slot = time_slot


class Project:
    def __init__(self, project_number, members, day_to_complete, deadline):
        self.project_number = project_number
        self.members = members
        self.day_to_complete = day_to_complete
        self.deadline = deadline


# Program to find the maximum profit
# job sequence from a given array
# of jobs with deadlines and profits


def printJobScheduling(arr, n):
    # sorting the array on the
    # basis of their deadlines
    arr = sorted(arr, key=lambda project: -len(project.members))

    # initialise the result array and maxHeap
    result = []
    maxHeap = []

    # starting the iteration from the end
    for i in range(n - 1, -1, -1):

        # calculate slots between two deadlines
        if i == 0:
            slots_available = arr[i].deadline
        else:
            slots_available = arr[i].deadline - arr[i - 1].deadline

        # include the profit of job(as priority), deadline
        # and job_id in maxHeap
        # note we push negative value in maxHeap to convert
        # min heap to max heap in python
        heapq.heappush(maxHeap, arr[i])

        while slots_available and maxHeap:

            # get the job with max_profit
            project = heapq.heappop(maxHeap)

            # reduce the slots
            slots_available -= 1

            # include the job in the result array
            result.append(project.project_number)

    # jobs included might be shuffled
    # sort the result array by their deadlines
    result.sort(key=lambda x: x[1])

    for job in result:
        print(job[0], end=" ")
    print()


# # Driver COde
# arr = [['a', 2, 100],  # Job Array
#        ['b', 1, 19],
#        ['c', 2, 27],
#        ['d', 1, 25],
#        ['e', 3, 15]]

# print("Following is maximum profit sequence of jobs")

# # Function Call
# printJobScheduling(arr)

# This code is contributed
# by Shivam Bhagat

if __name__ == "__main__":
    n = 7
    projects = [
        Project(
            1,
            [
                Student('A', [1, 1, 1, 1, 0, 1, 1]),
                Student('B', [0, 1, 1, 1, 0, 1, 1]),
            ],
            2,
            6
        ),
        Project(
            2,
            [
                Student('A', [1, 1, 1, 1, 0, 1, 1]),
                Student('C', [1, 0, 1, 1, 0, 0, 0]),
            ],
            1,
            5
        ),
        Project(
            3,
            [
                Student('A', [1, 1, 1, 1, 0, 1, 1]),
                Student('B', [0, 1, 1, 1, 0, 1, 1]),
                Student('C', [1, 0, 1, 1, 0, 0, 0]),
            ],
            2,
            4
        ),
    ]

    # Sort projects based on number of students required in the project in descending order
    projects = sorted(projects, key=lambda project: -len(project.members))

    print(f'The schedule is {printJobScheduling(projects, n)}')
    print("Runtime is O(n * m * k).... T^T")
