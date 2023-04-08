from final_exam.robot_services.robots.female_robot import FemaleRobot
from final_exam.robot_services.robots.male_robot import MaleRobot
from final_exam.robot_services.services.main_service import MainService
from final_exam.robot_services.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots = list()  # stores instances of class BaseRobot
        self.services = list()  # stores instances of class BaseService

    @staticmethod
    def attribute_collection_search(value, attribute, collection):
        for item in collection:
            if getattr(item, attribute) == value:
                return item

    @property
    def valid_service_types(self):
        return {
            "MainService": MainService,
            "SecondaryService": SecondaryService,
        }

    @property
    def valid_robot_types(self):
        return {
            "MaleRobot": MaleRobot,
            "FemaleRobot": FemaleRobot,
        }

    def add_service(self, service_type: str, name: str):
        if service_type not in self.valid_service_types:
            raise Exception("Invalid service type!")

        self.services.append(self.valid_service_types[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.valid_robot_types:
            raise Exception("Invalid robot type!")

        self.robots.append(self.valid_robot_types[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.attribute_collection_search(robot_name, "name", self.robots)
        service = self.attribute_collection_search(service_name, "name", self.services)

        if (robot.type_of_robot == "Male" and service.type_of_service == "Secondary Service") \
                or (robot.type_of_robot == "Female" and service.type_of_service == "Main Service"):
            return "Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.attribute_collection_search(service_name, "name", self.services)
        robot = self.attribute_collection_search(robot_name, "name", service.robots)
        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.attribute_collection_search(service_name, "name", self.services)
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.attribute_collection_search(service_name, "name", self.services)
        total_price = sum(robot.price for robot in service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        output = list()
        for service in self.services:
            output.append(service.details())

        return "\n".join(output)
