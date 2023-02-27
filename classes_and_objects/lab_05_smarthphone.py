"""
Create a class called Smartphone. Upon initialization, it should receive a memory (number). It should also have 2 other
instance attributes: apps (empty list by default) and is_on (False by default).

Create 3 methods:
-	power() - sets is_on on True if the phone is off, otherwise sets it to False
-	install(app, app_memory)
o	If there is enough memory on the phone and it is on, installs the app (add it to apps and decrease the memory
of the phone) and returns "Installing {app}"
o	If there is enough memory, but the phone is off, returns "Turn on your phone to install {app}"
o	Otherwise, returns "Not enough memory to install {app}"
-	status() - returns "Total apps: {total_apps_count}. Memory left: {memory_left}"
"""


class Smartphone:
    def __init__(self, memory: float):
        self.memory = memory
        self.apps = list()
        self.is_on = False

    def power(self):
        if not self.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def install(self, app: str, app_memory: float) -> str:
        if self.is_on:
            if self.memory >= app_memory:
                self.apps.append(app)
                self.memory -= app_memory
                return f"Installing {app}"
            return f"Not enough memory to install {app}"
        return f"Turn on your phone to install {app}"

    def status(self) -> str:
        total_apps_count = len(self.apps)

        return f"Total apps: {total_apps_count}. Memory left: {self.memory}"
