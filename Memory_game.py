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
exposed = []
matchedlist = []
counter = 0



# helper function to initialize globals
# function to construct list
def list_construct():
    global colorlist,cardlist,matchedlist,faceuplist,exposed
    colorlist = []
    exposed = []
    matchedlist = []
    # create list of cards, 
    cardlist,listb = range(0,8),range(0,8)
    cardlist += listb
    # fill colorlist to green in begining
    # fill faced up cards
    # mark all cards no matched
    for card in cardlist:
        colorlist.append("Green")
        matchedlist.append(False)
        exposed.append(False)
def init():
    global state, pre_pos, act_pos,counter
    pre_pos,act_pos = False,False
    # no cards are face up
    state = 0
    counter = 0
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
    if exposed[card]:
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
    global state,pre_pos,act_pos,counter
    cardpos = card_clicked(pos)
    # check the actual state and if pos is correct
    if (is_facedup(cardpos)):
            return
    # no previous card
    if state == 0:
        state = 1
        act_pos = cardpos
        exposed[cardpos] = True
    # previous + second card
    elif state == 1:
       pre_pos = act_pos
       act_pos = cardpos
       state = 2
       exposed[cardpos] = True   
       counter += 1
                
    # second card    
    else:
        if not (match_ok(act_pos)):
            exposed[pre_pos] = False
            exposed[act_pos] = False
                   
        act_pos = cardpos
        state =  1
        exposed[cardpos] = True
                       
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for x in range(16):
        canvas.draw_polygon([(CARD_XPOS + CARD_WIDTH*x,0)
                             ,(CARD_WIDTH*x+CARD_WIDTH,0)
                             ,(CARD_WIDTH*x+CARD_WIDTH,HEIGHT)
                             ,(CARD_XPOS + CARD_WIDTH*x,HEIGHT)]
                             ,2,"White",colorlist[x])
        if exposed[x]:
            canvas.draw_text(str(cardlist[x]),[CARD_XPOS + 10 + CARD_WIDTH*x,HEIGHT-HEIGHT/4],60,"White")
    label.set_text("Moves = %d"%(counter))
                   
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