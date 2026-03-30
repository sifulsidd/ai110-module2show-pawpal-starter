import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from datetime import timedelta
from pawpal_system import Task, Pet, Owner


def test_task_completion():
    # Daily task: mark_complete should flag it done and return next day's occurrence
    daily_task = Task(description="Morning walk", duration=30, frequency="daily", time="07:00 AM")
    assert daily_task.completed is False
    next_task = daily_task.mark_complete()
    assert daily_task.completed is True
    assert next_task is not None
    assert next_task.date == daily_task.date + timedelta(days=1)
    assert next_task.completed is False

    # Weekly task: next occurrence should be 7 days out
    weekly_task = Task(description="Bath time", duration=45, frequency="weekly", time="02:00 PM")
    next_task = weekly_task.mark_complete()
    assert weekly_task.completed is True
    assert next_task is not None
    assert next_task.date == weekly_task.date + timedelta(weeks=1)

    # Monthly task: no auto-scheduling, returns None
    monthly_task = Task(description="Vet checkup", duration=60, frequency="monthly", time="10:00 AM")
    next_task = monthly_task.mark_complete()
    assert monthly_task.completed is True
    assert next_task is None


def test_task_addition():
    owner = Owner(name="Alex")
    buddy = Pet(name="Buddy", age=3, owner=owner)
    task = Task(description="Feed breakfast", duration=10, frequency="daily", time="08:00 AM")

    assert len(buddy.tasks) == 0
    buddy.add_task(task)
    assert len(buddy.tasks) == 1

    # Completing the task and adding the next occurrence should grow the list
    next_task = task.mark_complete()
    if next_task:
        buddy.add_task(next_task)
    assert len(buddy.tasks) == 2
    assert buddy.tasks[1].completed is False
