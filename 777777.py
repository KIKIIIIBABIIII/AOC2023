def card(line):
    card = ""
    value = ""
    parts = line.split()

    if len(parts) == 2:
        card,value= parts
    dict = {"card" : card,"value":value}
    return dict

a = card()

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
    