import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
st.markdown("### Add Pet")

# Pet inputs matching the Pet dataclass fields
pet_name = st.text_input("Pet name", value="Mochi")
pet_age = st.number_input("Pet age", min_value=0, max_value=50, value=2)

# ADDED: Uses owner.add_pet() from pawpal_system.py to create and store a Pet
# on the Owner object in session state.
if st.button("Add Pet"):
    if "owner" not in st.session_state:
        st.warning("Please set an owner first.")
    else:
        pet = Pet(name=pet_name, age=pet_age, owner=st.session_state.owner)
        st.session_state.owner.add_pet(pet)
        st.success(f"Pet '{pet_name}' added to {st.session_state.owner.name}.")

# Display all pets currently stored on the owner
if "owner" in st.session_state and st.session_state.owner.pets:
    st.write("Current pets:")
    st.table([{"Name": p.name, "Age": p.age} for p in st.session_state.owner.pets])

# ADDED: Button to explicitly create and store the Owner in session state.
# Using a button instead of auto-initializing ensures the owner is only created
# when the user confirms, so name changes in the text input are captured correctly.
if st.button("Set Owner"):
    st.session_state.owner = Owner(name=owner_name)
    st.session_state.scheduler = Scheduler()
    st.success(f"Owner '{owner_name}' saved to session.")

# ADDED: Show the currently stored owner so the user knows what is in the session.
if "owner" in st.session_state:
    st.info(f"Current owner: {st.session_state.owner.name}")

st.markdown("### Add Task")
st.caption("Assign a task to one of the owner's pets.")

# Task inputs matching the Task dataclass fields
col1, col2 = st.columns(2)
with col1:
    task_description = st.text_input("Task description", value="Morning walk")
    task_time = st.text_input("Time", value="08:00 AM")
with col2:
    task_duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    task_frequency = st.selectbox("Frequency", ["daily", "weekly", "monthly"])

# ADDED: Uses owner.schedule_task() which calls pet.add_task() from pawpal_system.py.
# Requires an owner to be set in session state first.
if st.button("Add task"):
    if "owner" not in st.session_state:
        st.warning("Please set an owner first.")
    elif not st.session_state.owner.pets:
        st.warning("Please add a pet to the owner before scheduling tasks.")
    else:
        # Assign task to the first pet for now
        pet = st.session_state.owner.pets[0]
        task = Task(
            description=task_description,
            duration=task_duration,
            frequency=task_frequency,
            time=task_time,
        )
        # Calls pet.add_task() internally via Owner.schedule_task()
        st.session_state.owner.schedule_task(pet, task)
        st.success(f"Task '{task_description}' added to {pet.name}.")

# Display all tasks currently stored across all pets
all_tasks = []
if "owner" in st.session_state:
    for pet in st.session_state.owner.pets:
        for task in pet.tasks:
            all_tasks.append({"Pet": pet.name, "Task": task.description, "Time": task.time, "Duration": task.duration, "Frequency": task.frequency})

if all_tasks:
    st.write("Current tasks:")
    st.table(all_tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.warning(
        "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
    )
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )
