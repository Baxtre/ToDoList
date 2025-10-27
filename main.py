import argparse
import json
import os
import sys

# ======================================================================
# --- GLOBAL DATA AND CONFIGURATION ---
# The primary data structure for the To-Do List (State is stored here.)
TASKS = []

# Mapping of string types in JSON to actual Python type objects for argparse.
TYPE_MAP = {
    "str": str,
    "int": int,
    "float": float,
}

# ======================================================================
# ----------------------------------------------------------------------
# --- CORE APPLICATION LOGIC ---
# These functions only deal with data, not the UI.


def add_task(title: str, tag: str) -> None:
    """Adds a task to the task list."""
    task = {
        "title": title,
        "tag": tag,
        "isFinished": False,
    }
    TASKS.append(task)
    print(f"[!] Task {title} added successfully!")


def view_all() -> None:
    """Prints all tasks from the global TASKS list in a formatted view."""
