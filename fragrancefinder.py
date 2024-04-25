fragrances_masculine = ["Sauvage, Acqua Di Gio, Terre de Hermes, Oud Wood, Bleu de Chanel"]
fragrances_feminine = ["Chanel No 5, Miss Dior, Opium, Portrait of a Lady, Black Orchid "]

print(" Welcome to Fragrance Finder!\nLet's find out a fragrance that matches your style and type by answering a couple questions")

user_input = input("Are you looking for a masculine or feminine smell? M or F to answer: ")

if user_input.capitalize() == "M":
    user_input_masculine = input("What season would you like this for? Type Spring, Summer, Winter, Fall, or Year-Round")

