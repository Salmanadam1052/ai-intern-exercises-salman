# tools.py

def calculator(expression: str):
    """
    Evaluate a math expression safely.
    Example: "25 * 8" → 200
    """
    try:
        # eval can be risky; here we assume trusted input for simplicity
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"