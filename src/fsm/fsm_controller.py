from fsm.state import CarState

class FSMController:
    def __init__(self):
        self.current_state = CarState.IDLE

    def update(self, perception: dict) -> CarState:
        if self.current_state == CarState.IDLE:
            self.current_state = CarState.NORMAL_DRIVE

        elif self.current_state == CarState.NORMAL_DRIVE:
            if perception.get("emergency"):
                self.current_state = CarState.EMERGENCY
            elif perception.get("obstacle"):
                self.current_state = CarState.OBSTACLE_AVOID
            elif perception.get("stop_sign"):
                self.current_state = CarState.STOP

        elif self.current_state == CarState.OBSTACLE_AVOID:
            if not perception.get("obstacle"):
                self.current_state = CarState.NORMAL_DRIVE

        elif self.current_state == CarState.STOP:
            if perception.get("go"):
                self.current_state = CarState.NORMAL_DRIVE

        elif self.current_state == CarState.EMERGENCY:
            pass

        return self.current_state
