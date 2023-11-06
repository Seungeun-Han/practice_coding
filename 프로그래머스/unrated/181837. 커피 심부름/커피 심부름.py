def solution(order):
    answer = 0
    menu = {'americano': 4500, 'cafelatte': 5000, 'anything': 4500}
    menu_list = [i.replace('ice', '').replace('hot', '') for i in order]

    for m in menu.keys():
        answer += menu_list.count(m)*menu[m]

    return answer