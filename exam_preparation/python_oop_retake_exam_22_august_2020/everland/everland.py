from exam_preparation.python_oop_retake_exam_22_august_2020.everland.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = list()

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([room.room_cost + room.expenses for room in self.rooms])
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        output = list()
        rooms_to_remove = list()
        for room in self.rooms:
            cost = room.room_cost + room.expenses
            if room.budget >= cost:
                room.budget -= cost
                output.append(f"{room.family_name} paid {cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                rooms_to_remove.append(room)
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        for room in rooms_to_remove:
            self.rooms.remove(room)

        return "\n".join(output)

    def status(self):
        all_people_in_the_hotel = sum(room.members_count for room in self.rooms)
        output = [f"Total population: {all_people_in_the_hotel}"]
        for room in self.rooms:
            output.append(f"{room.family_name} with {room.members_count} members."
                          f" Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.children:
                for i in range(len(room.children)):
                    output.append(f"--- Child {i+1} monthly cost: {room.children[i].get_monthly_expense():.2f}$")

            if room.appliances:
                output.append(f"--- Appliances monthly cost:"
                              f" {sum(appliance.get_monthly_expense() for appliance in room.appliances):.2f}$")

        return "\n".join(output)
