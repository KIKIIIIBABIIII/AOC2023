
def card(line):
    card = ""
    value = ""
    parts = line.split()

    if len(parts) == 2:
        card, value = parts
    my_tuple = (card, value)
    return my_tuple

def classify_hand(hand):
    counts = {label: hand.count(label) for label in set(hand)}

    if any(count == 5 for count in counts.values()):
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
        elif order.index(c2) < order.index(c1):
            return False
    return False

def sort(cards):
    for i in range(len(cards)):
        for j in range(len(cards) - i - 1):
            if compare_cards_switch(cards[j][0], cards[j + 1][0]):
                cards[j], cards[j + 1] = cards[j + 1], cards[j]
            elif cards[j][0] == cards[j + 1][0] and int(cards[j][1]) > int(cards[j + 1][1]):
                cards[j], cards[j + 1] = cards[j + 1], cards[j]
    return cards


# 主循环
with open('7.txt', 'r') as file:
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for line in file:
        cardnumber = card(line)[0]
        cardvalue = card(line)[1]
        classification = classify_hand(cardnumber)

        if classification == "Five of a kind":
            five_of_a_kind.append(card(line)) 
        elif classification == "Four of a kind":
            four_of_a_kind.append(card(line))
        elif classification== "Full house":
            full_house.append(card(line))
        elif classification == "Three of a kind":
            three_of_a_kind.append(card(line))
        elif classification == "Two pair":
            two_pair.append(card(line))
        elif classification == "One pair":
            one_pair.append(card(line))
        elif classification == "High card":
            high_card.append(card(line))

# 合并list并排序
new_five_of_a_kind = sort(five_of_a_kind)
print(new_five_of_a_kind)
new_four_of_a_kind = sort(four_of_a_kind)
new_full_house = sort(full_house)
new_three_of_a_kind = sort(three_of_a_kind)
new_two_pair = sort(two_pair)
#print(new_two_pair)
new_one_pair = sort(one_pair)
#print(new_one_pair)
new_high_card = sort(high_card)
print(new_high_card)
new_final_list = new_high_card + new_one_pair+new_two_pair  + new_three_of_a_kind + new_full_house + new_four_of_a_kind + new_five_of_a_kind

rank_list = [int(item[1]) for item in new_final_list]

print(rank_list)

# 计算元组的权重和
result = 0
for i  in range(len(rank_list)):
    each_result = (i + 1)*rank_list[i]
    result += each_result
print(result)




