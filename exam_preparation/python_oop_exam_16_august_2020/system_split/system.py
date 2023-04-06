from exam_preparation.python_oop_exam_16_august_2020.system_split.hardware.heavy_hardware import HeavyHardware
from exam_preparation.python_oop_exam_16_august_2020.system_split.hardware.power_hardware import PowerHardware
from exam_preparation.python_oop_exam_16_august_2020.system_split.software.express_software import ExpressSoftware
from exam_preparation.python_oop_exam_16_august_2020.system_split.software.light_software import LightSoftware


class System:
    _hardware = list()
    _software = list()

    @staticmethod
    def attribute_collection_search(value, attribute, collection):
        for item in collection:
            if getattr(item, attribute) == value:
                return item

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.attribute_collection_search(hardware_name, "name", System._hardware)
        if not hardware:
            return "Hardware does not exist"

        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_software)
        System._software.append(new_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.attribute_collection_search(hardware_name, "name", System._hardware)
        if not hardware:
            return "Hardware does not exist"

        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_software)
        System._software.append(new_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.attribute_collection_search(hardware_name, "name", System._hardware)
        software = System.attribute_collection_search(software_name, "name", System._software)
        if not hardware or not software:
            return "Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory_consumption = sum(hardware.memory_used for hardware in System._hardware)
        total_capacity_taken = sum(hardware.capacity_used for hardware in System._hardware)
        total_memory = sum(hardware.memory for hardware in System._hardware)
        total_capacity = sum(hardware.capacity for hardware in System._hardware)

        output = [
            "System Analysis",
            f"Hardware Components: {len(System._hardware)}",
            f"Software Components: {len(System._software)}",
            f"Total Operational Memory: {total_memory_consumption} / {total_memory}",
            f"Total Capacity Taken: {total_capacity_taken} / {total_capacity}"
        ]
        return "\n".join(output)

    @staticmethod
    def system_split():
        output = list()

        for hardware in System._hardware:
            output.append(f"Hardware Component - {hardware.name}")
            output.append(f"Express Software Components:"
                          f" {len([sw for sw in hardware.software_components if sw.default_type == 'Express'])}")
            output.append(f"Light Software Components:"
                          f" {len([sw for sw in hardware.software_components if sw.default_type == 'Light'])}")
            output.append(f"Memory Usage: {hardware.memory_used} / {hardware.memory}")
            output.append(f"Capacity Usage: {hardware.capacity_used} / {hardware.capacity}")
            output.append(f"Type: {hardware.default_type}")
            output.append(f"Software Components: "
            f"{', '.join(sw.name for sw in hardware.software_components) if hardware.software_components else 'None'}")

        return "\n".join(output)
