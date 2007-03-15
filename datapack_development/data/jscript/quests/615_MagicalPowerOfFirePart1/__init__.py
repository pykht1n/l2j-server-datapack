#Made by Emperorc
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

#NPC
Naran = 31378
Udan = 31379
Asefa_Box = 31559

#MOBS
Varka_Mobs = [ 21350, 21351, 21353, 21354, 21355, 21357, 21358, 21360, 21361, \
21362, 21369, 21370, 21364, 21365, 21366, 21368, 21371, 21372, 21373, 21374, 21375 ]
Ketra_Orcs = [ 21324, 21325, 21327, 21328, 21329, 21331, 21332, 21334, 21335, \
21336, 21338, 21339, 21340, 21342, 21343, 21344, 21345, 21346, 21347, 21348, 21349 ]

#ITEMS
Key = 1661
Totem = 7242
Wisdom_Stone = 7081

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self, event, st) :
   cond = st.getInt("cond")
   id = st.getInt("id")
   aggro = st.getInt("aggro")
   Thief_Key = st.getQuestItemsCount(Key)
   htmltext = event
   if event == "31378-04.htm" :
       if st.getPlayer().getLevel() >= 74 and st.getPlayer().getAllianceWithVarkaKetra() <= -2 :
            st.set("cond","1")
            st.set("id","2")
            st.set("aggro","0")
            st.setState(STARTED)
            st.playSound("ItemSound.quest_accept")
            htmltext = "31378-04.htm"
       else :
            htmltext = "31378-02.htm"
            st.exitQuest(1)
   elif event == "31559-03.htm" :
       if Thief_Key:
           st.takeItems(Key,1)
           if aggro == 1 :
               htmltext = "31559-04.htm"
           else :
               htmletext = "31559-03.htm"
               st.giveItems(Totem,1)
               st.set("id","5")
               st.set("cond","3")
               st.playSound("ItemSound.quest_middle")
       else :
           htmltext = "31559-02.htm"
   return htmltext

 def onTalk (self, npc, st):
    npcId = npc.getNpcId()
    htmltext = "<html><head><body>I have nothing to say you</body></html>"
    cond = st.getInt("cond")
    id = st.getInt("id")
    aggro = st.getInt("aggro")
    Red_Totem = st.getQuestItemsCount(Totem)
    Stone = st.getQuestItemsCount(Wisdom_Stone)
    if npcId == Naran :
        if Stone :
            htmltext = "<html><head><body>You already have the stone!</body></html>"
        else :
            if st.getState()== CREATED :
                htmltext = "31378-01.htm"
            elif id == 2 :
                htmltext = "31378-05.htm"
    elif npcId == Udan :
        if st.getPlayer().getAllianceWithVarkaKetra() <= -2 :
            if id == 2 :
                htmltext = "31379-01.htm"
                st.set("cond","2")
                st.set("id","3")
            elif id == 3 :
                htmltext = "31379-02.htm"
            elif id == 4 or aggro == 1 :
                htmltext = "31379-03.htm"
                st.set("id","3")
                st.set("aggro","0")
            elif id == 5 and Red_Totem :
                htmltext = "31379-04.htm"
                st.giveItems(Wisdom_Stone,1)
                st.takeItems(Totem,1)
                st.unset("id")
                st.unset("aggro")
                st.playSound("ItemSound.quest_middle")
                st.exitQuest(1)
    elif npcId == Asefa_Box :
        if st.getPlayer().getAllianceWithVarkaKetra() <= -2 :
            if id == 3 :
                htmltext = "31559-01.htm"
    return htmltext

 def onAttack (self, npc, st):  #TODO: Instead of onAttack, this should best be\
    npcId = npc.getNpcId()      #onAgro/onSee. Change this when supported.
    cond = st.getInt("cond")
    id = st.getInt("id")
    Red_Totem = st.getQuestItemsCount(Totem)
    if npcId in Ketra_Orcs :
        if id > 2 :
            st.set("aggro","1")
            st.set("cond","1")
            st.set("id","4")
            if Red_Totem :
                st.takeItems(Totem,-1)
    return

 def onKill (self, npc, st):
    npcId = npc.getNpcId()
    cond = st.getInt("cond")
    id = st.getInt("id")
    Red_Totem = st.getQuestItemsCount(Totem)
    if npcId in Varka_Mobs :
        st.unset("id")
        st.unset("aggro")
        st.exitQuest(1)
        if Red_Totem:
            st.takeItems(Totem,-1)
    return
        

QUEST       = Quest(615,"615_MagicalPowerOfFirePart1","Magical Power of Fire - Part 1")
CREATED     = State('Start', QUEST)
STARTED     = State('Started', QUEST)

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(Naran)

CREATED.addTalkId(Naran)
STARTED.addTalkId(Naran)
STARTED.addTalkId(Udan)
STARTED.addTalkId(Asefa_Box)

STARTED.addQuestDrop(Asefa_Box,Totem,1)
for mobId in Varka_Mobs:
    STARTED.addKillId(mobId)
for mobId in Ketra_Orcs:
    STARTED.addAttackId(mobId)

print "importing quests: 615: Magical Power of Fire - Part 1"