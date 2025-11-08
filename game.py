import random
import sys

# Valid input shortcuts
VALID_CHOICES = {
    "rock": "rock",
    "r": "rock",
    "paper": "paper",
    "p": "paper",
    "scissors": "scissors",
    "s": "scissors",
}

# Which choice beats which
BEATS = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}

# Emojis for fun visuals
ICONS = {
    "rock": "🪨",
    "paper": "📜",
    "scissors": "✂️"
}


def get_user_choice():
    """
    Prompt user until valid input or quit command.
    Accepts full names or shortcuts (r/p/s).
    Returns normalized choice or exits on quit.
    """
    while True:
        raw = input("Enter your choice (rock/r, paper/p, scissors/s or q to quit): ").strip().lower()
        if raw in ("q", "quit", "exit"):
            print("👋 Exiting the game. Thanks for playing!")
            sys.exit()
        if raw in VALID_CHOICES:
            return VALID_CHOICES[raw]
        print("❌ Invalid input — please type 'rock', 'paper', 'scissors' or 'r', 'p', 's'.")


def get_computer_choice():
    """Return a random choice among 'rock','paper','scissors'."""
    return random.choice(list(BEATS.keys()))


def decide_winner(user, comp):
    """Return 'user', 'comp', or 'tie' depending on outcome."""
    if user == comp:
        return "tie"
    if BEATS[user] == comp:
        return "user"
    return "comp"


def play_round():
    """Play one round and return result + both choices."""
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    result = decide_winner(user_choice, comp_choice)
    return result, user_choice, comp_choice


def main():
    print("🎉 Welcome to Rock — Paper — Scissors!")
    mode = input("Type 'b' for best-of-N rounds, or press Enter to play indefinitely: ").strip().lower()

    rounds_to_play = None
    if mode == "b":
        while True:
            n = input("Best-of how many rounds? (odd number, e.g., 3, 5, 7): ").strip()
            if n.isdigit():
                n = int(n)
                if n % 2 == 1 and n > 0:
                    rounds_to_play = n
                    break
            print("⚠️ Please enter a positive odd number (3, 5, 7, ...).")

    user_score = comp_score = ties = rounds_played = 0
    needed_to_win = (rounds_to_play // 2) + 1 if rounds_to_play else None

    while True:
        result, user_choice, comp_choice = play_round()
        rounds_played += 1

        # Display choices with icons
        print(f"You chose {user_choice} {ICONS[user_choice]}, computer chose {comp_choice} {ICONS[comp_choice]}.")

        # Show round result
        if result == "user":
            user_score += 1
            print("✅ You win this round! 🎉")
        elif result == "comp":
            comp_score += 1
            print("💻 Computer wins this round.")
        else:
            ties += 1
            print("🤝 It's a tie.")

        print(f"📊 Score -> You: {user_score} | Computer: {comp_score} | Ties: {ties}")

        # Best-of mode check
        if rounds_to_play:
            if user_score >= needed_to_win or comp_score >= needed_to_win or rounds_played >= rounds_to_play:
                print("\n🏁 Final result:")
                if user_score > comp_score:
                    print(f"You win the best-of-{rounds_to_play}! 🏆")
                elif comp_score > user_score:
                    print(f"Computer wins the best-of-{rounds_to_play}. 😢")
                else:
                    print(f"It's a tie after {rounds_played} rounds.")
                break
        else:
            again = input("Play another round? (y/n or q to quit): ").strip().lower()
            if again in ("n", "no", "q", "quit", "exit"):
                print("👋 Thanks for playing — final score:")
                print(f"You: {user_score} | Computer: {comp_score} | Ties: {ties}")
                break


if __name__ == "__main__":
    main()
