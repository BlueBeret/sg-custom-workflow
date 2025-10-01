#!/usr/bin/env python3
"""
Main module for sg-custom-workflow
A simple demonstration of basic Python functionality.
"""


def greet(name="World"):
    """Print a greeting message."""
    print(f"Hello, {name}!")


def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)


def demonstrate_basic_operations():
    """Demonstrate basic Python operations."""
    print("\n=== Basic Python Operations Demo ===\n")
    
    # Basic greeting
    greet()
    greet("ShotGrid User")
    
    # Basic arithmetic
    numbers = [1, 2, 3, 4, 5]
    total = calculate_sum(numbers)
    print(f"\nSum of {numbers} = {total}")
    
    # Working with dictionaries
    workflow_info = {
        "name": "sg-custom-workflow",
        "type": "POC",
        "language": "Python"
    }
    print(f"\nWorkflow Info:")
    for key, value in workflow_info.items():
        print(f"  {key}: {value}")
    
    # Basic string operations
    message = "ShotGrid Custom Workflow"
    print(f"\nMessage: {message}")
    print(f"Length: {len(message)}")
    print(f"Uppercase: {message.upper()}")
    
    print("\n=== Demo Complete ===\n")


def main():
    """Main entry point of the application."""
    demonstrate_basic_operations()


if __name__ == "__main__":
    main()
