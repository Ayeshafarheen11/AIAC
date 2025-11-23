"""
Queue implementation (unbounded) and a few-shot prompt + modified bounded queue.

This file contains:
- Queue: a simple FIFO queue with `enqueue`, `dequeue`, and `front` methods.
- BoundedQueue: a bounded (fixed-capacity) queue that raises QueueFullError when
  trying to enqueue into a full queue.
- Custom exceptions: QueueEmptyError, QueueFullError
- A few-shot prompt demonstrating how to instruct an AI to perform the modification
  from an unbounded Queue to a bounded Queue.
- Self-test section under `if __name__ == "__main__"` with assertions and
  printed output.

This code is written to be straightforward, well-documented and easy to run.
"""
from typing import Generic, List, Optional, TypeVar

T = TypeVar('T')


class QueueEmptyError(Exception):
    """Raised when attempting to access or remove an item from an empty queue."""


class QueueFullError(Exception):
    """Raised when attempting to enqueue into a full bounded queue."""


class Queue(Generic[T]):
    """Simple FIFO queue implementation using a Python list as the backing store.

    Methods
    -------
    enqueue(item: T) -> None
        Append `item` to the tail of the queue.

    dequeue() -> T
        Remove and return the item at the head of the queue. Raises
        :class:`QueueEmptyError` if the queue is empty.

    front() -> T
        Return (but do not remove) the item at the head of the queue. Raises
        :class:`QueueEmptyError` if the queue is empty.

    size() -> int
        Return the number of items currently stored in the queue.

    is_empty() -> bool
        Return True if the queue is empty, otherwise False.
    """

    def __init__(self) -> None:
        """Initialize an empty queue."""
        # We use a plain list; append() adds to tail, pop(0) removes from head.
        # For performance-sensitive applications consider collections.deque.
        self._data: List[T] = []

    def enqueue(self, item: T) -> None:
        """Add `item` to the tail of the queue."""
        self._data.append(item)

    def dequeue(self) -> T:
        """Remove and return the item at the head of the queue.

        Raises
        ------
        QueueEmptyError
            If the queue is empty.
        """
        if not self._data:
            raise QueueEmptyError("Cannot dequeue from an empty queue")
        return self._data.pop(0)

    def front(self) -> T:
        """Return the head item without removing it.

        Raises
        ------
        QueueEmptyError
            If the queue is empty.
        """
        if not self._data:
            raise QueueEmptyError("Queue is empty")
        return self._data[0]

    def size(self) -> int:
        """Return the current number of items in the queue."""
        return len(self._data)

    def is_empty(self) -> bool:
        """Return True if the queue is empty."""
        return len(self._data) == 0


# --- Few-shot prompt (example) -------------------------------------------------
FEW_SHOT_PROMPT = """
You are given a simple Queue Python class with methods enqueue, dequeue, and front.
Modify the class so that it becomes a bounded queue with a maximum size argument
provided at construction time (max_size). If a caller attempts to enqueue when
the queue is already at max_size, raise a QueueFullError. Preserve the existing
behavior for dequeue and front (they should still raise QueueEmptyError when
appropriate).

Requirements for your modification:
- Add an optional argument `max_size: Optional[int]` to __init__ (None means
  unbounded).
- Validate that max_size, if provided, is a positive integer (> 0).
- Enqueue should raise QueueFullError if size == max_size.
- Keep clear docs and tests demonstrating the full behavior.
"""


# --- Modified: BoundedQueue ---------------------------------------------------
class BoundedQueue(Queue[T]):
    """Bounded queue that enforces a maximum capacity.

    Parameters
    ----------
    max_size: Optional[int]
        Maximum number of elements allowed in the queue. If None, the queue is
        unbounded and behaves exactly like :class:`Queue`.

    Raises
    ------
    ValueError
        If max_size is provided but is not a positive integer (> 0).
    """

    def __init__(self, max_size: Optional[int] = None) -> None:
        if max_size is not None:
            if not isinstance(max_size, int) or max_size <= 0:
                raise ValueError("max_size must be a positive integer or None")
        super().__init__()
        self._max_size: Optional[int] = max_size

    def enqueue(self, item: T) -> None:
        """Add `item` to the tail of the queue.

        Raises
        ------
        QueueFullError
            If the queue has reached its `max_size` capacity.
        """
        if self._max_size is not None and self.size() >= self._max_size:
            raise QueueFullError("Cannot enqueue to full queue (max_size={})".format(self._max_size))
        super().enqueue(item)

    # Other methods (dequeue, front, size, is_empty) inherited from Queue


# --- Test cases (unittest module) ---------------------------------------------------
import unittest


class TestQueue(unittest.TestCase):
    def test_unbounded_queue_basic(self):
        q = Queue[int]()
        self.assertTrue(q.is_empty())
        q.enqueue(10)
        q.enqueue(20)
        self.assertEqual(q.front(), 10)
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.dequeue(), 20)
        with self.assertRaises(QueueEmptyError):
            q.dequeue()

    def test_bounded_queue_full(self):
        bq = BoundedQueue[int](max_size=2)
        bq.enqueue(1)
        bq.enqueue(2)
        with self.assertRaises(QueueFullError):
            bq.enqueue(3)
        self.assertEqual(bq.front(), 1)
        self.assertEqual(bq.dequeue(), 1)
        self.assertEqual(bq.dequeue(), 2)
        with self.assertRaises(QueueEmptyError):
            bq.front()

    def test_bounded_none_behaves_unbounded(self):
        bq2 = BoundedQueue[int](max_size=None)
        for i in range(50):
            bq2.enqueue(i)
        self.assertEqual(bq2.size(), 50)

    def test_invalid_max_size(self):
        with self.assertRaises(ValueError):
            BoundedQueue(max_size=0)


if __name__ == '__main__':
    unittest.main()
