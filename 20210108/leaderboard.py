"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""
# !/bin/python3


def climbingLeaderboard_naive(ranked, player):
    res = list()
    for p in player:
        curr_rank = 1
        prev_ranked = None
        for r_item in ranked:
            if p >= r_item:
                res.append(curr_rank)
                break
            elif prev_ranked != r_item:
                curr_rank += 1
                prev_ranked = r_item
        if p < ranked[-1]:
            res.append(curr_rank)
        ranked.append(p)
        ranked.sort(reverse=True)
    return res


def climbingLeaderboard(ranked, player):
    res = list()
    leaderboard = sorted(set(ranked), reverse=True)
    l = len(leaderboard)

    for a in player:
        while (l > 0) and (a >= leaderboard[l-1]):
            l -= 1
        res.append(l + 1)
    return res


def climbingLeaderboard__(ranked, player):
    res = list()
    set_ranked = list(set(ranked))
    set_ranked.sort(reverse=True)
    rank_dict = dict(zip(set_ranked, range(1, len(set_ranked) + 1)))
    for p in player:
        nums = list(rank_dict.keys())
        nums.sort()
        for k in range(len(nums)):
            if p > nums[k]:
                more_k = [i for i in nums if i > nums[k]]
                for i in more_k:
                    rank_dict[i] += 1
                rank_dict[p] = rank_dict[k]
    return res


if __name__ == '__main__':
    # testcase
    # f_int = open("test/in.txt")
    # f_out = open("test/out.txt")
    # inp = f_int.readlines()
    # ranked_count = int(inp[0].strip())
    # ranked = list(map(int, inp[1].rstrip().split()))
    # player_count = int(inp[2].strip())
    # player = list(map(int, inp[3].rstrip().split()))
    # result = climbingLeaderboard(ranked, player)
    # # print(' '.join(map(str, result)))
    # correct = f_out.read().split('\n')
    # # print(' '.join(correct))
    # assert correct == result

    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)
    print('\n'.join(map(str, result)))

