fragrances_masculine = ["Sauvage, Acqua Di Gio, Terre de Hermes, Oud Wood, Bleu de Chanel"]
fragrances_feminine = ["Chanel No 5, Miss Dior, Opium, Portrait of a Lady, Black Orchid "]

print(" Welcome to Fragrance Finder!\nLet's find out a fragrance that matches your style and type by answering a couple questions")

user_input = input("Are you looking for a masculine or feminine smell? M or F to answer: ")
user_input_2 = input("Are you under 35 or over? U or O to answer: ")
user_input_3 = input ("What are you wearing this for? Business, Party, Personal")

if user_input.capitalize == "M":
    if user_input_2.capitalize == "U":
        if user_input_3 == "Business":
            print(fragrances_masculine[2],"would be a good choice")
        elif user_input_3 == "Party":
            print(fragrances_masculine[3],"would be perfect")
        elif user_input_3 == "Personal":
            print(fragrances_masculine[4],"would be a good choice")
    
    

