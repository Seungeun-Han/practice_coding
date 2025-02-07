from itertools import combinations

def solution(relation):
    answer = 0
    
    m, n = len(relation), len(relation[0])
    key_list = []
    relation_comb = []
    index_list = [j for j in range(len(relation[0]))]
    for i in range(1, len(relation[0])+1):
        relation_comb.append(list(combinations(index_list, i)))

    relation_comb = sum(relation_comb, [])
    
    # 전치 행렬
    relation_transform = [[relation[i][j] for i in range(len(relation))] for j in range(len(relation[0]))]
    
    # 유일성 확인
    for k in relation_comb:
        if len(k) == 1: # 1개 칼럼만 볼 때
            if len(set(relation_transform[k[0]])) == m:
                key_list.append(k)
        else:  # 2개 이상의 칼럼을 볼 때
            new_key_list = [relation_transform[i] for i in k]
            new_key = ['_'.join([new_key_list[i][j] for i in range(len(k))]) for j in range(m)]
            if len(set(new_key)) == m:
                key_list.append(k)
    
    print(key_list)
    # 최소성 확인
    key_set = [set(i) for i in key_list]

    remove_set = []
    for i in key_set:
        for j in key_set:
            if i != j and j.issubset(i):
                remove_set.append(tuple(i))
    
    return len(set(key_list) - set(remove_set))