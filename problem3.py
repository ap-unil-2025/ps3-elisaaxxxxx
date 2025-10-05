"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        # TODO: Get input from user
        # TODO: Check if user typed 'done'
        # TODO: Try to convert to float and add to list
        # TODO: Handle invalid input gracefully
        pass

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.
    """
    values = []   

    while True:
        guest_input = input("Enter a value (type 'done' to finish): ")

        if guest_input.lower() == "done":
            break   

        try:
            number = float(guest_input)   
            values.append(number)         
        except ValueError:
            print("Enter a valid number")

    return values



    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}

    # TODO: Calculate count
    # TODO: Calculate sum
    # TODO: Calculate average
    # TODO: Find minimum
    # TODO: Find maximum
    # TODO: Count even numbers (hint: use modulo operator)
    # TODO: Count odd numbers

    return analysis

def analyze_numbers(numbers):
    """Take a list of numbers and return summary statistics in a dictionary."""
    if not numbers:
        return None

    n = len(numbers)
    total = sum(numbers)
    avg = total / n
    mn = min(numbers)
    mx = max(numbers)
    even_count = sum(1 for x in numbers if x.is_integer() and int(x) % 2 == 0)
    odd_count  = sum(1 for x in numbers if x.is_integer() and int(x) % 2 != 0)

    return {
        "count": n,
        "sum": total,
        "average": avg,
        "min": mn,
        "max": mx,
        "even_count": even_count,
        "odd_count": odd_count,
    }


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.
    pass

nums = get_numbers_from_user()        
stats = analyze_numbers(nums)         

print("\nNumbers entered:", nums)     
print("\nAnalysis Results:")
for key, value in stats.items():
    print(f"- {key}: {value}")
    

def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()