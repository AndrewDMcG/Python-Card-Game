#list of random numbers, stackexchange deck example make it your own
import random
DeckDict = {1 = "Aid Merchant",
            2 = "Aid Soldier",
            3 = "Aid Thief",
            4 = "Aid Diplomat",
            5 = "Favorable Trade",
            6 = "Raid",
            7 = "Swindle",
            8 = "Seize",
            9 = "Buyout",
            10 = "Spoils of War",
            11 = "Heist",
            12 = "Intervention",
            13 = "Guerilla Tactic",
            14 = "Audit",
            15 = "Reonnaissance",
            16 = "Burglary",
            17 = "Aid Auditor",
            18 = "Aid Mercenary",
            19 = "Aid Thief",
            20 = "Aid Informant",}
random.shuffle(Deck)

#do integer stuff to card class cards
#Turn deck into dictionary only 20, no worries
#por ejemplo:
# suits = {1: "Clubs",
#          etc.
#if statement, each condition is a key
#execution would be assign card class attributes or whatever
#if statements in functiion
#def makeCard(key):
#if key ==1
#    newcard = card(definecard)
 #    etc

if key == 1
    newcard = Card(self, gold=2, diplomacy=0, stealth=0, might=0, victory_point=1, effect="None", completed="In Progress")
if key == 2
    newcard = Card(self, gold=0, diplomacy=0, stealth=0, might=2, victory_point=1, effect="None", completed="In Progress")
if key == 3
    newcard = Card(self, gold=0, diplomacy=0, stealth=2, might=0, victory_point=1, effect="None", completed="In Progress")
if key == 4
    newcard = Card(self, gold=0, diplomacy=2, stealth=0, might=0, victory_point=1, effect="None", completed="In Progress")
if key == 5
    newcard = Card(self, gold=4, diplomacy=0, stealth=0, might=0, victory_point=2, effect="None", completed="In Progress")
if key == 6
    newcard = Card(self, gold=0, diplomacy=0, stealth=0, might=4, victory_point=2, effect="None", completed="In Progress")
if key == 7
    newcard = Card(self, gold=0, diplomacy=0, stealth=4, might=0, victory_point=2, effect="None", completed="In Progress")
if key == 8
    newcard = Card(self, gold=0, diplomacy=4, stealth=0, might=0, victory_point=2, effect="None", completed="In Progress")    
if key == 9
    newcard = Card(self, gold=6, diplomacy=0, stealth=0, might=0, victory_point=3, effect="None", completed="In Progress")
if key == 10
    newcard = Card(self, gold=0, diplomacy=0, stealth=0, might=6, victory_point=3, effect="None", completed="In Progress")
if key == 11
    newcard = Card(self, gold=0, diplomacy=0, stealth=6, might=0, victory_point=3, effect="None", completed="In Progress")
if key == 12
    newcard = Card(self, gold=0, diplomacy=6, stealth=0, might=0, victory_point=3, effect="None", completed="In Progress")
if key == 13
    newcard = Card(self, gold=2, diplomacy=0, stealth=0, might=2, victory_point=2, effect="None", completed="In Progress")
if key == 14
    newcard = Card(self, gold=2, diplomacy=2, stealth=0, might=0, victory_point=2, effect="None", completed="In Progress")
if key == 15
    newcard = Card(self, gold=0, diplomacy=2, stealth=2, might=0, victory_point=2, effect="None", completed="In Progress")
if key == 16
    newcard = Card(self, gold=0, diplomacy=0, stealth=2, might=2, victory_point=2, effect="None", completed="In Progress")
if key == 17
    newcard = Card(self, gold=1, diplomacy=1, stealth=0, might=0, victory_point=2, effect="None", completed="In Progress")
if key == 18
    newcard = Card(self, gold=1, diplomacy=0, stealth=0, might=1, victory_point=2, effect="None", completed="In Progress")
if key == 19
    newcard = Card(self, gold=0, diplomacy=0, stealth=1, might=1, victory_point=2, effect="None", completed="In Progress")
if key == 20
    newcard = Card(self, gold=0, diplomacy=1, stealth=1, might=0, victory_point=2, effect="None", completed="In Progress")    



if Card.completed = "Complete":
    VP = VP + Card.victory_point
    return VP

if Card.completed = "Complete":
    AP = AP - 1
    return AP

if AP = 0:
    end turn code here
    
#Game Setup
random player starts

for i=1:15
    if i==1,2,3
        give to player 1
        p1card(i)=Deck(i)
    elif i==4,5,6
        give to player 2
        p2card(i)=Deck(i)
    elif i==7,8,9
        give to player 3
        p3card(i)=Deck(i) 
    elif i==10,11,12
        give to player 4
        p4card(i)=Deck(i)

#Places/Things
#Players - Number
##Deck - Tuple
Hand(s) - List
Table - List
Completed Pile(s) - List
Resource Pile(s) - List
##Bank - functions
Turns - 

#Player Actions
take_resource(might, gold, diplomacy, stealth);
    player n gets 1 might/gold/diplomacy/stealth
list.append(x)

alsoresource = raw_input("Whadda ya takin'?")
res_list = []

def res_take(res_list):
    res_list.append(alsoresource)
    return res_list

def res_use(res_list):
    res_list.remove(card name stuff here)
    return res_list


invest_resource(might, gold, diplomacy, stealth);
    player n puts 1 might/gold/diplomacy/stealth into the ""bank""
#Might replace with non-user_imput type thing; should go into turn; SANITIZE INPUTS
resource = raw_input("Whadda ya buyin'?")
bank_list = [resource]

def bank_interest(bank_list):
    bank_list.append(bank_list[0])
    return bank_list

print bank_interest(bank_list)
print bank_interest(bank_list)
print bank_interest(bank_list)
print bank_interest(bank_list)
print bank_interest(bank_list)

#Get turnt; same
Cashmoney = raw_input("Cash in?")
if Cashmoney == "yes":
    del bank_list[:]
else:
    bank_list = bank_list
print bank_list






when quest= completed;
    player n gets x VP

when player quest= completed;
    player n draws a quest

when table quest= completed;
    table draws a quest

when player n AP = 0;
    player n turn ends and player m turn begins
    
#Game Rules
Draw a card any time one is played

when player n VP = 15;
    player n wins
    game ends

