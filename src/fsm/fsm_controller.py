from fsm.state import CarState


class FSMController:
    def __init__(self):
        # 현재 차량 상태
        self.current_state = CarState.IDLE

    def update(self, perception: dict) -> CarState:
       

        # 1️ 어떤 상태든 무조건 최우선으로 처리해야 하는 조건
        if perception.get("emergency", False):
            self.current_state = CarState.EMERGENCY
            return self.current_state

        # 2️ 상태별 전이 로직
        if self.current_state == CarState.IDLE:
            # 시스템 시작 후 바로 주행 상태로 전이
            self.current_state = CarState.NORMAL_DRIVE

        elif self.current_state == CarState.NORMAL_DRIVE:
            if perception.get("obstacle", False):
                self.current_state = CarState.OBSTACLE_AVOID
            elif perception.get("stop_sign", False):
                self.current_state = CarState.STOP

        elif self.current_state == CarState.OBSTACLE_AVOID:
            # 장애물이 사라지면 정상 주행 복귀
            if not perception.get("obstacle", False):
                self.current_state = CarState.NORMAL_DRIVE

        elif self.current_state == CarState.STOP:
            # 출발 신호가 들어오면 다시 주행
            if perception.get("go", False):
                self.current_state = CarState.NORMAL_DRIVE

        elif self.current_state == CarState.EMERGENCY:
            # 비상 상태는 외부 리셋 없이는 유지
            pass

        return self.current_state
