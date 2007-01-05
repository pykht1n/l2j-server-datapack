# Made by Polo
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

#Npc
MOIRA = 31979
KARUDA = 32017

default="<html><head><body>I have nothing to say to you</body></html>"

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
   htmltext = default
   id = st.getState()
   cond = st.getInt("cond")
   if id <> COMPLETED :
     htmltext = event
     if htmltext == "31979-03.htm" and cond == 0 :
       st.set("cond","1")
       st.setState(STARTED)
       st.playSound("ItemSound.quest_accept")
     elif htmltext == "32017-02.htm" :
       if cond == 1 and st.getInt("ok") :
         st.giveItems(57,1695)
         st.unset("cond")
         st.unset("ok")
         st.setState(COMPLETED)
         st.playSound("ItemSound.quest_finish")
       else :
         htmltext=default
   return htmltext

 def onTalk (Self,npc,st):
   npcId = npc.getNpcId()
   htmltext = default
   id = st.getState()
   cond = st.getInt("cond")
   if id == COMPLETED :
      htmltext="<html><head><body>This quest have already been completed</body></html>"
   elif npcId == MOIRA :
      if cond == 0 :
         if st.getPlayer().getLevel()>=20 :
            htmltext = "31979-02.htm"
         else :
            htmltext = "31979-01.htm"
            st.exitQuest(1)
      else:
         htmltext = "31979-03.htm"
   elif npcId == KARUDA and cond==1 :
      htmltext = "32017-01.htm"
      st.set("ok","1")
   return htmltext

QUEST       = Quest(122,"122_OminousNews","Ominous News")
CREATED     = State('Start', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(MOIRA)

CREATED.addTalkId(MOIRA)
STARTED.addTalkId(MOIRA)
COMPLETED.addTalkId(MOIRA)

STARTED.addTalkId(KARUDA)

print "importing quests: 122: Ominous News"