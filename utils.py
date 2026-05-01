def process_data(name: str) -> str:
    """
    Process user input and return formatted string
    """
    if not name.strip():
        raise ValueError("Invalid name")

    return f"Hello, {name.capitalize()}! Welcome to DevOps project 🚀"