# implementation of card game - Memory

import simplegui
import random
WIDTH = 800
HEIGHT = 100
CARD_WIDTH = WIDTH/16
CARD_XPOS = 0
# CARD_HEIGHT
cardlist = [] 
colorlist = []
faceuplist = []
matchedlist = []



# helper function to initialize globals
# function to construct list
def list_construct():
    global colorlist,cardlist,matchedlist,faceuplist
    # create list of cards, 
    cardlist,listb = range(0,8),range(0,8)
    cardlist += listb
    # fill colorlist to green in begining
    for card in cardlist:
        colorlist.append("Green")
    # fill faced up cards
        faceuplist.append(False)
    # mark all cards no matched
        matchedlist.append(False)

def init():
    global state, pre_pos, actual_pos
    pre_pos,actual_pos = False,False
    # no cards are face up
    state = 0
    list_construct()
    # random shorted
    random.shuffle(cardlist)
    #print cardlist
   
 # returns the clicked card
def card_clicked(pos):
    global previous_card
    actual_card = pos[0] // CARD_WIDTH
    return actual_card

# check if clicked card already is faced up
def is_facedup(card):
    if faceuplist[card]:
        return True
    else:
        return False
# check if the cards match
def match_ok(actual):
    if(cardlist[actual]==cardlist[pre_pos]):
        matchedlist[actual],matchedlist[pre_pos] = True,True
        return True
    else:
        # faceuplist[pre_pos] = False
        return False
    
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,pre_pos,actual_pos
    
    cardpos = card_clicked(pos)
    # check the actual state and if pos is correct
    if (is_facedup(cardpos)):
            return
    faceuplist[cardpos] = True
    # no previous card
    if state == 0:
        state = 1
        pre_pos = cardpos
    # previous + second card
    elif state == 1:
        if(match_ok(cardpos)):
            state = 0
           
        else:
            state = 2
            actual_pos = cardpos
            
                
    # second card    
    else:
        faceuplist[pre_pos] = False
        pre_pos = actual_pos
        state =  1
        print "mierda"
    
    
   
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for x in range(16):
        canvas.draw_polygon([(CARD_XPOS + CARD_WIDTH*x,0)
                             ,(CARD_WIDTH*x+CARD_WIDTH,0)
                             ,(CARD_WIDTH*x+CARD_WIDTH,HEIGHT)
                             ,(CARD_XPOS + CARD_WIDTH*x,HEIGHT)]
                             ,2,"White",colorlist[x])
        if faceuplist[x]:
            canvas.draw_text(str(cardlist[x]),[CARD_XPOS + 10 + CARD_WIDTH*x,HEIGHT-HEIGHT/4],60,"White")
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)

frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric