from fsm.state import CarState


class VehicleController:
    def __init__(self):
        # 현재 차량 명령 상태
        self.speed = 0
        self.steering = 0

    def control(self, state: CarState) -> dict:
        """
        FSM 상태를 받아 실제 차량 제어 명령으로 변환
        반환값은 나중에 CAN / ROS2 / UART로 그대로 보낼 수 있음
        """

        if state == CarState.IDLE:
            self.speed = 0
            self.steering = 0

        elif state == CarState.NORMAL_DRIVE:
            self.speed = 30       # 기본 주행 속도
            self.steering = 0

        elif state == CarState.OBSTACLE_AVOID:
            self.speed = 15
            self.steering = 20    # 임시: 오른쪽 회피

        elif state == CarState.STOP:
            self.speed = 0
            self.steering = 0

        elif state == CarState.EMERGENCY:
            self.speed = 0
            self.steering = 0

        return {
            "speed": self.speed,
            "steering": self.steering
        }
