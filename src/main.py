from fsm.fsm_controller import FSMController
from control.vehicle_controller import VehicleController
from perception.perception_manager import PerceptionManager
from can.can_interface import CANInterface
from can.can_message import ControlCommand, PerceptionMessage


def main():
    fsm = FSMController()
    controller = VehicleController()
    perception_mgr = PerceptionManager()
    can = CANInterface()

    # 테스트 시나리오
    test_sequence = [
        {"ai": {"obstacle": False}},
        {"ai": {"obstacle": True}},
        {"ai": {"obstacle": False}},
        {"ai": {"stop_sign": True}},
        {"signal": {"go": True}},
        {"signal": {"emergency": True}},
    ]

    for i, step in enumerate(test_sequence):
        # 1️⃣ Perception 입력
        if "ai" in step:
            perception_mgr.update_from_ai(step["ai"])
        if "signal" in step:
            perception_mgr.update_from_signal(step["signal"])

        perception = perception_mgr.get_perception()

        # 2️⃣ FSM
        state = fsm.update(perception)

        # 3️⃣ Control
        cmd = controller.control(state)
        control_msg = ControlCommand(
            speed=cmd["speed"],
            steering=cmd["steering"]
        )

        # 4️⃣ CAN 송신
        can.send(control_msg.to_can_frame())

        # 5️⃣ Mock CAN Loopback
        can.loopback()

        # 6️⃣ CAN 수신 → Perception (확장용)
        rx = can.receive()
        if rx and rx["can_id"] == 0x200:
            p_msg = PerceptionMessage.from_can_frame(rx)
            perception_mgr.update_from_signal(p_msg.__dict__)

        print(
            f"[{i}] State={state.name}, "
            f"Speed={cmd['speed']}, Steering={cmd['steering']}"
        )


if __name__ == "__main__":
    main()
