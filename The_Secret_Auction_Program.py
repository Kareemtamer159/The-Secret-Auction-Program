import art  # Importing the external file that contains the logo 🎨

# Print the logo of the program
print(art.logo)
print("Welcome👋, To The Secret Auction Program🔨.")

# Function to find the highest bidder 🏆
def find_highest_bidder(bidding_record):
    # Use the max function to get the name of the person with the highest bid 🔍
    winner = max(bidding_record, key=bidding_record.get)
    print(f"The winner is '{winner}'🥇 with a bid of '${bidding_record[winner]}'💰.")

# Dictionary to store each bidder's name and bid amount 📘
bids = {}

# Boolean variable to control the loop 💡
keep_bidding = True

# Start of the bidding loop 🎬
while keep_bidding:
    # Ask for the bidder's name 🔤
    name = input("What is your name🔤? : ")

    # Ask for the bid amount 💵
    bid = float(input("What is your bid💵? : $"))

    # Store the bid in the dictionary
    bids[name] = bid

    # Ask if there are more bidders 👥
    more_bidders = input("Are there any other bidders👥? Type 'yes'✅ or 'no'❌ : ").lower()

    # If there are more bidders, simulate clearing the screen to hide previous bids 🔒
    if more_bidders == "yes":
        print("\n" * 100)  # Clear screen
        print(art.logo)
    elif more_bidders == "no":
        keep_bidding = False  # Exit the loop ⛔

# Call the function to display the winner at the end 🏁
find_highest_bidder(bids)
