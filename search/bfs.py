x = 0
y = 0
board = [['S','#','.','.','.'],
         ['.','.','.','#','.'],
         ['.','#','.','.','.'],
         ['.','.','#','#','G']]
#boardのサイズ
h = len(board)
w = len(board[0])

#boardのスタート地点を0に初期化します。
board[y][x] = 0

#移動可能な方向をチェックするためのリストを用意します。
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queue = []

#queueを初期化します
for dx, dy in d:
                        
    #枠外判定
    if y+dy >= h or y+dy < 0 or x+dx >= w or x+dx < 0:
        continue
                        
    #Gが見つかれば、終わりです。
    if board[y+dy][x+dx] == 'G':
        board[y+dy][x+dx] = board[y][x]+1
                        
    #数字または＃(壁)でないかをチェックします。
    if board[y+dy][x+dx] != '.':
        continue
                        
    #上記のいずれでもない場合、c+1で埋めます
    board[y+dy][x+dx] = board[y][x] + 1
    queue.append((y+dy, x+dx))

def BFS(board):         
    #探索する場所がなくなるまで(＝queueの要素がなくなるまで)探索します。
    while queue:
        y, x = queue.pop(0)
        #4方向についてチェックします。
        for dx, dy in d:
                        
            #枠外判定
            if y+dy >= h or y+dy < 0 or x+dx >= w or x+dx < 0:
                continue
                        
            #Gが見つかれば、終わりです。
            if board[y+dy][x+dx] == 'G':
                board[y+dy][x+dx] = board[y][x]+1
                return board[y][x] + 1
                        
            #数字または＃(壁)でないかをチェックします。
            if board[y+dy][x+dx] != '.':
                continue
                        
            #上記のいずれでもない場合、今の場所の数字+1で埋めます
            board[y+dy][x+dx] = board[y][x]+1
        
            #queueに新しい場所を追加します
            queue.append((y+dy, x+dx)) 
                   
print(BFS(board))
for b in board:                        
    print(b) 