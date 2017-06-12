# -*- coding: utf-8 -*-

import random
import time

# puzzle을 아래와 같이 보기좋은 모양으로 출력함
# 1 2 3
# 4 5 6
# 7 8
def show_puzzle(puzzle):
    for row in puzzle:
        for num in row:
            if num < 10:
                print num, "  ",
            else:
                print num, " ",
        print
        print

    return

# 퍼즐을 생성한다.
# 퍼즐은 동적으로 생성되며, 2차원 리스트 형태를 갖는다
# 즉 [[1, 2, 3], [4, 5, 6], [7, 8, '']]
# 빈공간은 ''로 표현한다
def initiate_puzzle(size):
    rows = []
    puzzle = []
    puzzlelst= range(1, size**2)
    puzzlelst.append('  ')

    rng = 0
    for row in range(size):
        for idx in range(rng, rng+size):
            rows.append(puzzlelst[idx])

        puzzle.append(rows)
        rows = []
        rng += size

    return puzzle

# 퍼즐을 랜덤하게 섞음
def shuffle_puzzle(puzzle):
    dxs = [1, 0, -1,  0]
    dys = [0, 1,  0, -1]

    cnt = 0
    while cnt <= 300:
        rnd = random.randint(0, 3)
        dx = dxs[rnd]
        dy = dys[rnd]

        i, j = get_index(puzzle, '  ')
        ni = i + dx
        nj = j + dy

        if 0 <= ni < len(puzzle) and 0 <= nj < len(puzzle[0]):
            puzzle[ni][nj], puzzle[i][j] = puzzle[i][j], puzzle[ni][nj]
        cnt += 1

# 퍼즐이 종료되었는지, 즉 차례대로 정렬되어 완료가 되었는지 검사
def is_done(puzzle, complete):
    completed = True
    for i in range(len(puzzle[0])):
        for j in range(len(puzzle)):
            if not puzzle[i][j] == complete[i][j]:
                completed = False
    return completed

# 퍼즐 보드에서 숫자 n의 인덱스 검색
# 2차원이기 때문에 i, j형태의 인덱스 값을 반환
def get_index(puzzle, n):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == n:
                return i, j

# 퍼즐에서 숫자 n을 이동,
# 이동할 수 없는 경우에는 이동할 수 없다고 표시
# 이동이 가능한 경우는 양옆위아래에 ''가 위치해 있을 경우이다
def move_by_number(puzzle, n):
    i, j = get_index(puzzle, n)
    move_by_index(puzzle, i, j)

    return puzzle

# 숫자를 이동시키기 위해서는 결국 인덱스를 알아야 함
# 즉 move_by_number 내부에서 호출되는 함순
def move_by_index(puzzle, i, j):
    # movable condition
    # 좌우위아래 한방향중 하나가 '' 값이라면 이동 가능
    posi, posj = get_index(puzzle, '  ')
    if (posi-i, posj-j) == (-1, 0):
        puzzle[i][j], puzzle[i-1][j] = puzzle[i-1][j], puzzle[i][j]
    elif (posi-i, posj-j) == (1, 0):
        puzzle[i][j], puzzle[i+1][j] = puzzle[i+1][j], puzzle[i][j]
    elif (posi-i, posj-j) == (0, -1):
        puzzle[i][j], puzzle[i][j-1] = puzzle[i][j-1], puzzle[i][j]
    elif (posi-i, posj-j) == (0, 1):
        puzzle[i][j], puzzle[i][j+1] = puzzle[i][j+1], puzzle[i][j]
    else:
        print "Not movable around this number"


# 퍼즐 생성
size = int(raw_input(' -> please insert puzzle size : '))
puzzle = initiate_puzzle(size)

# 연습문제) -> 아래와 같이 복사하는 이유는? puzzle을 섞고 맞춘 후 비교하기 위해서 섞기 전 바른 순서를 complete에 저장해둔다.
complete = [row[:] for row in puzzle]

# 퍼즐 섞기
shuffle_puzzle(puzzle)

# 섞인 퍼즐 보기
show_puzzle(puzzle)

# 퍼즐 풀기
while not is_done(puzzle, complete):
    try:
        num = int(raw_input(' -> select a number to move : '))

        # 움직일 수 선택하기
        move_by_number(puzzle, num)

        #창 초기화 속도가 빨라서 늦춰주기
        time.sleep(0.3)

        # 화면 clear
        import os
        cls = lambda: os.system('cls') # windows cls, mac clear
        cls()

        # 움직인 이후 퍼즐 상태 보기
        show_puzzle(puzzle)
    except:
        print "Any help? Try another one!"

print '\nyou solved the puzzle!'
