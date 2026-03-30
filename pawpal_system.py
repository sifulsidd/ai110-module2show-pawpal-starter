from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    duration: int
    frequency: str
    completed: bool = False

    def mark_complete(self):
        self.completed = True

    def __str__(self) -> str:
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.description} ({self.duration} mins, {self.frequency})"


@dataclass
class Pet:
    name: str
    age: int
    owner: Owner
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        self.tasks.append(task)

    def get_pending_tasks(self) -> list[Task]:
        return [task for task in self.tasks if not task.completed]

    def __str__(self) -> str:
        return f"{self.name} (age {self.age})"


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        self.pets.append(pet)

    def schedule_task(self, pet: Pet, task: Task):
        pet.add_task(task)

    def view_all_tasks(self) -> list[Task]:
        return [task for pet in self.pets for task in pet.tasks]

    def __str__(self) -> str:
        return f"Owner: {self.name} ({len(self.pets)} pets)"


@dataclass
class Scheduler:
    def get_all_tasks(self, owner: Owner) -> list[Task]:
        return owner.view_all_tasks()

    def get_pending_tasks(self, owner: Owner) -> list[Task]:
        return [task for task in self.get_all_tasks(owner) if not task.completed]

    def get_tasks_by_pet(self, owner: Owner) -> dict[str, list[Task]]:
        return {pet.name: pet.tasks for pet in owner.pets}

    def get_tasks_by_frequency(self, owner: Owner, frequency: str) -> list[Task]:
        return [task for task in self.get_all_tasks(owner) if task.frequency == frequency]