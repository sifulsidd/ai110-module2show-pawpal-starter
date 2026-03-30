from pawpal_system import Task, Pet, Owner, Scheduler


def main():
    # Create owner
    owner = Owner(name="Alex")

    # Create pets
    buddy = Pet(name="Buddy", age=3, owner=owner)
    luna = Pet(name="Luna", age=5, owner=owner)

    # Add pets to owner
    owner.add_pet(buddy)
    owner.add_pet(luna)

    # Assign tasks to Buddy
    owner.schedule_task(buddy, Task(description="Morning walk", duration=30, frequency="daily", time="07:00 AM"))
    owner.schedule_task(buddy, Task(description="Feed breakfast", duration=10, frequency="daily", time="08:00 AM"))

    # Assign tasks to Luna
    owner.schedule_task(luna, Task(description="Vet checkup", duration=60, frequency="monthly", time="10:00 AM"))
    owner.schedule_task(luna, Task(description="Evening walk", duration=20, frequency="daily", time="06:00 PM"))
    owner.schedule_task(luna, Task(description="Bath time", duration=45, frequency="weekly", time="02:00 PM"))

    # Use Scheduler to retrieve and display tasks
    scheduler = Scheduler()

    print("=" * 40)
    print("        TODAY'S SCHEDULE")
    print("=" * 40)

    tasks_by_pet = scheduler.get_tasks_by_pet(owner)
    for pet_name, tasks in tasks_by_pet.items():
        print(f"\n{pet_name}:")
        for task in tasks:
            print(f"  - {task}")

    print("\n" + "=" * 40)
    print(f"Total tasks:   {len(scheduler.get_all_tasks(owner))}")
    print(f"Pending tasks: {len(scheduler.get_pending_tasks(owner))}")
    print("=" * 40)


if __name__ == "__main__":
    main()
