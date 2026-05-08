import sys

def check_password_strength(password):
    """
    DecodeLabs Industrial Kit - Project 1: Password Strength Checker
    Constraint: Validation time must grow linearly, not exponentially.
    Complexity: O(n) (Linear Scan)
    """

    # 1. LENGTH VERIFICATION (The Zero Point)
    # < 8 chars = Immediate fail due to exponential brute force risk.
    if len(password) < 8:
        return "FAIL", "Password is too short! Minimum 8 characters required."

    # 2. PATTERN RECOGNITION (Pythonic Elegance)
    # Using any() for short-circuit evaluation to maintain O(n) complexity.
    has_upper  = any(char.isupper() for char in password)  # [A-Z]
    has_lower  = any(char.islower() for char in password)  # [a-z]
    has_digit  = any(char.isdigit() for char in password)  # [0-9]
    has_symbol = any(not char.isalnum() for char in password) # [SYMBOLS]

    # 3. RISK CLASSIFICATION (The Logic Skeleton)
    # sum() calculates the entropy level based on character variety.
    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if score == 4:
        return "STRONG", "Digital foundation secure: All criteria met."
    elif score == 3:
        return "MODERATE", "Passable, but consider adding more character variety."
    else:
        return "WEAK", "High Risk: Include uppercase, lowercase, digit, and symbol."

def main():
    print("--- DecodeLabs Password Strength Checker ---")
    print("Track: Junior Analyst // Defensive Logic\n")
    
    try:
        # INPUT: RAW BYTE STREAM logic
        user_input = input("Enter password for risk analysis: ")
        
        if not user_input:
            print("Error: Input stream cannot be empty.")
            return

        # PROCESS & OUTPUT
        status, message = check_password_strength(user_input)
        
        print("-" * 50)
        print(f"RISK LEVEL : {status}")
        print(f"REPORT     : {message}")
        print("-" * 50)

        # SECURITY PROTOCOL: The Immutability Trap
        # Manually clear the reference to the password from local memory.
        del user_input
        
    except KeyboardInterrupt:
        print("\n[!] Process interrupted by user. Exiting safely...")
        sys.exit(0)

if __name__ == "__main__":
    main()