from datetime import datetime, timedelta

def get_current_date():
    """
    Returns the current date in the format "MM/DD/YYYY".

    This function uses the datetime module to get the current date and formats it
    as a string in the specified format. The date is based on the system's current
    date and time.

    Returns:
    str: A string representing the current date in the format "MM-DD-YYYY".

    Example:
    >>> get_current_date()
    '09-11-2023'  # Assuming the current date is September 11, 2023
    """
    current_date = datetime.now()
    return current_date.strftime("%m-%d-%Y")

def adjust_date(start_date, days_to_add):
    """
    Adds a specified number of days to a given date and returns the new date.

    This function takes a start date in the format "MM-DD-YYYY" and adds a specified
    number of days to it. The result is returned as a string in the same format.

    Args:
    start_date (str): A string representing the start date in the format "MM-DD-YYYY".
    days_to_add (int): The number of days to add to the start date.

    Returns:
    str: A string representing the new date after adding the specified number of days,
         in the format "MM-DD-YYYY".

    Example:
    >>> adjust_date("09-11-2023", 30)
    '10-11-2023'  # Assuming the start date is September 11, 2023, adding 30 days results in October 11, 2023
    """
    date_obj = datetime.strptime(start_date, "%m-%d-%Y")
    adjusted_date = date_obj + timedelta(days=days_to_add)
    return adjusted_date.strftime("%m-%d-%Y")

def format_currency(amount):
    """
    This function takes a number and formats it as a proper currency string with:

    A dollar sign ($)
    Commas for thousands separators
    Exactly 2 decimal places

    Here are some examples of how it works:
    format_currency(1234.5)      # Returns: "$1,234.50"
    format_currency(1000000)     # Returns: "$1,000,000.00"
    format_currency(12.1)        # Returns: "$12.10"
    format_currency(5)           # Returns: "$5.00"
    """
    return '${:,.2f}'.format(amount)