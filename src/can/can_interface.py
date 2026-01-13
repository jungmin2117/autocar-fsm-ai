import queue
from typing import Optional


class CANInterface:
    """
    CAN 송수신 인터페이스
    - 현재: Mock CAN (Queue 기반)
    - 나중에: socketCAN / vendor API로 교체
    """

    def __init__(self):
        # 송신 / 수신 큐 (Mock CAN Bus)
        self.tx_queue = queue.Queue()
        self.rx_queue = queue.Queue()

    def send(self, frame: dict):
        """
        CAN Frame 송신
        frame 예:
        {
            "can_id": 0x100,
            "data": {...}
        }
        """
        print(f"[CAN TX] ID={hex(frame['can_id'])}, DATA={frame['data']}")
        self.tx_queue.put(frame)

    def receive(self) -> Optional[dict]:
        """
        CAN Frame 수신 (있으면 반환, 없으면 None)
        """
        if not self.rx_queue.empty():
            frame = self.rx_queue.get()
            print(f"[CAN RX] ID={hex(frame['can_id'])}, DATA={frame['data']}")
            return frame
        return None

    # ============================
    # 아래는 Mock용 기능 (테스트용)
    # ============================

    def loopback(self):
        """
        송신된 프레임을 다시 수신으로 보내는 Mock loopback
        실제 CAN에서는 이 부분이 하드웨어/드라이버 역할
        """
        if not self.tx_queue.empty():
            frame = self.tx_queue.get()
            self.rx_queue.put(frame)
