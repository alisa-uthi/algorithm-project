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


def find_project_schedule(projects, n):
    # Sort projects based on the daeadline and number of students required in the project
    projects = sorted(projects, key=lambda project: (
        project.deadline, -len(project.members)))

    # To store result (Sequence of project number)
    # Default value is 0, meaning that the student is busy on that day
    result = [0] * n

    # Iterate through all given number of days
    for day in range(0, n):
        # Iterate through all given projects
        for project_index in range(0, len(projects)):
            # Get students who work on the project
            students = projects[project_index].members

            # Get time slot of all students in a particular day
            # To determine if all students are available to do the project
            all_members_available = True
            for student_index in range(0, len(students)):
                if(not students[student_index].time_slot[day]):
                    all_members_available = False
                    break

            # If they are all available and the current date is not the project's deadline and the project has not yet finished,
            # Add the project number to the result and decrease day to complete the project by 1
            if(all_members_available and day <= projects[project_index].deadline and projects[project_index].day_to_complete != 0):
                result[day] = projects[project_index].project_number
                projects[project_index].day_to_complete -= 1
                break

    return result


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

    # projects = [
    #     Project(
    #         1,
    #         [
    #             Student('A', [1, 1, 1, 1, 0, 1, 1]),
    #             Student('B', [1, 1, 1, 1, 0, 1, 1]),
    #             Student('C', [1, 0, 1, 1, 0, 0, 1]),
    #         ],
    #         2,
    #         7
    #     ),
    #     Project(
    #         2,
    #         [
    #             Student('A', [1, 1, 1, 1, 0, 1, 1]),
    #             Student('B', [1, 1, 1, 1, 0, 1, 1]),
    #         ],
    #         1,
    #         5
    #     ),
    #     Project(
    #         3,
    #         [
    #             Student('A', [1, 1, 1, 1, 0, 1, 1]),
    #             Student('B', [1, 1, 1, 1, 0, 1, 1]),
    #             Student('C', [1, 0, 1, 1, 0, 0, 1]),
    #         ],
    #         2,
    #         4
    #     ),
    # ]

    print(f'The schedule is {find_project_schedule(projects, n)}')
    print("Runtime is O(n * m * k).... T^T")
