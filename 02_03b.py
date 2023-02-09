from collections import deque


class Task(object):
    def __init__(self, task_description, has_priority=False):
        self.task_description = task_description
        self.has_priority = has_priority

    def __str__(self):
        return "Task: {0}, Priority: {1} ".format(self.task_description, self.has_priority)


task_queue = deque()


def add_task(task):
    if task.has_priority:
        task_queue.appendleft(task)
    else:
        task_queue.append(task)


def do_task():
    task_queue.popleft()


def print_tasks():
    for task in task_queue:
        print(task.task_description)


def main():
    # add code here

    add_task(Task("Write List"))
    add_task(Task("Make Breakfast"))
    add_task(Task("Respond to Email", True))

    print_tasks()
    print(do_task())
    print_tasks()
    return


if __name__ == "__main__":
    main()
