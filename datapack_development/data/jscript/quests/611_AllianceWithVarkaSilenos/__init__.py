#Made by Emperorc
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

#NPC
Naran_Ashanuk = 31378

#MOB
    #mobs for Alliance lvl 1:Ketra Orc footmen, raiders, scouts, shamans and war hounds
Ketra_One = [ 21324, 21325, 21327, 21328, 21329 ]
    #mobs for Alliance lvl 2 : Ketra Orc-warriors, Lieutenants, mediums, Elite Soldiers,\
    #White Captains, Seers, Commanders, Elite Guards
Ketra_Two = [ 21331, 21332, 21334, 21335, 21336, 21338, 21343, 21344 ]
    #mobs for Alliance lvl 3 and up SHOULD BE:Ketra Orc captains, battalion commanders, \
    #grand seers, chief shamans, chief royal guards, prophets, Prophet's Guards, and Prophet's Aides
        #AS LISTED in npc.sql: Ketra Orc-General, Battalion Commander, Grand Seer, \
        #Ketra's - Head Shaman, Head Guard, Prophet, Prophet's Guard, and Prophet's Aide
Ketra_Three = [ 21339, 21340, 21342, 21345, 21346, 21347, 21348, 21349 ]
    #All Varka Silenos mobs
Varka_Silenos = [ 21350, 21351, 21353, 21354, 21355, 21357, 21358, 21360, 21361, \
21362, 21369, 21370, 21364, 21365, 21366, 21368, 21371, 21372, 21373, 21374, 21375 ]

#Quest Items
Varka_Badge_Soldier, Varka_Badge_Officer, Varka_Badge_Captain = [7216, 7217, 7218]
Ketra_Alliance_One, Ketra_Alliance_Two, Ketra_Alliance_Three, \
Ketra_Alliance_Four, Ketra_Alliance_Five = [7211, 7212, 7213, 7214, 7215]
Varka_Alliance_One, Varka_Alliance_Two, Varka_Alliance_Three, \
Varka_Alliance_Four, Varka_Alliance_Five  = [7221, 7222, 7223, 7224, 7225]
Ketra_Badge_Soldier, Ketra_Badge_Officer, Ketra_Badge_Captain  = [7226, 7227,7228]
Valor_Feather, Wisdom_Feather = [ 7229, 7230 ]

def decreaseAlliance(st) :
  if st.getPlayer().isAlliedWithVarka() :
    cond = st.getInt("cond")
    id = st.getInt("id")
    st.takeItems(Ketra_Badge_Soldier,-1)
    st.takeItems(Ketra_Badge_Officer,-1)
    st.takeItems(Ketra_Badge_Captain,-1)
    st.takeItems(Valor_Feather,-1)
    st.takeItems(Wisdom_Feather,-1)
    st.getPlayer().setAllianceWithVarkaKetra(0)
    st.exitQuest(1)
    if cond == 2 :
      if id == 2 :
        st.takeItems(Varka_Alliance_One,-1)
      else :
        st.takeItems(Varka_Alliance_Two,-1)
        st.giveItems(Varka_Alliance_One,1)
    elif cond == 3 :
      if id == 2:
        st.takeItems(Varka_Alliance_Two,-1)
        st.giveItems(Varka_Alliance_One,1)
      else :
         st.takeItems(Varka_Alliance_Three,-1)
         st.giveItems(Ketra_Alliance_Two,1)
    elif cond == 4 :
      if id == 2 :
        st.takeItems(Varka_Alliance_Three,-1)
        st.giveItems(Varka_Alliance_Two,1)
      else :
        st.takeItems(Varka_Alliance_Four,-1)
        st.giveItems(Varka_Alliance_Three,1)
    elif cond == 5 :
      if id == 2 :
        st.takeItems(Varka_Alliance_Four,-1)
        st.giveItems(Varka_Alliance_Three,1)
      else :
        st.takeItems(Varka_Alliance_Five,-1)
        st.giveItems(Varka_Alliance_Four,1)
    elif cond == 6 :
      st.takeItems(Varka_Alliance_Five,-1)
      st.giveItems(Varka_Alliance_Four,1)

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
   cond = st.getInt("cond")
   id = st.getInt("id")
   htmltext = event
   if event == "31378-03a.htm" :
       if st.getPlayer().getLevel() >= 74 :
            st.set("cond","1")
            st.set("id","2")
            st.setState(STARTED)
            st.playSound("ItemSound.quest_accept")
            htmltext = "31378-03a.htm"
       else :
            htmltext = "31378-02b.htm"
            st.getPlayer().setAllianceWithVarkaKetra(0)
            st.exitQuest(1)
   elif event == "31378-10-1.htm" :
       htmltext = "31378-10-1.htm"
       st.set("id","3")
       st.takeItems(Ketra_Badge_Soldier, 100)
       st.giveItems(Varka_Alliance_One, 1)
       st.getPlayer().setAllianceWithVarkaKetra(-1)
       st.playSound("Itemsound.quest_itemget")
   elif event == "31378-10-2.htm" :
       htmltext = "31378-10-2.htm"
       st.set("id","3")
       st.takeItems(Ketra_Badge_Soldier, 200)
       st.takeItems(Ketra_Badge_Officer, 100)
       st.takeItems(Varka_Alliance_One, -1)
       st.giveItems(Varka_Alliance_Two, 1)
       st.getPlayer().setAllianceWithVarkaKetra(-2)
       st.playSound("Itemsound.quest_itemget")
   elif event == "31378-10-3.htm" :
       htmltext = "31378-10-3.htm"
       st.set("id","3")
       st.takeItems(Ketra_Badge_Soldier, 300)
       st.takeItems(Ketra_Badge_Officer, 200)
       st.takeItems(Ketra_Badge_Captain, 100)
       st.takeItems(Varka_Alliance_Two, -1)
       st.giveItems(Varka_Alliance_Three, 1)
       st.getPlayer().setAllianceWithVarkaKetra(-3)
       st.playSound("Itemsound.quest_itemget")
   elif event == "31378-10-4.htm" :
       htmltext = "31378-10-4.htm"
       st.set("id","3")
       st.takeItems(Ketra_Badge_Soldier, 300)
       st.takeItems(Ketra_Badge_Officer, 300)
       st.takeItems(Ketra_Badge_Captain, 200)
       st.takeItems(Varka_Alliance_Three, -1)
       st.takeItems(Valor_Feather,-1)
       st.giveItems(Varka_Alliance_Four, 1)
       st.getPlayer().setAllianceWithVarkaKetra(-4)
       st.playSound("Itemsound.quest_itemget")
   elif event == "31378-11a.htm" :
       htmltext = "31378-11a.htm"
   elif event == "31378-19.htm" :
       htmltext = "31378-19.htm"
   elif event == "31378-11b.htm" :
       htmltext = "31378-11b.htm"
   elif event == "31378-20.htm" :
       htmltext = "31378-20.htm"
       st.takeItems(Ketra_Badge_Soldier, -1)
       st.takeItems(Ketra_Badge_Officer, -1)
       st.takeItems(Ketra_Badge_Captain, -1)
       st.takeItems(Varka_Alliance_One, -1)
       st.takeItems(Varka_Alliance_Two, -1)
       st.takeItems(Varka_Alliance_Three, -1)
       st.takeItems(Varka_Alliance_Four, -1)
       st.takeItems(Varka_Alliance_Five, -1)
       st.takeItems(Valor_Feather,-1)
       st.takeItems(Wisdom_Feather,-1)
       st.getPlayer().setAllianceWithVarkaKetra(0)
       st.exitQuest(1)
   return htmltext

 def onTalk (self,npc,st):
    npcId = npc.getNpcId()
    htmltext = "<html><head><body>I have nothing to say you</body></html>"
    cond = st.getInt("cond")
    id = st.getInt("id")
    KBadgeS = st.getQuestItemsCount(Ketra_Badge_Soldier)
    KBadgeO = st.getQuestItemsCount(Ketra_Badge_Officer)
    KBadgeC = st.getQuestItemsCount(Ketra_Badge_Captain)
    VAlliance1 = st.getQuestItemsCount(Varka_Alliance_One)
    VAlliance2 = st.getQuestItemsCount(Varka_Alliance_Two)
    VAlliance3 = st.getQuestItemsCount(Varka_Alliance_Three)
    VAlliance4 = st.getQuestItemsCount(Varka_Alliance_Four)
    VAlliance5 = st.getQuestItemsCount(Varka_Alliance_Five)
    VAlliance = VAlliance1 + VAlliance2 + VAlliance3 + VAlliance4 + VAlliance5
    KAlliance = st.getQuestItemsCount(Ketra_Alliance_One) + \
     st.getQuestItemsCount(Ketra_Alliance_Two) + st.getQuestItemsCount(Ketra_Alliance_Three) + \
     st.getQuestItemsCount(Ketra_Alliance_Four) + st.getQuestItemsCount(Ketra_Alliance_Five)
    Valor = st.getQuestItemsCount(Valor_Feather)
    Wisdom = st.getQuestItemsCount(Wisdom_Feather)
    if npcId == Naran_Ashanuk :
        st.set("id","1")
        if st.getPlayer().isAlliedWithKetra() or KAlliance :
            htmltext= "31378-02a.htm"
            st.exitQuest(1)
        elif VAlliance == 0 :
            if cond != 1 :
                htmltext = "31378-01.htm"
            else :
                st.set("id","2")
                if KBadgeS < 100 :
                    htmltext= "31378-03b.htm"
                elif KBadgeS >= 100 :
                    htmltext = "31378-09.htm"
        elif VAlliance :
            st.setState(STARTED)
            st.set("id","2")
            if VAlliance1 :
                if cond != 2 :
                    htmltext = "31378-04.htm"
                    st.set("cond","2")
                    st.getPlayer().setAllianceWithVarkaKetra(-1)
                else :
                    if KBadgeS < 200 or KBadgeO < 100 :
                        htmltext = "31378-12.htm"
                    elif KBadgeS >= 200 and KBadgeO >= 100 :
                        htmltext = "31378-13.htm"
            elif VAlliance2 :
                if cond != 3 :
                    htmltext = "31378-05.htm"
                    st.set("cond","3")
                    st.getPlayer().setAllianceWithVarkaKetra(-2)
                else :
                    if KBadgeS < 300 or KBadgeO < 200 or KBadgeC < 100 :
                        htmltext = "31378-15.htm"
                    elif KBadgeS >= 300 and KBadgeO >= 200 and KBadgeC >= 100 :
                        htmltext = "31378-16.htm"
            elif VAlliance3 :
                if cond != 4 :
                    htmltext = "31378-06.htm"
                    st.set("cond","4")
                    st.getPlayer().setAllianceWithVarkaKetra(-3)
                else:
                    if KBadgeS < 300 or KBadgeO < 300 or KBadgeC < 200 or Valor == 0 :
                        htmltext = "31378-21.htm"
                    elif KBadgeS >= 300 and KBadgeO >= 300 and KBadgeC >= 200 and Valor > 0 :
                        htmltext = "31378-22.htm"
            elif VAlliance4 :
                if cond != 5 :
                    htmltext = "31378-07.htm"
                    st.set("cond","5")
                    st.getPlayer().setAllianceWithVarkaKetra(-4)
                else :
                    if KBadgeS < 400 or KBadgeO < 400 or KBadgeC < 200 or Wisdom == 0 :
                        htmltext = "31378-17.htm"
                    elif KBadgeS >= 400 and KBadgeO >= 400 and KBadgeC >= 200 and Wisdom > 0 :
                        htmltext = "31378-10-5.htm"
                        st.takeItems(Ketra_Badge_Soldier, 400)
                        st.takeItems(Ketra_Badge_Officer, 400)
                        st.takeItems(Ketra_Badge_Captain, 200)
                        st.takeItems(Varka_Alliance_Four, -1)
                        st.takeItems(Wisdom_Feather,-1)
                        st.giveItems(Varka_Alliance_Five, 1)
                        st.getPlayer().setAllianceWithVarkaKetra(-5)
                        st.set("id","3")
                        st.playSound("Itemsound.quest_itemget")
            elif VAlliance5 :
                if cond != 6 :
                    htmltext = "31378-18.htm"
                    st.set("cond","6")
                    st.getPlayer().setAllianceWithVarkaKetra(-5)
                else:
                    htmltext = "31378-08.htm"
    return htmltext

 def onKill (self,npc,st):
    npcId = npc.getNpcId()
    cond = st.getInt("cond")
    id = st.getInt("id")
    KBadgeS = st.getQuestItemsCount(Ketra_Badge_Soldier)
    KBadgeO = st.getQuestItemsCount(Ketra_Badge_Officer)
    KBadgeC = st.getQuestItemsCount(Ketra_Badge_Captain)
    VAlliance1 = st.getQuestItemsCount(Varka_Alliance_One)
    VAlliance2 = st.getQuestItemsCount(Varka_Alliance_Two)
    VAlliance3 = st.getQuestItemsCount(Varka_Alliance_Three)
    VAlliance4 = st.getQuestItemsCount(Varka_Alliance_Four)
    VAlliance5 = st.getQuestItemsCount(Varka_Alliance_Five)
    if not st.getPlayer().isAlliedWithKetra() :
        if npcId in Ketra_One : 
            if cond == 1 and id == 2 :
                if KBadgeS == 99 :
                    st.giveItems(Ketra_Badge_Soldier,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Soldier,1)
                    st.playSound("Itemsound.quest_middle")
            elif cond == 2 and VAlliance1 and id == 2 :
                if KBadgeS == 199  :
                    st.giveItems(Ketra_Badge_Soldier,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Soldier,1)
                    st.playSound("Itemsound.quest_middle")
            elif cond == 3 and VAlliance2 and id == 2 :
                if KBadgeS == 299 :
                    st.giveItems(Ketra_Badge_Soldier,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Soldier,1)
                    st.playSound("Itemsound.quest_middle")
            elif cond == 4 and VAlliance3 and id == 2 :
                if KBadgeS == 299 :
                    st.giveItems(Ketra_Badge_Soldier,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Soldier,1)
                    st.playSound("Itemsound.quest_middle")
            elif cond == 5 and VAlliance4 and id == 2 :
                if KBadgeS == 399 :
                    st.giveItems(Ketra_Badge_Soldier,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Soldier,1)
                    st.playSound("Itemsound.quest_middle")
        elif npcId in Ketra_Two :
            if cond == 2 and VAlliance1 and id == 2 :
                if KBadgeO == 99 :
                    st.giveItems(Ketra_Badge_Officer,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Officer,1)
                    st.playSound("Itemsound.quest_middle")
            elif cond == 3 and VAlliance2 and id == 2 :
                if KBadgeO == 199 :
                    st.giveItems(Ketra_Badge_Officer,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Officer,1)
                    st.playSound("Itemsound.quest_middle")
            elif cond == 4 and VAlliance3 and id == 2 :
                if KBadgeO == 299 :
                    st.giveItems(Ketra_Badge_Officer,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Officer,1)
                    st.playSound("Itemsound.quest_middle")
            elif cond == 5 and VAlliance4 and id == 2 :
                if KBadgeO == 399 :
                    st.giveItems(Ketra_Badge_Officer,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Officer,1)
                    st.playSound("Itemsound.quest_middle")
        elif npcId in Ketra_Three :
            if cond == 3 and VAlliance2 and id == 2 :
                if KBadgeO == 99 :
                    st.giveItems(Ketra_Badge_Captain,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Captain,1)
                    st.playSound("Itemsound.quest_middle")
            elif cond == 4 and VAlliance3 and id == 2 :
                if KBadgeO == 199 :
                    st.giveItems(Ketra_Badge_Captain,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Captain,1)
                    st.playSound("Itemsound.quest_middle")
            elif cond == 5 and VAlliance4 and id == 2 :
                if KBadgeO == 199 :
                    st.giveItems(Ketra_Badge_Captain,1)
                    st.playSound("Itemsound.quest_itemget")
                else :
                    st.giveItems(Ketra_Badge_Captain,1)
                    st.playSound("Itemsound.quest_middle")
        elif npcId in Varka_Silenos :
            decreaseAlliance(st)
            party = st.getPlayer().getParty()
            if party :
                for player in party.getPartyMembers().toArray() :
                    pst = player.getQuestState("611_AllianceWithVarkaSilenos")
                    if pst :
                        decreaseAlliance(pst)
    return

QUEST       = Quest(611,"611_AllianceWithVarkaSilenos","Alliance With Varka Silenos")
CREATED     = State('Start', QUEST)
STARTED     = State('Started', QUEST, True)

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(Naran_Ashanuk)

CREATED.addTalkId(Naran_Ashanuk)
STARTED.addTalkId(Naran_Ashanuk)

for mobId in Ketra_One :
    STARTED.addKillId(mobId)
    STARTED.addQuestDrop(Naran_Ashanuk,Ketra_Badge_Soldier,1)
for mobId in Ketra_Two :
    STARTED.addKillId(mobId)
    STARTED.addQuestDrop(Naran_Ashanuk,Ketra_Badge_Officer,1)
for mobId in Ketra_Three :
    STARTED.addKillId(mobId)
    STARTED.addQuestDrop(Naran_Ashanuk,Ketra_Badge_Captain,1)
for mobId in Varka_Silenos :
    STARTED.addKillId(mobId)

print "importing quests: 611: Alliance With Varka Silenos" 