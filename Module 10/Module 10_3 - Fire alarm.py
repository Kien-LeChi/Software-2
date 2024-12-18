class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor


    def floor_up(self, elevator_num):
        self.current_floor = min(self.top_floor, self.current_floor + 1)
        print(f"The elevator {elevator_num} is on floor {self.current_floor}")

    def floor_down(self, elevator_num):
        self.current_floor = max(self.bottom_floor, self.current_floor - 1)
        print(f"The elevator {elevator_num} is on floor {self.current_floor}")


    def go_to_floor(self, elevator_num, floor):
        check = True
        if floor < self.bottom_floor or floor > self.top_floor :
            print("The floor is out of range. Please try again.")
            return
        if self.current_floor == floor:
            print(f"The elevator {elevator_num} is already on floor {floor}.")
            return
        
        while self.current_floor < floor and check :
            self.floor_up(elevator_num)

        while self.current_floor > floor and check :
            self.floor_down(elevator_num)

class Building:

    def __init__(self, bottom_floor, top_floor, total_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.total_elevators = total_elevators
        self.all_elevators = []
        for i in range(total_elevators) :
            self.all_elevators.append(Elevator(bottom_floor, top_floor))


    def run_elevator(self, elevator_num, destination) :
        if elevator_num > self.total_elevators or elevator_num < 1 :
            print("Error: Out of range elevator numbers")
        else :
            self.all_elevators[elevator_num - 1].go_to_floor(elevator_num, destination)


    def fire_alarm(self) :
        for i in range(self.total_elevators) :
            self.run_elevator(i + 1, self.bottom_floor)
        print("All elevators have been evacuated")

Eiffel_Tower = Building(1, 100, 10)
Eiffel_Tower.run_elevator(2, 5)
Eiffel_Tower.run_elevator(3, 9)
Eiffel_Tower.run_elevator(8, 3)
Eiffel_Tower.run_elevator(10, 4)
Eiffel_Tower.fire_alarm()



