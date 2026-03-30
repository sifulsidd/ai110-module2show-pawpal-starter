from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Task:
    description: str
    duration: int


@dataclass
class Pet:
    name: str
    owner: Owner


@dataclass
class Owner:
    name: str
    pets: list[Pet] = field(default_factory=list)
    tasks: list[Task] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        pass

    def schedule_task(self, task: Task):
        pass

    def view_all_tasks(self) -> list[Task]:
        pass
