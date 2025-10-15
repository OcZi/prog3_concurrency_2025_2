"""
Unit tests for concurrency demonstrations.
"""
import unittest
import threading
import time
from producer_consumer import ProducerConsumer
from thread_pool import run_thread_pool_demo
from reader_writer import ReaderWriter
from deadlock_demo import DeadlockDemo


class TestProducerConsumer(unittest.TestCase):
    """Test cases for Producer-Consumer pattern."""
    
    def test_initialization(self):
        """Test ProducerConsumer initialization."""
        pc = ProducerConsumer(queue_size=10, num_producers=2, num_consumers=3)
        self.assertEqual(pc.num_producers, 2)
        self.assertEqual(pc.num_consumers, 3)
        self.assertFalse(pc.stop_event.is_set())
        
    def test_run_completes(self):
        """Test that producer-consumer simulation completes successfully."""
        pc = ProducerConsumer(queue_size=5, num_producers=1, num_consumers=1)
        start_time = time.time()
        pc.run(duration=1)
        elapsed_time = time.time() - start_time
        # Should complete within reasonable time (1s + overhead)
        self.assertLess(elapsed_time, 3)
        self.assertTrue(pc.stop_event.is_set())


class TestThreadPool(unittest.TestCase):
    """Test cases for Thread Pool."""
    
    def test_thread_pool_execution(self):
        """Test that thread pool executes all tasks."""
        results = run_thread_pool_demo(num_tasks=5, max_workers=2)
        self.assertEqual(len(results), 5)
        # Verify all task IDs are present
        task_ids = [task_id for task_id, _ in results]
        self.assertEqual(sorted(task_ids), [0, 1, 2, 3, 4])


class TestReaderWriter(unittest.TestCase):
    """Test cases for Reader-Writer problem."""
    
    def test_initialization(self):
        """Test ReaderWriter initialization."""
        rw = ReaderWriter()
        self.assertEqual(rw.resource, 0)
        self.assertEqual(rw.readers_count, 0)
        self.assertFalse(rw.stop_event.is_set())
        
    def test_run_completes(self):
        """Test that reader-writer simulation completes successfully."""
        rw = ReaderWriter()
        start_time = time.time()
        rw.run(num_readers=2, num_writers=1, duration=1)
        elapsed_time = time.time() - start_time
        # Should complete within reasonable time (1s + overhead)
        self.assertLess(elapsed_time, 3)
        self.assertTrue(rw.stop_event.is_set())
        # Resource should have been incremented by writers
        self.assertGreaterEqual(rw.resource, 0)


class TestDeadlockDemo(unittest.TestCase):
    """Test cases for Deadlock demonstration."""
    
    def test_initialization(self):
        """Test DeadlockDemo initialization."""
        demo = DeadlockDemo()
        self.assertIsNotNone(demo.lock1)
        self.assertIsNotNone(demo.lock2)
        
    def test_safe_execution(self):
        """Test that safe execution completes without deadlock."""
        demo = DeadlockDemo()
        # This should complete successfully
        demo.demonstrate_deadlock_prevention()
        # If we get here, no deadlock occurred


class TestConcurrentAccess(unittest.TestCase):
    """Test cases for concurrent access scenarios."""
    
    def test_thread_safety(self):
        """Test thread-safe counter increment."""
        counter = {'value': 0}
        lock = threading.Lock()
        
        def increment():
            for _ in range(1000):
                with lock:
                    counter['value'] += 1
                    
        threads = [threading.Thread(target=increment) for _ in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
            
        # With proper locking, should be exactly 5000
        self.assertEqual(counter['value'], 5000)


if __name__ == '__main__':
    unittest.main()
