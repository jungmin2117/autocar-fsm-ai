from dataclasses import dataclass

# 실제 차량 기준처럼 CAN ID 정의
CAN_ID_CONTROL_CMD = 0x100
CAN_ID_PERCEPTION = 0x200


@dataclass
class ControlCommand:
    speed: int        # km/h
    steering: int     # degree

    def to_can_frame(self) -> dict:
        """
        CAN frame 형태로 변환 (Mock)
        """
        return {
            "can_id": CAN_ID_CONTROL_CMD,
            "data": {
                "speed": self.speed,
                "steering": self.steering
            }
        }


@dataclass
class PerceptionMessage:
    obstacle: bool
    stop_sign: bool
    emergency: bool

    @staticmethod
    def from_can_frame(frame: dict):
        data = frame["data"]
        return PerceptionMessage(
            obstacle=data.get("obstacle", False),
            stop_sign=data.get("stop_sign", False),
            emergency=data.get("emergency", False)
        )
