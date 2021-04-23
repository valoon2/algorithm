def solution(board, moves):
    answer = 0
    stackList = []

    for i in moves :
        for j in range(len(board)):
            if board[j][i-1] !=0 :
                stackList.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stackList) > 1:
                    if stackList[-1] == stackList[-2]:
                        stackList.pop(-1)
                        stackList.pop(-1)
                        answer += 2
                break
                
    return answer
