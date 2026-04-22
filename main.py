"""
main.py — the PRODUCER
Run this after starting the worker in another terminal.
"""
from tasks import add, multiply, divide


def demo_add():
    print("\n" + "="*50)
    print("DEMO 1 — Basic addition with .delay()")
    print("="*50)

    # Send the task to RabbitMQ — returns INSTANTLY
    result = add.delay(10, 25)

    print(f"Task sent!  ID     : {result.id}")
    print(f"            Status : {result.status}")   # PENDING

    # Block and wait for the worker to finish
    answer = result.get(timeout=30)

    print(f"            Status : {result.status}")   # SUCCESS
    print(f"            Result : {answer}")           # 35


def demo_multiply():
    print("\n" + "="*50)
    print("DEMO 2 — Multiply with .apply_async() + countdown")
    print("="*50)

    # apply_async lets us delay execution by N seconds
    result = multiply.apply_async(args=[6, 7], countdown=3)

    print(f"Task sent!  ID     : {result.id}")
    print(f"            (worker will start in ~3 seconds)")

    answer = result.get(timeout=30)
    print(f"            Result : {answer}")           # 42


def demo_multiple_tasks():
    print("\n" + "="*50)
    print("DEMO 3 — Send 5 additions in parallel")
    print("="*50)

    pairs  = [(1, 2), (10, 20), (100, 200), (7, 3), (50, 50)]
    results = [add.delay(x, y) for x, y in pairs]

    print(f"Sent {len(results)} tasks at once!\n")

    for i, (res, (x, y)) in enumerate(zip(results, pairs), 1):
        answer = res.get(timeout=30)
        print(f"  Task {i}: {x} + {y} = {answer}")


def demo_check_status():
    print("\n" + "="*50)
    print("DEMO 4 — Polling status without blocking")
    print("="*50)
    import time

    result = add.delay(99, 1)
    print(f"Task sent! Polling every 0.5s...\n")

    while not result.ready():
        print(f"  Status: {result.status} ...")
        time.sleep(0.5)

    print(f"  Status: {result.status}")
    print(f"  Result: {result.result}")


if __name__ == '__main__':
    demo_add()
    demo_multiply()
    demo_multiple_tasks()
    demo_check_status()