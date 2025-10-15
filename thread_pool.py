"""
Thread Pool Implementation
Demonstrates parallel processing using thread pools.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random


def process_task(task_id):
    """Simulates a task that takes some time to complete."""
    processing_time = random.uniform(0.5, 2.0)
    print(f"Task {task_id}: Starting (will take {processing_time:.2f}s)")
    time.sleep(processing_time)
    result = task_id * task_id
    print(f"Task {task_id}: Completed with result {result}")
    return result


def run_thread_pool_demo(num_tasks=10, max_workers=4):
    """Demonstrates thread pool execution."""
    print(f"Running Thread Pool demo with {num_tasks} tasks and {max_workers} workers")
    print("-" * 70)
    
    start_time = time.time()
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        futures = {executor.submit(process_task, i): i for i in range(num_tasks)}
        
        # Process completed tasks
        for future in as_completed(futures):
            task_id = futures[future]
            try:
                result = future.result()
                results.append((task_id, result))
            except Exception as e:
                print(f"Task {task_id} generated an exception: {e}")
                
    end_time = time.time()
    
    print("-" * 70)
    print(f"All tasks completed in {end_time - start_time:.2f} seconds")
    print(f"Results: {sorted(results)}")
    return results


if __name__ == "__main__":
    run_thread_pool_demo(num_tasks=10, max_workers=4)
