
def card(line):
    card = ""
    value = ""
    parts = line.split()

    if len(parts) == 2:
        card,value= parts
    dict = {"card" : card,"value":value}
    return dict
def classify_hand(hand):
    counts = {label: hand.count(label) for label in set(hand)}

    if "5" in counts and counts["5"] == 5:
        return "Five of a kind"
    elif any(count == 4 for count in counts.values()):
        return "Four of a kind"
    elif set(counts.values()) == {3, 2}:
        return "Full house"
    elif any(count == 3 for count in counts.values()):
        return "Three of a kind"
    elif list(counts.values()).count(2) == 2:
        return "Two pair"
    elif list(counts.values()).count(2) == 1:
        return "One pair"
    else:
        return "High card"

#按照顺序互换牌的位置
def compare_cards_switch(card1, card2):
    order = "AKQJT98765432" 
    for c1, c2 in zip(card1, card2):
        if order.index(c2) > order.index(c1):
            return True
    return False

def sort(x):
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if compare_cards_switch(x[j], x[j + 1]):
                x[j], x[j + 1] = x[j + 1], x[j]
    return x

def getdictvalue(my_dict):
    result_sum = sum(cardvalue * (index + 1) for index, cardvalue in enumerate(my_dict.values()))
    return result_sum


with open('7.txt', 'r') as file:
    five_of_a_kind = {}
    four_of_a_kind = {}
    full_house = {}
    three_of_a_kind = {}
    two_pair= {}
    one_pair = {}
    high_card = {}
    for line in file:
        cardnumber = card(line)["card"]
        cardvalue = card(line)["value"]
        if classify_hand(cardnumber) == "Five of a kind":
            five_of_a_kind.update(card(line))
        if classify_hand(cardnumber) == "Four of a kind":
            four_of_a_kind.update(card(line))
        if classify_hand(cardnumber) == "Full house":
            full_house.update(card(line))
        if classify_hand(cardnumber) == "Three of a kind":
            three_of_a_kind.update(card(line))
        if classify_hand(cardnumber) == "Two pair":
            two_pair.update(card(line))
        if classify_hand(cardnumber) == "One pair":
            one_pair.update(card(line))
        if classify_hand(cardnumber) == "High card":
            high_card.update(card(line))
    new_five_of_a_kind = sort(five_of_a_kind)
    new_four_of_a_kind  = sort(four_of_a_kind)
    new_full_house = sort(full_house)
    new_three_of_a_kind = sort(three_of_a_kind)
    new_two_pair = sort(two_pair)
    new_one_pair = sort(one_pair)
    new_high_card  = sort(high_card)
    merged_dict = new_high_card.copy()
    merged_dict.update(new_one_pair)
    merged_dict.update(new_two_pair )
    merged_dict.update(new_three_of_a_kind)
    merged_dict.update(new_full_house)
    merged_dict.update(new_four_of_a_kind)
    merged_dict.update(new_five_of_a_kind)
    
    result = getdictvalue(merged_dict)