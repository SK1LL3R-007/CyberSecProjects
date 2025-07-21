import re
import sys

def display_banner():
    print("=" * 60)
    print("Password Strength Evaluation Tool  |  Developed by SK1LL3R")
    print("=" * 60)

def evaluate_password(password):
    issues = []
    score = 0

    if len(password) >= 12:
        score += 1
    else:
        issues.append("Password should be at least 12 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        issues.append("Include at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        issues.append("Include at least one lowercase letter (a-z).")

    if re.search(r"\d", password):
        score += 1
    else:
        issues.append("Include at least one numeric digit (0-9).")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        score += 1
    else:
        issues.append("Include at least one special character (!@#$%^&* etc.).")

    return score, issues

def classify_score(score):
    if score == 5:
        return "STRONG"
    elif 3 <= score < 5:
        return "MODERATE"
    else:
        return "WEAK"

def main():
    display_banner()
    try:
        password = input("Enter the password to evaluate: ").strip()
        if not password:
            print("No input detected. Exiting.")
            sys.exit(1)

        score, issues = evaluate_password(password)
        strength = classify_score(score)

        print(f"\n[RESULT] Password Strength: {strength}")

        if issues:
            print("\n[RECOMMENDATIONS]")
            for issue in issues:
                print(f" - {issue}")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
