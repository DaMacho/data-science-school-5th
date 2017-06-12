# -*- coding: utf-8 -*-

import random

# puzzle을 아래와 같이 보기좋은 모양으로 출력함
# 1 2 3
# 4 5 6
# 7 8
def show_puzzle(puzzle):
    for row in puzzle:
        for item in row:
            print item,
        print

# 퍼즐을 생성한다.
# 퍼즐은 동적으로 생성되며, 2차원 리스트 형태를 갖는다
# 즉 [[1, 2, 3], [4, 5, 6], [7, 8, '']]
# 빈공간은 ''로 표현한다
def initiate_puzzle(size):
    puzzle = []
    for i in range(size):
        j = 1
        a = []
        while j <= size:
            if i*size+j == size*size:
                a.append('')
            else:
                a.append(i*size+j)
            j += 1
        puzzle.append(a)
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

        i, j = get_index(puzzle, '')

        ni = i + dx
        nj = j + dy

        if 0 <= ni < len(puzzle) and 0 <= nj < len(puzzle[0]):
            puzzle[ni][nj], puzzle[i][j] = puzzle[i][j], puzzle[ni][nj]
        cnt += 1

# # 퍼즐이 종료되었는지, 즉 차례대로 정렬되어 완료가 되었는지 검사
def is_done(puzzle, complete):
    return puzzle == complete

# 퍼즐 보드에서 숫자 n의 인덱스 검색
# 2차원이기 때문에 i, j형태의 인덱스 값을 반환
def get_index(puzzle, n):
    for a in range(size):
        if n in puzzle[a]:
            i = a
            j = puzzle[a].index(n)
    return i, j

# 퍼즐에서 숫자 n을 이동,
# 이동할 수 없는 경우에는 이동할 수 없다고 표시
# 이동이 가능한 경우는 양옆위아래에 ''가 위치해 있을 경우이다
def move_by_number(puzzle, n):
    i, j = get_index(puzzle, n)
    move_by_index(puzzle, i, j)
# # 숫자를 이동시키기 위해서는 결국 인덱스를 알아야 함
# # 즉 move_by_number 내부에서 호출되는 함순
def move_by_index(puzzle, i, j):
    # movable condition
    # 좌우위아래 한방향중 하나가 '' 값이라면 이동 가능
    m, n = get_index(puzzle, '')
    if i == m + 1 or i == m - 1:
        puzzle[i][j], puzzle[m][n] = puzzle[m][n], puzzle[i][j]
        return puzzle
    elif j == n + 1 or j == n - 1:
        puzzle[i][j], puzzle[m][n] = puzzle[m][n], puzzle[i][j]

# 퍼즐 생성
size = int(raw_input(' -> please insert puzzle size : '))
puzzle = initiate_puzzle(size)

# 연습문제) -> 아래와 같이 복사하는 이유는?
# 답) 퍼즐을 푼 뒤 최초 생성된 상태와 같은지 확인하기 위해
complete = [row[:] for row in puzzle]

# 퍼즐 섞기
shuffle_puzzle(puzzle)

# 섞인 퍼즐 보기
show_puzzle(puzzle)

# 퍼즐 풀기
while not is_done(puzzle, complete):

    try:
        num_to_move = int(raw_input(' -> select a number to move : '))
        # 움직일 수 선택하기
        move_by_number(puzzle, num_to_move)
        # 화면 clear
        import os
        cls = lambda: os.system('cls') # windows cls
        cls()
        # 움직인 이후 퍼즐 상태 보기
        show_puzzle(puzzle)
    except UnboundLocalError as err:
        print "please select again. between 1 and {}".format(len(puzzle)*len(puzzle)-1)
    except ValueError as other:
        print "something else broke", other

print '\nyou solved the puzzle!'
