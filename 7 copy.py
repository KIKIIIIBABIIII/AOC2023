
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
    count_of_J = counts.get('J', 0)
    #让J替换使得整个卡片
    if 'J' not in hand:
        if any(count == 5 for count in counts.values()) :#AAAAA
            return "Five of a kind"
        elif any(count == 4 for count in counts.values()): #AAAAK
            return "Four of a kind"
        elif set(counts.values()) == {3, 2}:#AAAKK
            return "Full house"
        elif any(count == 3 for count in counts.values()):#AAAK9
            return "Three of a kind"
        elif list(counts.values()).count(2) == 2:#AAKK7
            return "Two pair"
        elif list(counts.values()).count(2) == 1:#AA789
            return "One pair"
        else:#AK7T6
            return "High card"
    else:
        if count_of_J == 1:
            if any(count == 4 for count in counts.values()):
                return "Five of a kind"
            elif set(counts.values()) == {3, 2}:
                return "Four of a kind"
            elif any(count == 3 for count in counts.values()):
                return "Four of a kind"
            elif list(counts.values()).count(2) == 2:
                return "Full house"
            elif list(counts.values()).count(2) == 1:
                return "Three of a kind"
            else:
                return "One pair"
        elif count_of_J == 2:
            if set(counts.values()) == {3, 2}:#AAAKK
                return "Five of a kind"
            elif any(count == 3 for count in counts.values()):#AAAJJ
                return "Five of a kind"
            elif list(counts.values()).count(2) == 2:#AAJJ7
                return "Four of a kind"
            elif list(counts.values()).count(2) == 1:#86JJ9
                return "Three of a kind"
            else:#AK7T6
                assert 0
        elif count_of_J == 3:
            if set(counts.values()) == {3, 2}:#AAAKK
                return "Five of a kind"
            elif any(count == 3 for count in counts.values()):#JJJK9
                return "Four of a kind"
            elif list(counts.values()).count(2) == 2:#AAKK7
                assert 0
            elif list(counts.values()).count(2) == 1:#AA789
                assert 0
            else:#AK7T6
                assert 0
        else:
            return "Five of a kind"
                
#按照顺序互换牌的位置
def compare_cards_switch(card1, card2):
    order = "AKQT98765432J" 
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




