result = 1


def Backtracking(x, y, board, alphabets, depth):
    # 상하좌우
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    isNoWaytoOut = True
    for i in range(4):
        ty = dy[i] + y
        tx = dx[i] + x

        if tx < 0 or ty < 0 or tx >= C or ty >= R:  # 보드 밖으로 못나가게
            continue

        alphabet = ord(board[ty][tx])-65
        # 방문하지 않았고, 등록된 알파벳이 없는 칸이면
        if not alphabets[alphabet]:
            isNoWaytoOut = False
            alphabets[alphabet] = True
            Backtracking(tx, ty, board, alphabets, depth+1)

            alphabets[alphabet] = False

    if isNoWaytoOut:  # 막다른 길이면
        global result
        if result < depth:
            result = depth


R, C = map(int, input().split())

board = [[None]*C for _ in range(R)]

for i in range(R):
    board[i] = list(input())

alphabets = [None]*100
for i in range(26):  # A~Z 리스트 생성
    alphabets[i] = False


# 1행1열 방문처리
alphabets[ord(board[0][0])-65] = True

Backtracking(0, 0, board, alphabets, 1)

print(result)
