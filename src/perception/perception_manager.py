class PerceptionManager:
    def __init__(self):
        # 초기 인식 상태
        self.data = {
            "obstacle": False,
            "stop_sign": False,
            "emergency": False,
            "go": False,
        }

    def update_from_ai(self, ai_result: dict):
        self.data.update(ai_result)

    def update_from_signal(self, signal: dict):
        self.data.update(signal)

    def get_perception(self) -> dict:
        return self.data.copy()
