def sum(a,b,c):
    return a + b + c
def printBoard():
    z='x' if Xstate[0] else ('o' if Ystate[0] else 0)
    z1='x' if Xstate[1] else ('o' if Ystate[1] else 1)
    z2='x' if Xstate[2] else ('o' if Ystate[2] else 2)
    z3='x' if Xstate[3] else ('o' if Ystate[3] else 3)
    z4='x' if Xstate[4] else ('o' if Ystate[4] else 4)
    z5='x' if Xstate[5] else ('o' if Ystate[5] else 5)
    z6='x' if Xstate[6] else ('o' if Ystate[6] else 6)
    z7='x' if Xstate[7] else ('o' if Ystate[7] else 7)
    z8='x' if Xstate[8] else ('o' if Ystate[8] else 8)
    
    print(f"{z} | {z1} | {z2}")
    print(f"-----|-----|-----")
    print(f"{z3} | {z4}| {z5}")
    print(f"-----|------|------")
    print(f"{z6} | {z7} | {z8}")
    print(f"-----|-----|-----")
def checkWIn(Xstate,Ystate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6], [1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(Xstate[win[0]],Xstate[win[1]],Xstate[win[2]])==3):
            print("x won the match")
            return 1
        if (sum(Ystate[win[0]],Ystate[win[1]],Ystate[win[2]])==3):
            print("O win the match")
            return 0
        else:
            return -1
        
if __name__=="__main__":
    Xstate=[0,0,0,0,0,0,0,0,0]
    Ystate=[0,0,0,0,0,0,0,0,0]
    turn=1
    print("welcome to tic tac toe")
    while True:
        printBoard()
        if turn==1:
            print("X's chance")
            value=int(input("please enter a value:"))
            Xstate[value]=1
        else:
            print("o's chance ")
            value=int(input("please enter a value:"))
            Ystate[value]=1
        cwin=checkWIn(Xstate,Ystate)
        if cwin!=-1:
            print("macth over")
            break
        turn=1-turn

