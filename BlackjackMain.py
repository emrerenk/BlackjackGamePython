import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
pc_cards = []
user_total = 0
pc_total = 0
pc_card_number = 0

def results(users_cards, users_total, pc_first_card):
    print(f"Your Cards: {users_cards}, current score: {users_total}")
    print(f"Computer's first card: {pc_first_card}")

def final_results(users_cards, users_total, pcs_cards, pcs_total):
    print(f"Your final hand: {users_cards}, final score: {users_total}")
    print(f"Computer's final hand: {pcs_cards}, final score: {pcs_total}")

def card_add(card_deck, cards_total):
    rand_index = random.randint(0, len(cards) - 1)
    new_card = cards[rand_index]
    card_deck.append(new_card)
    cards_total = sum(card_deck)
    if card_deck[len(card_deck) - 1] == 11 and cards_total > 21:
        card_deck[len(card_deck) - 1] = 1
        cards_total = sum(card_deck)
    return cards_total

def final_calculator(users_total, pcs_total, pcs_cards):
    if users_total == pcs_total:
        print("It's a draw 😬")
    elif pcs_total > 21:
        print("You are win! Opponent went over! 😆")
    elif len(pcs_cards) == 2 and pcs_total == 21:
        print("You are lose! Opponent has blackjack! 🤯")
    elif (21 - users_total) < (21 - pcs_total):
        print("You are win! 😁")
    elif (21 - pcs_total) < (21 - users_total):
        print("You are lose! 😤")

play_game = True
while play_game:
    user_cards = []
    pc_cards = []
    user_total = 0
    pc_total = 0
    pc_card_number = 0
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == "y":
        print("\n" * 50)  # terminali temizlemek için
        print(art.logo)
        for i in range(2):
            rand_index_no = random.randint(0, len(cards) - 1)
            card = cards[rand_index_no]
            user_cards.append(card)
            user_total = sum(user_cards)
            if card == 11 and user_total > 21:
                user_cards[i] = 1
                user_total = sum(user_cards)
        while pc_total < 17:
            rand_index_no = random.randint(0, len(cards) - 1)
            card = cards[rand_index_no]
            pc_cards.append(card)
            pc_total = sum(pc_cards)
            if card == 11 and pc_total > 21:
                pc_cards[pc_card_number] = 1
                pc_total = sum(pc_cards)
            pc_card_number += 1
        results(user_cards, user_total, pc_cards[0])
        if len(user_cards) == 2 and user_total == 21:
            print("Win with a Blackjack 😎")
        else:
            is_continued_game = True
            while is_continued_game:
                is_choose_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if is_choose_card == "y":
                    user_total = card_add(user_cards, user_total)
                    if user_total > 21:
                        if pc_total > 21:
                            pc_cards = [pc_cards[0]]
                            pc_total = pc_cards[0]
                            final_results(user_cards, user_total, pc_cards, pc_total)
                            print("You went over. You lose 😭")
                        else:
                            final_results(user_cards, user_total, pc_cards, pc_total)
                            print("You went over. You lose 😭")
                        is_continued_game = False
                        #buradan sonra en başa sarması lazım
                    else:
                        results(user_cards, user_total, pc_cards[0])
                elif is_choose_card == "n":
                    final_results(user_cards, user_total, pc_cards, pc_total)
                    final_calculator(user_total, pc_total, pc_cards)
                    is_continued_game = False

    elif play_game == "n":
        play_game = False