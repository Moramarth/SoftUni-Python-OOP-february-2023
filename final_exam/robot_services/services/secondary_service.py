from final_exam.robot_services.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str):
        super().__init__(name, self.default_capacity_for_type)

    @property
    def default_capacity_for_type(self):
        return 15

    @property
    def type_of_service(self):
        return "Secondary Service"
