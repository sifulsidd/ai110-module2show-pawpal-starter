from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    duration: int
    frequency: str
    time: str
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def __str__(self) -> str:
        """Return a formatted string summary of the task."""
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.description} at {self.time} ({self.duration} mins, {self.frequency})"


@dataclass
class Pet:
    name: str
    age: int
    owner: Owner
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def get_pending_tasks(self) -> list[Task]:
        """Return all incomplete tasks for this pet."""
        return [task for task in self.tasks if not task.completed]

    def __str__(self) -> str:
        """Return the pet's name and age as a string."""
        return f"{self.name} (age {self.age})"


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's list of pets."""
        self.pets.append(pet)

    def schedule_task(self, pet: Pet, task: Task):
        """Assign a task to a specific pet."""
        pet.add_task(task)

    def view_all_tasks(self) -> list[Task]:
        """Return a flat list of all tasks across all owned pets."""
        return [task for pet in self.pets for task in pet.tasks]

    def __str__(self) -> str:
        """Return the owner's name and number of pets as a string."""
        return f"Owner: {self.name} ({len(self.pets)} pets)"


@dataclass
class Scheduler:
    def get_all_tasks(self, owner: Owner) -> list[Task]:
        """Retrieve every task across all of the owner's pets."""
        return owner.view_all_tasks()

    def get_pending_tasks(self, owner: Owner) -> list[Task]:
        """Return only incomplete tasks across all of the owner's pets."""
        return [task for task in self.get_all_tasks(owner) if not task.completed]

    def get_tasks_by_pet(self, owner: Owner) -> dict[str, list[Task]]:
        """Return tasks grouped by pet name."""
        return {pet.name: pet.tasks for pet in owner.pets}

    def get_tasks_by_frequency(self, owner: Owner, frequency: str) -> list[Task]:
        """Return all tasks matching the given frequency across all pets."""
        return [task for task in self.get_all_tasks(owner) if task.frequency == frequency]
