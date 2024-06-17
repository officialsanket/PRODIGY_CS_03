import re

def check_password_strength(password):
    # Criteria for the password strength
    criteria = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'numbers': bool(re.search(r'[0-9]', password)),
        'special_characters': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }

    # Calculate the strength score
    score = sum(criteria.values())
    strength = 'Very Weak'

    if score == 5:
        strength = 'Very Strong'
    elif score == 4:
        strength = 'Strong'
    elif score == 3:
        strength = 'Moderate'
    elif score == 2:
        strength = 'Weak'

    # Feedback message
    feedback = []
    if not criteria['length']:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria['uppercase']:
        feedback.append("Password should include at least one uppercase letter.")
    if not criteria['lowercase']:
        feedback.append("Password should include at least one lowercase letter.")
    if not criteria['numbers']:
        feedback.append("Password should include at least one number.")
    if not criteria['special_characters']:
        feedback.append("Password should include at least one special character.")

    return strength, feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for message in feedback:
        print(f" - {message}")
