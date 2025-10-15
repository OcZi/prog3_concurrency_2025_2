"""
Reader-Writer Problem Implementation
Demonstrates multiple readers and writers with proper synchronization.
"""
import threading
import time
import random


class ReaderWriter:
    def __init__(self):
        self.resource = 0
        self.readers_count = 0
        self.resource_lock = threading.Lock()
        self.readers_lock = threading.Lock()
        self.stop_event = threading.Event()
        
    def reader(self, reader_id):
        """Reader thread that reads the shared resource."""
        while not self.stop_event.is_set():
            # Entry section
            with self.readers_lock:
                self.readers_count += 1
                if self.readers_count == 1:
                    self.resource_lock.acquire()
                    
            # Critical section - reading
            print(f"Reader {reader_id}: Reading value {self.resource} (Active readers: {self.readers_count})")
            time.sleep(random.uniform(0.1, 0.3))
            
            # Exit section
            with self.readers_lock:
                self.readers_count -= 1
                if self.readers_count == 0:
                    self.resource_lock.release()
                    
            time.sleep(random.uniform(0.5, 1.0))
            
    def writer(self, writer_id):
        """Writer thread that writes to the shared resource."""
        while not self.stop_event.is_set():
            # Entry section
            self.resource_lock.acquire()
            
            # Critical section - writing
            old_value = self.resource
            self.resource += 1
            print(f"Writer {writer_id}: Updated value from {old_value} to {self.resource}")
            time.sleep(random.uniform(0.2, 0.5))
            
            # Exit section
            self.resource_lock.release()
            
            time.sleep(random.uniform(1.0, 2.0))
            
    def run(self, num_readers=3, num_writers=2, duration=5):
        """Run the reader-writer simulation."""
        print(f"Starting Reader-Writer simulation for {duration} seconds...")
        print(f"Readers: {num_readers}, Writers: {num_writers}")
        print("-" * 70)
        
        # Create reader threads
        readers = [
            threading.Thread(target=self.reader, args=(i,), name=f"Reader-{i}")
            for i in range(num_readers)
        ]
        
        # Create writer threads
        writers = [
            threading.Thread(target=self.writer, args=(i,), name=f"Writer-{i}")
            for i in range(num_writers)
        ]
        
        # Start all threads
        for t in readers + writers:
            t.start()
            
        # Run for specified duration
        time.sleep(duration)
        
        # Signal threads to stop
        self.stop_event.set()
        
        # Wait for all threads to complete
        for t in readers + writers:
            t.join()
            
        print("-" * 70)
        print(f"Reader-Writer simulation completed. Final value: {self.resource}")


if __name__ == "__main__":
    rw = ReaderWriter()
    rw.run(num_readers=3, num_writers=2, duration=5)
