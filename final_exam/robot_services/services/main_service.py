from final_exam.robot_services.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, self.default_capacity_for_type)

    @property
    def default_capacity_for_type(self):
        return 30

    @property
    def type_of_service(self):
        return "Main Service"
