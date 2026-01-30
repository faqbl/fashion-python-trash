#'rps' in the following codes refers to rock_paper_scissors game
import pygame
import sys
import time
import math
pygame.init()#initialization
WIDTH,HEIGHT=600,700
BOARD_SIZE=3
CELL_SIZE=WIDTH//BOARD_SIZE
L_WIDTH=15
O_WIDTH=15
X_WIDTH=20
O_R=CELL_SIZE//3
SPACE=CELL_SIZE//4
#set constants
BACKGROUND_COLOR=(255,255,255)
L_COLOR=(0,0,0)
O_COLOR=(0,0,0)
X_COLOR=(0,0,0)
TEXT_COLOR=(0,0,0)
#define colors
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TicTacToe')
screen.fill(BACKGROUND_COLOR)
#set up panel
board=[[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
player='X'
computer='O'
game_over=False
winner=None
thinking_time=0
unit="ms"
#initialize variables
ROCK='rock'
SCISSORS='scissors'
PAPER='paper'
RPS=[ROCK,SCISSORS,PAPER]
#set rps constants
rps_phase=True
player_choice=None
computer_choice=None
rps_result=None
#initialize rps variables
BUTTON_WIDTH=150
BUTTON_HEIGHT=60
BUTTON_MARGIN=30
#set rps panel
first_hand=0

def reset():#just set the global variables as default
    global board,game_over,winner,thinking_time,unit,rps_phase,player_choice,computer_choice,rps_result,player,computer,first_hand
    board=[[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    game_over=False
    winner=None
    thinking_time=0
    unit="ms"
    rps_phase=True
    player_choice=None
    computer_choice=None
    rps_result=None
    player='X'
    computer='O'
    first_hand=0
    screen.fill(BACKGROUND_COLOR)

def rps_ing():#display rps panel
    font=pygame.font.SysFont('Arial',40)
    title=font.render("Choice your gesture to",True,TEXT_COLOR)
    screen.blit(title,(WIDTH//2-title.get_width()//2,20))
    title=font.render("play rock-paper-scissors with PC to",True,TEXT_COLOR)
    screen.blit(title,(WIDTH//2-title.get_width()//2,60))
    title=font.render("decide who's the 1st move",True,TEXT_COLOR)
    screen.blit(title,(WIDTH//2-title.get_width()//2,100))
    #display notice
    by=200
    choice=["ROCK","SCISSORS","PAPER"]
    #display alternative buttons for player
    for i,c in enumerate(choice):
        bx=WIDTH//2-(BUTTON_WIDTH*1.5+BUTTON_MARGIN)+i*(BUTTON_WIDTH+BUTTON_MARGIN)
        pygame.draw.rect(screen,(255,255,255),(bx,by,BUTTON_WIDTH,BUTTON_HEIGHT))
        pygame.draw.rect(screen,TEXT_COLOR,(bx,by,BUTTON_WIDTH,BUTTON_HEIGHT),2)
        #display background
        font=pygame.font.SysFont('Arial',30)
        text=font.render(c,True,TEXT_COLOR)
        screen.blit(text,(bx+BUTTON_WIDTH//2-text.get_width()//2,by+BUTTON_HEIGHT//2-text.get_height()//2))
        #display buttons text

def rps_end():#display rps result
    font=pygame.font.SysFont('Arial',30)
    player_text=f"Your choice:{rps_show(player_choice)}"
    computer_text=f"PC's choice:{rps_show(computer_choice)}"
    player_surface=font.render(player_text,True,TEXT_COLOR)
    computer_surface=font.render(computer_text,True,TEXT_COLOR)
    screen.blit(player_surface,(WIDTH//2-player_surface.get_width()//2,300))
    screen.blit(computer_surface,(WIDTH//2-computer_surface.get_width()//2,350))
    # display choices of both sides
    result_text=""
    if rps_result=='player':
        result_text="You're the 1st move."
    elif rps_result=='computer':
        result_text="PC is the 1st move."
    else:
        result_text="Tie.Press left button at anywhere to re-decide."
    result_surface=font.render(result_text,True,TEXT_COLOR)
    screen.blit(result_surface,(WIDTH//2-result_surface.get_width()//2,400))
    #display result,if tied,continue
    if rps_result!='tie':#if one side won,notice starting
        start_text="Press left button to start."
        start_surface=font.render(start_text,True,TEXT_COLOR)
        screen.blit(start_surface,(WIDTH//2-start_surface.get_width()//2,450))

def rps_show(choice):#for text showing
    if choice==ROCK:
        return "ROCK"
    elif choice==SCISSORS:
        return "SCISSORS"
    elif choice==PAPER:
        return "PAPER"
    return ""

def rps_judge():
    if player_choice==computer_choice:
        return 'tie'
    if  (player_choice==ROCK and computer_choice==SCISSORS)or\
        (player_choice==SCISSORS and computer_choice==PAPER)or\
        (player_choice==PAPER and computer_choice==ROCK):
        return 'player'
    else:
        return 'computer'

def computer_rps():#PC's rps choice is decided randomly
    import random
    return random.choice(RPS)

def draw_board():
    for i in range(1,BOARD_SIZE):#draw the horizon
        pygame.draw.line(screen,L_COLOR,(0,i*CELL_SIZE),(WIDTH,i*CELL_SIZE),L_WIDTH)
    for i in range(1,BOARD_SIZE):#draw the vertical
        pygame.draw.line(screen,L_COLOR,(i*CELL_SIZE,0),(i*CELL_SIZE,HEIGHT-100),L_WIDTH)
    pygame.draw.rect(screen,(255,255,255),(0,HEIGHT-100,WIDTH,100))
    #draw the text area
    font=pygame.font.SysFont('Arial',30)
    if game_over:#if one side win,announce
        if winner==player:
            text="Player wins."
        if winner==computer:
            text="PC wins."
        if winner=='tie':
            text="Tie game."
        text_surface=font.render(text,True,TEXT_COLOR)
        screen.blit(text_surface,(WIDTH//2-text_surface.get_width()//2,HEIGHT-80))
    if not game_over:  # if it's PC round,show PC's thinking time
        time_text=f"PC think time:{thinking_time}{unit}"
        time_surface=font.render(time_text,True,TEXT_COLOR)
        screen.blit(time_surface,(WIDTH//2-time_surface.get_width()//2,HEIGHT-80))
    notice_text="Press 'R' to restart the game."
    if game_over:
        notice_text="Press 'R' to restart the game or other buttons to exit."
    notice_surface=font.render(notice_text,True,TEXT_COLOR)
    screen.blit(notice_surface,(WIDTH//2-notice_surface.get_width()//2,HEIGHT-40))

def draw_pieces():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j]=='X':
                pygame.draw.line(screen,X_COLOR,(j*CELL_SIZE+SPACE,i*CELL_SIZE+SPACE),((j+1)*CELL_SIZE-SPACE,(i+1)*CELL_SIZE-SPACE),X_WIDTH)
                pygame.draw.line(screen,X_COLOR,((j+1)*CELL_SIZE-SPACE,i*CELL_SIZE+SPACE),(j*CELL_SIZE+SPACE,(i+1)*CELL_SIZE-SPACE),X_WIDTH)
            elif board[i][j]=='O':
                pygame.draw.circle(screen,O_COLOR,(j*CELL_SIZE+CELL_SIZE//2,i*CELL_SIZE+CELL_SIZE//2),O_R,O_WIDTH)

def check_winner():
    for i in range(BOARD_SIZE):#check rows
        if board[i][0]==board[i][1]==board[i][2] and board[i][0] is not None:
            return board[i][0]
    for i in range(BOARD_SIZE):#check columns
        if board[0][i]==board[1][i]==board[2][i] and board[0][i] is not None:
            return board[0][i]
    if board[0][0]==board[1][1]==board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] and board[0][2] is not None:
        return board[0][2]
    #check diagonal
    if all(board[i][j] is not None for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)):#check if finish with tie
        return 'tie'
    return None

def evaluate(board,depth,computer_round):#using Minimax algorithm
    result=check_winner()
    '''
    if game finish,return evaluation value
    evaluation value:
    win:1
    tie:0
    lose:-1
    '''
    if result==computer:
        return 1
    elif result==player:
        return -1
    elif result=='tie':
        return 0
    if computer_round:
        best=-math.inf#we hope the best as great as possible,so the return value is initialized as negative infinity
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] is None:
                    board[i][j]=computer
                    score=evaluate(board,depth+1,False)#explore more deeply,try to find a better return value
                    board[i][j]=None
                    best=max(score,best)
        return best
    else:
        best=math.inf#similarly,we initialize the return value as positive infinity
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] is None:
                    board[i][j]=player
                    score=evaluate(board,depth+1,True)
                    board[i][j]=None
                    best=min(score,best)
        return best

'''
the above evaluate function uses the Minimax algorithm
here is a more efficient algorithm called alpha-beta pruning below
'''

'''
def evaluate(board,depth,computer_round,alpha=-math.inf,beta=math.inf):
    result = check_winner()
    if result==computer:
        return 1
    elif result==player:
        return -1
    elif result=='tie':
        return 0
    if computer_round:
        best=-math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] is None:
                    board[i][j]=computer
                    score=evaluate(board,depth+1,False,alpha,beta)
                    board[i][j]=None
                    best=max(score,best)
                    alpha=max(alpha,best)#considering own side will decide the max lower bound,use this value to prune
                    if beta<=alpha:
                        break
            if beta<=alpha:
                break
        return best
    else:
        best=math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] is None:
                    board[i][j]=player
                    score=evaluate(board,depth+1,True,alpha,beta)
                    board[i][j]=None
                    best=min(score,best)
                    beta=min(beta,best)#considering enemy side will decide the min upper bound,use this value to prune
                    if beta<=alpha:
                        break
            if beta<=alpha:
                break
        return best
'''

def computer_move():
    global thinking_time
    global unit
    start_time=time.time()#for thinking time calculation
    best_score=-math.inf#PC hopes to maximize profit,so do as the computer round of Minimax algorithm
    best_move=None#initialize as doing nothing
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] is None:
                board[i][j]=computer
                score=evaluate(board,0,False)
                board[i][j]=None
                if score>best_score:
                    best_score=score
                    best_move=(i,j)
    if best_move:
        board[best_move[0]][best_move[1]]=computer
    end_time=time.time()#calculate PC's thinking time
    thinking_time=int((end_time-start_time)*1000)
    unit="ms"#default unit as millisecond
    if thinking_time==0:#if display 0 under millisecond,change the unit as nanosecond
        thinking_time=int((end_time-start_time)*pow(10,9))
        unit="ns"

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if rps_phase:
            if event.type==pygame.MOUSEBUTTONDOWN:#get player's choice for mouse click
                mouseX,mouseY=event.pos
                if player_choice is None:#get the specific click
                    by=200
                    for i,c in enumerate(RPS):
                        bx=WIDTH//2-(BUTTON_WIDTH*1.5+BUTTON_MARGIN)+i*(BUTTON_WIDTH+BUTTON_MARGIN)
                        if bx<=mouseX<=bx+BUTTON_WIDTH and by<=mouseY<=by+BUTTON_HEIGHT:
                            player_choice=c
                            computer_choice=computer_rps()
                            rps_result=rps_judge()
                            break
                else:
                    if rps_result!='tie':#if one side won the rps,decide the first hand based on the result
                        if rps_result=='computer':
                            first_hand=1
                        rps_phase=False
                        screen.fill(BACKGROUND_COLOR)
                    else:#if tied,continue
                        player_choice=None
                        computer_choice=None
                        rps_result=None
        else:
            if first_hand==1:
                computer='X'
                player='O'
                #exchange the first-hand
                computer_move()
                first_hand=0#in case following-up wrong judgement(in case PC moves without waiting player's moving)
            if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX,mouseY=event.pos
                if mouseY<HEIGHT-100:#only deal with the legal move(blank)
                    clicked_x=mouseY//CELL_SIZE
                    clicked_y=mouseX//CELL_SIZE
                    if board[clicked_x][clicked_y] is None:#player's move
                        board[clicked_x][clicked_y]=player
                        winner=check_winner()#check if winner is generated
                        if winner:
                            game_over=True
                        if not game_over:#if game isn't finished yet,continue(PC round)
                            computer_move()
                            winner=check_winner()#check again
                            if winner:
                                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:#Press 'R' to reset the game
                    reset()
                if game_over and event.key!=pygame.K_r:#Press 'R' to reset the game
                    pygame.quit()
                    sys.exit()
    screen.fill(BACKGROUND_COLOR)
    if rps_phase:
        rps_ing()
        if player_choice is not None:
            rps_end()
    else:
        draw_board()
        draw_pieces()
    pygame.display.update()
    #update condition and re-display after each round
