import art
print(art.logo)

auction = True
auction_data = {}

while auction:
    Name = input("Enter your name: ")
    Bid = int(input("Enter your bid value: $"))
    question = input("if new bid needs to be add 'Yes' or type 'No ").lower()

    auction_data[Name] = Bid
    if question == "yes":
        print("\n" *20)

    else:
        auction = False
        max_value = max(auction_data.values())
        for key in auction_data:
            auction_data[key] = max_value

        print("\n" *20)
        print(f"The Bidding winner is: {key} with {max_value}$.")
        print("Thank you for your participation.")
