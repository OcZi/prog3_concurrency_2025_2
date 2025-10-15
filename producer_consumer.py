"""
Producer-Consumer Pattern Implementation
Demonstrates thread synchronization using queues and locks.
"""
import threading
import queue
import time
import random


class ProducerConsumer:
    def __init__(self, queue_size=10, num_producers=2, num_consumers=3):
        self.buffer = queue.Queue(maxsize=queue_size)
        self.num_producers = num_producers
        self.num_consumers = num_consumers
        self.stop_event = threading.Event()
        
    def producer(self, producer_id):
        """Producer thread that adds items to the buffer."""
        while not self.stop_event.is_set():
            item = random.randint(1, 100)
            try:
                self.buffer.put(item, timeout=0.5)
                print(f"Producer {producer_id}: Produced {item} (Queue size: {self.buffer.qsize()})")
                time.sleep(random.uniform(0.1, 0.5))
            except queue.Full:
                print(f"Producer {producer_id}: Queue full, waiting...")
                
    def consumer(self, consumer_id):
        """Consumer thread that removes items from the buffer."""
        while not self.stop_event.is_set():
            try:
                item = self.buffer.get(timeout=0.5)
                print(f"Consumer {consumer_id}: Consumed {item} (Queue size: {self.buffer.qsize()})")
                time.sleep(random.uniform(0.1, 0.8))
                self.buffer.task_done()
            except queue.Empty:
                if self.stop_event.is_set():
                    break
                    
    def run(self, duration=5):
        """Run the producer-consumer simulation."""
        print(f"Starting Producer-Consumer simulation for {duration} seconds...")
        print(f"Producers: {self.num_producers}, Consumers: {self.num_consumers}")
        print("-" * 70)
        
        # Create producer threads
        producers = [
            threading.Thread(target=self.producer, args=(i,), name=f"Producer-{i}")
            for i in range(self.num_producers)
        ]
        
        # Create consumer threads
        consumers = [
            threading.Thread(target=self.consumer, args=(i,), name=f"Consumer-{i}")
            for i in range(self.num_consumers)
        ]
        
        # Start all threads
        for t in producers + consumers:
            t.start()
            
        # Run for specified duration
        time.sleep(duration)
        
        # Signal threads to stop
        self.stop_event.set()
        
        # Wait for all threads to complete
        for t in producers + consumers:
            t.join()
            
        print("-" * 70)
        print("Producer-Consumer simulation completed.")


if __name__ == "__main__":
    pc = ProducerConsumer(queue_size=5, num_producers=2, num_consumers=3)
    pc.run(duration=5)
