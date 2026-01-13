from enum import Enum, auto

class CarState(Enum):
    IDLE = auto()               # 대기 상태
    NORMAL_DRIVE = auto()       # 정상 주행
    OBSTACLE_AVOID = auto()     # 장애물 회피
    STOP = auto()               # 정지   
    EMERGENCY = auto()          # 비상 상태
