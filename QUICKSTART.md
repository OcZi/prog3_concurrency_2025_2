# Quick Start Guide

## Installation

No installation required! This project uses only Python standard library.

Requirements:
- Python 3.6 or higher

## Usage Examples

### Option 1: Interactive Menu

```bash
python main.py
```

This will show a menu where you can select which demonstration to run.

### Option 2: Run Individual Modules

```bash
# Producer-Consumer Pattern
python producer_consumer.py

# Thread Pool
python thread_pool.py

# Reader-Writer Problem
python reader_writer.py

# Deadlock Prevention
python deadlock_demo.py
```

### Option 3: Run All Tests

```bash
python -m unittest test_concurrency.py -v
```

## What You'll Learn

1. **Producer-Consumer Pattern** - How multiple threads can safely share a buffer
2. **Thread Pools** - How to efficiently execute tasks in parallel
3. **Reader-Writer Locks** - How to allow multiple readers but exclusive writers
4. **Deadlock Prevention** - How proper lock ordering prevents deadlocks

## Example Output

When you run the Producer-Consumer pattern, you'll see output like:

```
Starting Producer-Consumer simulation for 5 seconds...
Producers: 2, Consumers: 3
----------------------------------------------------------------------
Producer 0: Produced 53 (Queue size: 1)
Consumer 0: Consumed 53 (Queue size: 0)
Producer 1: Produced 93 (Queue size: 1)
Consumer 2: Consumed 93 (Queue size: 0)
...
```

This shows threads working concurrently, with queue size changing as items are produced and consumed.

## Troubleshooting

**Q: The program seems to hang**
A: This is unlikely with the current implementation as all threads have proper cleanup. If it does happen, press Ctrl+C to exit.

**Q: Output is too fast to read**
A: Each module can be modified by adjusting the `time.sleep()` values to slow down execution.

**Q: Tests fail**
A: Make sure you're using Python 3.6 or higher. The tests are designed to be robust, but timing-related tests may occasionally fail on very slow systems.

## Next Steps

After running the demonstrations, try:
1. Modifying the number of producers/consumers/readers/writers
2. Changing the queue size in Producer-Consumer
3. Adjusting the number of workers in the Thread Pool
4. Adding your own synchronization patterns

## Support

This is an educational project. For questions about concurrency concepts, refer to your CS2013 course materials.
