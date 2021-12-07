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

    def get_available_days(self, current_day):
        available_days = 0
        students = self.members
        for day in range(current_day, self.deadline):
            some_members_busy = any(
                student for student in students if student.time_slot[day] == 0)
            if(not some_members_busy):
                available_days += 1
        return available_days


def find_project_schedule(projects, n):
    # Sort projects based on the deadline and number of students required in the project
    projects = sorted(projects, key=lambda project: (
        project.deadline, -len(project.members), project.day_to_complete, ))

    # To store result (Sequence of project number)
    # Default value is 0, meaning that the student is busy on that day
    result = [0] * n

    # If there is no project, return the result
    if len(projects) == 0:
        return result

    # Iterate through all the given days
    for day in range(0, n):
        # Iterate through all the given projects
        for project_index in range(0, len(projects)):
            # If the students do not have enough time to complete a project before the deadline,
            # They should skip that project and work on another project instead.
            if(projects[project_index].get_available_days(day) < projects[project_index].day_to_complete):
                projects[project_index].day_to_complete = 0

            # Get students who work on the project
            students = projects[project_index].members

            # Get the time slot of all students in a particular day
            # To determine if all students are available to work on the project
            some_members_busy = any(
                student for student in students if student.time_slot[day] == 0)

            # If they are all available and the current date is not the project's deadline and the project has not yet finished,
            # Add the project number to the result and decrease day to complete the project by 1
            if(not some_members_busy and day <= projects[project_index].deadline and projects[project_index].day_to_complete != 0):
                result[day] = projects[project_index].project_number
                projects[project_index].day_to_complete -= 1
                break

    return result


if __name__ == "__main__":
    n = 7

    # [2, 1, 3, 3, 0, 1, 0]
    # projects = [
    #     Project(
    #         1,
    #         [
    #             Student('A', [1, 1, 1, 1, 0, 1, 1]),
    #             Student('B', [0, 1, 1, 1, 0, 1, 1]),
    #         ],
    #         2,
    #         6
    #     ),
    #     Project(
    #         2,
    #         [
    #             Student('A', [1, 1, 1, 1, 0, 1, 1]),
    #             Student('C', [1, 0, 1, 1, 0, 0, 0]),
    #         ],
    #         1,
    #         5
    #     ),
    #     Project(
    #         3,
    #         [
    #             Student('A', [1, 1, 1, 1, 0, 1, 1]),
    #             Student('B', [0, 1, 1, 1, 0, 1, 1]),
    #             Student('C', [1, 0, 1, 1, 0, 0, 0]),
    #         ],
    #         2,
    #         4
    #     ),
    # ]

    # [3, 2, 3, 1, 0, 0, 1]
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

    # [1, 1, 2, 3, 0, 0, 3] --> [1, 1, 2, 0, 0, 0, 0]: students need 3 days to complete the project
    # but the students only have 2 days.
    # projects = [
    #     Project(
    #         1,
    #         [
    #             Student('A', [1, 1, 1, 1, 0, 1, 1]),
    #             Student('B', [1, 1, 1, 1, 0, 1, 1]),
    #         ],
    #         2,
    #         4
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
    #         3,
    #         7
    #     ),
    # ]

    # [0, 1, 1, 0, 0, 0, 0]
    # projects = [
    #     Project(
    #         1,
    #         [
    #             Student('A', [1, 1, 1, 1, 0, 1, 1]),
    #             Student('B', [0, 1, 1, 1, 0, 1, 1]),
    #         ],
    #         2,
    #         6
    #     ),
    # ]

    # [0, 1, 1, 2, 1, 3, 3]
    # The schedule is [0, 2, 1, 0, 1, 1, 3] --> [0, 2, 1, 0, 1, 1, 0]: the students need 2 days to complete,
    # but they only have 1 day left.
    # projects = [
    #     Project(
    #         1,
    #         [
    #             Student('A', [0, 1, 1, 0, 1, 1, 1]),
    #         ],
    #         3,
    #         6
    #     ),
    #     Project(
    #         2,
    #         [
    #             Student('C', [1, 1, 0, 1, 0, 1, 1]),
    #             Student('D', [0, 1, 0, 1, 0, 1, 1]),
    #         ],
    #         1,
    #         5
    #     ),
    #     Project(
    #         3,
    #         [
    #             Student('A', [0, 1, 1, 0, 1, 1, 1]),
    #             Student('B', [1, 0, 1, 0, 0, 1, 1]),
    #             Student('C', [1, 1, 0, 1, 0, 1, 1]),
    #             Student('D', [0, 1, 0, 1, 0, 1, 1]),
    #         ],
    #         2,
    #         7
    #     ),
    # ]

    # [1, 0, 1, 2, 0, 0, 0] --> [1, 0, 1, 2, 0, 0, 0]: the students need 5 days to complete project 1 but only have 3 days
    # and need 2 days to complete project 1 but only have 1 day. Skipping project 3 gives the optimal solution.
    projects = [
        Project(
            1,
            [
                Student('A', [1, 1, 1, 1, 0, 1, 1]),
                Student('B', [1, 1, 1, 1, 0, 1, 1]),
                Student('C', [1, 0, 1, 1, 0, 0, 1]),
            ],
            2,
            7
        ),
        Project(
            2,
            [
                Student('C', [1, 0, 1, 1, 0, 0, 1]),
                Student('D', [0, 1, 0, 1, 0, 1, 1]),
            ],
            1,
            5
        ),
        Project(
            3,
            [
                Student('A', [1, 1, 1, 1, 0, 1, 1]),
                Student('B', [1, 1, 1, 1, 0, 1, 1]),
                Student('C', [1, 0, 1, 1, 0, 0, 1]),
            ],
            5,
            4
        ),
    ]

    print(f'The schedule is {find_project_schedule(projects, n)}')
