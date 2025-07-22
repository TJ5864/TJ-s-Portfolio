import pandas as pd 
import re 
df = pd.read_csv("cleaned_player_projections.csv")

drafted_players = []

def top_n_players(position, n=10):
    
    position_pattern = re.compile(r'\b' + position + r'\b', re.IGNORECASE)
    filtered = df[df['Player'].str.contains(position_pattern)]
    drafted_all = set(drafted_by_me + drafted_by_others)
    filtered = filtered[~filtered['Player'].isin(drafted_all)]
    filtered = filtered.sort_values(by='Fantasy Points', ascending=False)
    print(filtered[['Player', 'Fantasy Points', 'Fantasy Points Per Game']].head(n))

drafted_by_me = []
drafted_by_others = []

def draft_player(player_name, drafted_by='me'):
    pattern = re.compile(player_name, re.IGNORECASE)
    matches = df[df['Player'].str.contains(pattern)]

    if matches.empty:
        print(f"No match found for '{player_name}'")
        return

    if len(matches) > 1:
        print(f"Multiple players matched '{player_name}':")
        print(matches[['Player', 'Position', 'Team']])
        return

    matched_name = matches.iloc[0]['Player']

    if matched_name in drafted_by_me or matched_name in drafted_by_others:
        print(f"Player '{matched_name}' already drafted.")
        return

    if drafted_by.lower() == 'me':
        drafted_by_me.append(matched_name)
        print(f"{matched_name} drafted BY YOU.")
    else:
        drafted_by_others.append(matched_name)
        print(f"{matched_name} drafted BY OTHER TEAMS.")
    
    

def get_available_players():
    drafted_all = set(drafted_by_me + drafted_by_others)
    available = df[~df['Player'].isin(drafted_all)]
    return available

def main():
    print("Welcome to the Fantasy Football Draft Assistant!")
 

    while True: 
        print("\n Pick an option 1-7")
        print("1. Top 10 players for a position")
        print("2. Draft a player to your team")
        print("3. Draft a player to another team (make unavailable)")
        print("4. View Available Players ")
        print("5. View Your Team")
        print("6. View Players Drafted by other Teams")
        print("7. Exit")
        choice = input("Pick a Number 1-7: ")

        if choice == '1':
            position = input("Enter the position you want to draft (QB, RB, WR, TE, K, DST): ").upper()
            top_n_players(position)

        elif choice == '2':
            player_name = input("Enter the player name you want to draft: ")
            draft_player(player_name, 'me')

        elif choice == '3':
            player_name = input("Enter the player name you want to draft: ")
            draft_player(player_name, 'other')

        elif choice == '4':
            available_players = get_available_players()
            print(available_players[['Player', 'Position', 'Team', 'Fantasy Points', 'Fantasy Points Per Game']])

        elif choice == '5':
            print("Your Team:")
            print("Drafted by You:")
            print(drafted_by_me)
            print("Drafted by Others:")
            print(drafted_by_others)

        elif choice == '6':
            print("Players Drafted by Others:")
            print(drafted_by_others)

        elif choice == '7':
            print("Exiting the Draft Assistant. Goodbye!")
            break
if __name__ == "__main__":
    main()

