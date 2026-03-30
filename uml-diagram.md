```mermaid
classDiagram
    class Task {
        +String description
        +int duration
    }

    class Owner {
        +String name
        +Pet[] pets
        +addPet(pet: Pet)
        +scheduleTask(task: Task)
        +viewAllTasks() Task[]
    }

    class Pet {
        +String name
        +String ownerName
    }

    Owner "1" *-- "0..*" Pet : owns
    Owner "0..*" --> "0..*" Task : selects
```
