"""
Deadlock Demonstration and Prevention
Shows how deadlocks can occur and how to prevent them.
"""
import threading
import time


class DeadlockDemo:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        
    def thread1_bad(self):
        """Thread that can cause deadlock."""
        print("Thread 1: Attempting to acquire lock1...")
        with self.lock1:
            print("Thread 1: Acquired lock1")
            time.sleep(0.1)  # Simulate some work
            print("Thread 1: Attempting to acquire lock2...")
            with self.lock2:
                print("Thread 1: Acquired lock2")
                print("Thread 1: Both locks acquired!")
                
    def thread2_bad(self):
        """Thread that can cause deadlock (acquires locks in opposite order)."""
        print("Thread 2: Attempting to acquire lock2...")
        with self.lock2:
            print("Thread 2: Acquired lock2")
            time.sleep(0.1)  # Simulate some work
            print("Thread 2: Attempting to acquire lock2...")
            with self.lock1:
                print("Thread 2: Acquired lock1")
                print("Thread 2: Both locks acquired!")
                
    def thread1_good(self):
        """Thread with proper lock ordering."""
        print("Thread 1 (Safe): Attempting to acquire lock1...")
        with self.lock1:
            print("Thread 1 (Safe): Acquired lock1")
            time.sleep(0.1)
            print("Thread 1 (Safe): Attempting to acquire lock2...")
            with self.lock2:
                print("Thread 1 (Safe): Acquired lock2")
                print("Thread 1 (Safe): Both locks acquired!")
                
    def thread2_good(self):
        """Thread with proper lock ordering (same order as thread1)."""
        print("Thread 2 (Safe): Attempting to acquire lock1...")
        with self.lock1:
            print("Thread 2 (Safe): Acquired lock1")
            time.sleep(0.1)
            print("Thread 2 (Safe): Attempting to acquire lock2...")
            with self.lock2:
                print("Thread 2 (Safe): Acquired lock2")
                print("Thread 2 (Safe): Both locks acquired!")
                
    def demonstrate_deadlock_prevention(self):
        """Demonstrates deadlock prevention with consistent lock ordering."""
        print("Demonstrating SAFE execution (consistent lock ordering)...")
        print("-" * 70)
        
        t1 = threading.Thread(target=self.thread1_good, name="Thread-1-Safe")
        t2 = threading.Thread(target=self.thread2_good, name="Thread-2-Safe")
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
        
        print("-" * 70)
        print("Safe execution completed successfully!")


if __name__ == "__main__":
    demo = DeadlockDemo()
    print("=== Deadlock Prevention Demo ===\n")
    demo.demonstrate_deadlock_prevention()
