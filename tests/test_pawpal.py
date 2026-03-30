import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pawpal_system import Task, Pet, Owner


def test_task_completion():
    task = Task(description="Morning walk", duration=30, frequency="daily", time="07:00 AM")
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_task_addition():
    owner = Owner(name="Alex")
    buddy = Pet(name="Buddy", age=3, owner=owner)
    task = Task(description="Feed breakfast", duration=10, frequency="daily", time="08:00 AM")

    assert len(buddy.tasks) == 0
    buddy.add_task(task)
    assert len(buddy.tasks) == 1
