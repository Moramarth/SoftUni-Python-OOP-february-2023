from classes_and_objects.exercise_05_to_do_list.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = list()

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        for current_task in self.tasks:
            if current_task.name == task_name:
                current_task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        completed = 0
        for current_task in self.tasks:
            if current_task.completed:
                completed += 1
                self.tasks.remove(current_task)
        return f"Cleared {completed} tasks."

    def view_section(self) -> str:
        info = [f"Section {self.name}:"]
        for current_task in self.tasks:
            result = current_task.details()
            info.append(result)
        return "\n".join(info)
