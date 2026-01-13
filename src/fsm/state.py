from enum import Enum, auto

class CarState(Enum):
    IDLE = auto()
    NORMAL_DRIVE = auto()
    OBSTACLE_AVOID = auto()
    STOP = auto()
    EMERGENCY = auto()
