"""
CS2013: Concurrency - Main Entry Point
Demonstrates various concurrency patterns and synchronization techniques.
"""
import sys
from producer_consumer import ProducerConsumer
from thread_pool import run_thread_pool_demo
from reader_writer import ReaderWriter
from deadlock_demo import DeadlockDemo


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 70)
    print("CS2013: Concurrency Demonstrations")
    print("=" * 70)
    print("1. Producer-Consumer Pattern")
    print("2. Thread Pool Example")
    print("3. Reader-Writer Problem")
    print("4. Deadlock Prevention")
    print("5. Run All Demonstrations")
    print("0. Exit")
    print("=" * 70)


def run_producer_consumer():
    """Run Producer-Consumer demonstration."""
    print("\n### PRODUCER-CONSUMER PATTERN ###\n")
    pc = ProducerConsumer(queue_size=5, num_producers=2, num_consumers=3)
    pc.run(duration=5)


def run_thread_pool():
    """Run Thread Pool demonstration."""
    print("\n### THREAD POOL EXAMPLE ###\n")
    run_thread_pool_demo(num_tasks=10, max_workers=4)


def run_reader_writer():
    """Run Reader-Writer demonstration."""
    print("\n### READER-WRITER PROBLEM ###\n")
    rw = ReaderWriter()
    rw.run(num_readers=3, num_writers=2, duration=5)


def run_deadlock_demo():
    """Run Deadlock Prevention demonstration."""
    print("\n### DEADLOCK PREVENTION ###\n")
    demo = DeadlockDemo()
    demo.demonstrate_deadlock_prevention()


def run_all():
    """Run all demonstrations."""
    demos = [
        ("Producer-Consumer Pattern", run_producer_consumer),
        ("Thread Pool Example", run_thread_pool),
        ("Reader-Writer Problem", run_reader_writer),
        ("Deadlock Prevention", run_deadlock_demo)
    ]
    
    for name, demo_func in demos:
        print(f"\n{'*' * 70}")
        print(f"Running: {name}")
        print('*' * 70)
        demo_func()
        print("\n")


def main():
    """Main program loop."""
    while True:
        print_menu()
        try:
            choice = input("\nEnter your choice (0-5): ").strip()
            
            if choice == '0':
                print("\nExiting program. Goodbye!")
                sys.exit(0)
            elif choice == '1':
                run_producer_consumer()
            elif choice == '2':
                run_thread_pool()
            elif choice == '3':
                run_reader_writer()
            elif choice == '4':
                run_deadlock_demo()
            elif choice == '5':
                run_all()
            else:
                print("\nInvalid choice. Please enter a number between 0 and 5.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
