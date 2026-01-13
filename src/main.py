from fsm.fsm_controller import FSMController

def main():
    fsm = FSMController()

    test_sequence = [
        {"obstacle": False},
        {"obstacle": True},
        {"obstacle": False},
        {"stop_sign": True},
        {"go": True},
    ]

    for i, perception in enumerate(test_sequence):
        state = fsm.update(perception)
        print(f"[{i}] FSM State: {state.name}")

if __name__ == "__main__":
    main()
