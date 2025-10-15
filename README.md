# CS2013: Concurrency

A comprehensive demonstration of concurrency concepts and synchronization techniques in Python.

## Overview

This project demonstrates fundamental concurrency patterns and thread synchronization techniques commonly taught in computer science courses. It includes practical implementations of:

1. **Producer-Consumer Pattern** - Thread synchronization using queues
2. **Thread Pool** - Parallel task execution
3. **Reader-Writer Problem** - Multiple readers and writers with proper locking
4. **Deadlock Prevention** - Demonstrates safe lock ordering

## Project Structure

```
.
├── main.py                  # Main entry point with interactive menu
├── producer_consumer.py     # Producer-Consumer pattern implementation
├── thread_pool.py           # Thread pool demonstration
├── reader_writer.py         # Reader-Writer problem implementation
├── deadlock_demo.py         # Deadlock prevention demonstration
├── test_concurrency.py      # Unit tests for all modules
└── README.md                # This file
```

## Requirements

- Python 3.6 or higher
- Standard library only (no external dependencies)

## Running the Program

### Interactive Mode

Run the main program to access an interactive menu:

```bash
python main.py
```

This will present a menu where you can:
- Run individual demonstrations
- Run all demonstrations sequentially
- Exit the program

### Running Individual Modules

Each module can be run independently:

```bash
# Producer-Consumer Pattern
python producer_consumer.py

# Thread Pool Example
python thread_pool.py

# Reader-Writer Problem
python reader_writer.py

# Deadlock Prevention
python deadlock_demo.py
```

## Running Tests

Execute the test suite to verify all concurrency implementations:

```bash
python -m pytest test_concurrency.py -v
```

Or using unittest:

```bash
python -m unittest test_concurrency.py -v
```

## Concurrency Patterns Explained

### 1. Producer-Consumer Pattern

Demonstrates how multiple producer threads can add items to a shared buffer while consumer threads remove and process those items. Uses:
- `queue.Queue` for thread-safe buffer
- Thread synchronization to prevent race conditions
- Proper cleanup with stop events

**Key Concepts:**
- Thread-safe data structures
- Bounded buffer management
- Producer-consumer synchronization

### 2. Thread Pool

Shows how to efficiently execute multiple tasks in parallel using a thread pool. Uses:
- `concurrent.futures.ThreadPoolExecutor`
- Task submission and result collection
- Efficient resource utilization

**Key Concepts:**
- Parallel processing
- Thread reuse
- Future objects for result handling

### 3. Reader-Writer Problem

Implements the classic reader-writer synchronization problem where:
- Multiple readers can access the resource simultaneously
- Writers must have exclusive access
- Uses locks to coordinate access

**Key Concepts:**
- Shared resource access
- Reader-writer locks
- Critical sections

### 4. Deadlock Prevention

Demonstrates deadlock prevention through consistent lock ordering:
- Shows how deadlocks can occur with improper lock ordering
- Demonstrates safe execution with consistent lock ordering
- Emphasizes the importance of lock hierarchy

**Key Concepts:**
- Deadlock conditions
- Lock ordering
- Deadlock prevention strategies

## Learning Objectives

After running these demonstrations, you should understand:

1. **Thread Synchronization** - How to coordinate multiple threads safely
2. **Race Conditions** - What they are and how to prevent them
3. **Locks and Mutexes** - Using locks for mutual exclusion
4. **Thread-Safe Data Structures** - When and how to use them
5. **Deadlock Prevention** - Strategies to avoid deadlocks
6. **Parallel Processing** - Efficient task distribution across threads

## Expected Output

Each demonstration produces output showing:
- Thread activity and state changes
- Resource access patterns
- Synchronization events
- Completion status

The output is designed to be educational, showing exactly what happens during concurrent execution.

## Common Issues and Solutions

### Timing Issues

Some demonstrations use `time.sleep()` to simulate work and make race conditions visible. Adjust timing parameters if demonstrations run too quickly or slowly.

### Thread Cleanup

All demonstrations properly clean up threads using:
- Stop events to signal termination
- `join()` to wait for thread completion
- Context managers for resource management

## Extensions and Exercises

Consider extending this project by:

1. Adding more synchronization patterns (e.g., Semaphores, Barriers)
2. Implementing the Dining Philosophers problem
3. Creating a thread-safe data structure from scratch
4. Adding performance benchmarks
5. Implementing process-based parallelism with `multiprocessing`

## License

This is an educational project for CS2013: Concurrency course.

## Author

Educational demonstration project for concurrent programming concepts.