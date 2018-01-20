# -*- coding: utf-8 -*-
#Cat_Bot

import LINETCR
from LINETCR.lib.curve.ttypes import *
from bs4 import BeautifulSoup
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,ast,os,subprocess,requests,wikipedia,urllib2,urllib

cl = LINETCR.LINE()
cl.login(token="EogdTQfvjLK46rIuGCm8.wOOueDmiOnsPzSq34HkxYa.F8rvFF3za92iloflJajDyR7OpS8WCPoEPKsxyIjtxR8=")
cl.loginResult()
print "You've been logged in\n"

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""⛵⛵Annda selfbot⛵⛵

「Commands」
➠  Help
➠ .lurkset 
➠ .lurkview 
➠ .gcreator
➠ .gurl
➠ .curl
➠ .cancel
➠ .wikipedia (Text)
➠ .instagram (Username)
➠ .tagall
➠ .gift
➠ .me
➠ .id@en (Text)
➠ .en@id (Text)
➠ .say-id (Text)
➠ .say-jpn (Text)
➠ .music (Song title)
➠ .play (Song title)
➠ .lyric (Song title)
➠ .image (Contoh: .image ayam)
➠ .steal dp (@nama)
➠ .text (text)
➠ .speed
➠ .status
➠ .refresh
➠ @bye
"""

mid = cl.getProfile().mid
Bots=[mid]
Creator="u5a8a1411d308a0d4a966c437e21297c8"
admin=["ud783cd9e1d44986656da6f0312407448","u5a8a1411d308a0d4a966c437e21297c8","ua508afe5e7dce9bbb0abf42c60967ce2"]
APC=["u1d2bc2ceab5337aeb18478f8d0e48f81","ud783cd9e1d44986656da6f0312407448","ua508afe5e7dce9bbb0abf42c60967ce2","u5a8a1411d308a0d4a966c437e21297c8"]

contact = cl.getProfile()
profile = cl.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

wait = {
    "LeaveRoom":True,
    "AutoJoin":False,
    "Members":1,
    "AutoCancel":False,
    "AutoKick":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "atjointicket":False,
    "Qr":False,
    "Timeline":False,
    "aRead":True,
    "Contact":False,
    "lang":"JP",
    "sticker":True,
    "setkey":True,
    "BlGroup":{}
}

def sendAudioWithURL(self, to_, url):
        path = 'pythonLiness.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e

def sendAudio(self, to_, path):
        M = Message(to=to_,contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass
def findLyric(to,song):
    params = {'songname':song}
    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.urlencode(params))
    data = r.text
    data = json.loads(data)
    for song in data:
        cl.sendText(to,"Lyrics Of " + song[0] + ":\n\n"+ song[5])
        
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

Start = time.time()

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Hours %02d Minutes %02d Seconds' % (hours, mins, secs)    

def updateProfilePicture(self, path, type='p'):
        files = {'file': open(path, 'rb')}
        params = {'oid': self.profile.mid,'type': 'image'}
        if type == 'vp':
            params.update({'ver': '2.0', 'cat': 'vp.mp4'})
        data = {'params': self.genOBSParams(params)}
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/p/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update profile picture failure.')
        return True
        
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "• @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         cl.sendMessage(msg)
    except Exception as error:
        print error
        
#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items 
 
    
def bot(op):
    try:
#--------------------END_OF_OPERATION--------------------
        if op.type == 0:
            return
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e	      
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            cl.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            cl.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM-------------------        
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == admin:
                    if "Kantai join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
#--------------NOTIFIED_INVITE_INTO_GROUP----------------
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    cl.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in mid:
		if op.param2 in mid:
		    cl.acceptGroupInvitation(op.param1)
#-------if mid in op.param3:
#        if op.type == 13:
#           if mid in op.param3:
#            if op.param2 in Creator:
#                cl.acceptGroupInvitation(op.param1)
#            else:
#             G = cl.getGroupIdsJoined()
#             if len(G) <= 200:
#	       cl.acceptGroupInvitation(op.param1)
#	       group = cl.getGroup(op.param1)
#               gMembMids = [contact.mid for contact in group.members]
#               if len(gMembMids) <= 20 or len(gMembMids) >= 500:
#                  cl.sendText(op.param1, "Maaf jumlah Minimal member tidak mencukupi, minimal member 20. Terimakasih.")
#                  time.sleep(1)
#                  cl.leaveGroup(op.param1)
#	     else:
#               cl.acceptGroupInvitation(op.param1)
#               cl.sendText(op.param1,"Type「Help」to start using me ( ° ʖ °)")
#               if op.param1 in G:
#                  pass
#               else:
#                  msg = op.message
#                  cl.sendText(op.param1, "Maksimal grup telah tercapai.")
#                  time.sleep(1)
#                  cl.leaveGroup(op.param1)
#           else:
#                pass                 

#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Bots:
			    pass
		        if op.param2 in Bots:
			    pass
		        else:
		            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        if op.param2 in wait["blacklist"]:
                            pass
		        else:
			    cl.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass

#--------------------------NOTIFIED_UPDATE_GROUP---------------------
            
#--------------------------RECEIVE_MESSAGE---------------------------
        if op.type == 25:
            msg = op.message
#----------------------------------------------------------------------------
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            cl.sendText(msg.to,"already")
                            cl.sendText(msg.to,"already")
                            cl.sendText(msg.to,"already")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            cl.sendText(msg.to,"aded")
                            cl.sendText(msg.to,"aded")
                            cl.sendText(msg.to,"aded")
		    else:
			cl.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        cl.sendText(msg.to,"deleted")
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        cl.sendText(msg.to,"It is not in the black list")
                        cl.sendText(msg.to,"It is not in the black list")
                        
#--------------------------------------------------------
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     cl.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                     else:
                         contact = cl.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = cl.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                
                elif wait["aRead"] == True:
                    if msg.toType == 0:
                        cl.sendChatChecked(msg.from_,msg.id)
                    else:
                        cl.sendChatChecked(msg.to,msg.id)        
                
                elif wait['sticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.sendText(msg.to, filler)
                else:
                    pass

#--------------------------------------------------------
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
                
#--------------------------------------------------------
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif msg.text in ["Runtime"]:
              if msg.from_ in admin:
                eltime = time.time() - Start
                van = "Annda bot has been running for:\n"+waktu(eltime)
                cl.sendText(msg.to,van)
            
            elif msg.text in [".crash"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u5a8a1411d308a0d4a966c437e21297c8,'"}
                cl.sendMessage(msg)
                
            elif msg.text in ["/owner"]:
                msg.contentType = 13
                cl.sendText(msg.to, "📧: kantaiowner@gmail.com")
                msg.contentMetadata = {'mid': Creator}
                cl.sendMessage(msg)
#--------------------------------------------------------
	    elif msg.text in [".Group creator",".Gcreator",".gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
#--------------------------------------------------------
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
                    
#--------------------------------------------------------
            elif msg.text in ["Key","help","Help"]:
                cl.sendText(msg.to,helpMessage)
                
            elif msg.text in ["Ckey","Chelp","chelp"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,creatorMessage)
#--------------------------------------------------------
            elif msg.text in ["List group"]:
		if msg.from_ in Creator:
		    cl.sendText(msg.to,"ちょっと待って下さい。。。")
                    gid = cl.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = cl.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    cl.sendText(msg.to,"======[List Group]======\n"+ h +"Total group: "+str(jml))
		else:
		    cl.sendText(msg.to,"Admin permission required.")
		    
#--------------------------------------------------------
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
		        h = cl.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    cl.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    cl.sendText(msg.to, "Creator permission required.")
#--------------------------------------------------------
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        cl.sendText(msg.to,"nothing")
                        cl.sendText(msg.to,"nothing")
                        cl.sendText(msg.to,"nothing")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +cl.getGroup(gid).name + "\n"
                        cl.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    cl.sendText(msg.to, "Admin permission required.")
		    
#--------------------------------------------------------
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if cl.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    cl.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    cl.sendText(msg.to, "Admin permission required.")
#--------------------------------------------------------
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = cl.getGroupIdsJoined()
		try:
		    if msg.from_ in admin:
                        for i in gid:
                            h = cl.getGroup(i).name
		            if h == ng:
		                cl.inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success join to ["+ h +"] group")
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"Creator permission required.")
		except Exception as e:
		    cl.sendMessage(msg.to, str(e))
#--------------------------------------------------------
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = cl.getGroup(i).name
		        if h == ng:
			    cl.sendText(i,"Bot di paksa keluar oleh owner!")
		            cl.leaveGroup(i)
			    cl.leaveGroup(i)
			    cl.sendText(msg.to,"Success left ["+ h +"] group")
			else:
			    pass
		else:
		    cl.sendText(msg.to,"Creator permission required.")
#--------------------------------------------------------
	    elif "Leave all group" == msg.text:
		gid = cl.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			cl.sendText(i,"Cleaning group..")
			cl.sendText(i,"If you still use this bot please reinvite.")
		        cl.leaveGroup(i)
		    cl.sendText(msg.to,"Success leave all group")
		else:
		    cl.sendText(msg.to,"Creator permission required.")
#--------------------------------------------------------
            elif msg.text in [".cancel",".Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        cl.sendText(msg.to,"No one is inviting")
                else:
                    Cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Ourl","Url:on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url Active")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in [".curl","Url:off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Url inActive")

                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Join on","Autojoin:on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    cl.sendText(msg.to,"AutoJoin Active")
		else:
		    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Join off","Autojoin:off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    cl.sendText(msg.to,"AutoJoin inActive")
		else:
		    cl.sendText(msg.to,"Admin permission required.")
#--------------------------------------------------------
	    elif msg.text in ["Autocancel:on"]:
	      if msg.from_ in admin:     
                wait["AutoCancel"] = True
                cl.sendText(msg.to,"The group of people and below decided to automatically refuse invitation")
		print wait["AutoCancel"][msg.to]

	    elif msg.text in ["Autocancel:off"]:
	      if msg.from_ in admin: 
                wait["AutoCancel"] = False
                cl.sendText(msg.to,"Invitation refused turned off")
		print wait["AutoCancel"][msg.to]
#--------------------------------------------------------
	    elif "Autokick:on" in msg.text:
	      if msg.from_ in admin:
		wait["AutoKick"] = True
		cl.sendText(msg.to,"AutoKick Active")

	    elif "Autokick:off" in msg.text:
	      if msg.from_ in admin: 
		wait["AutoKick"] = False
		cl.sendText(msg.to,"AutoKick inActive")
#--------------------------------------------------------
            elif msg.text in [".k on","Contact:on"]:
              if msg.from_ in admin:    
                wait["Contact"] = True
                cl.sendText(msg.to,"Contact Active")

            elif msg.text in [".k off","Contact:off"]:
              if msg.from_ in admin:    
                wait["Contact"] = False
                cl.sendText(msg.to,"Contact inActive")
#--------------------------------------------------------                
            elif msg.text in ["Status"]:
                md = ""
		if wait["AutoJoin"] == True: md+="✦ Auto join : on\n"
                else: md +="✦ Auto join : off\n"
		if wait["Contact"] == True: md+="✦ Info Contact f: on\n"
		else: md+="✦ Info Contact : off\n"
                if wait["AutoCancel"] == True:md+="✦ Auto cancel : on\n"
                else: md+= "✦ Auto cancel : off\n"
		if wait["Qr"] == True: md+="✦ Qr Protect : on\n"
		else:md+="✦ Qr Protect : off\n"
		if wait["AutoKick"] == True: md+="✦ Autokick : on\n"
		else:md+="✦ Autokick : off"
                cl.sendText(msg.to,"=====[Status]=====\n"+md)
                
#--------------------------------------------------------
            elif msg.text in [".Gift",".gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            
            elif ".play " in msg.text:
                try:
                    songname = msg.text.replace(".play ","")
                    cl.sendText(msg.to,"ちょっと待って下さい。。。")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = '\nLink Download : ' + song[4]
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
            
            elif ".music " in msg.text:
                try:
                    songname = msg.text.replace(".music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Title : ' + song[0]
                        hasil += '\nDuration : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
            
            elif ".lyric " in msg.text:
                songname = msg.text.replace(".lyric ","")
                params = {"songname": songname}
                r=requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data=r.text
                data=json.loads(data)
                for song in data:
                    songz = song[5].encode('utf-8')
                    lyric = songz.replace('ti:','Title -')
                    lyric = lyric.replace('ar:','Artist -')
                    lyric = lyric.replace('al:','Album -')
                    removeString = "[1234567890.:]"
                    for char in removeString:
                        lyric = lyric.replace(char,'')
                    cl.sendText(msg.to, "Judul: " + song[0].encode('utf-8') + "\n\n" + lyric)
            
            elif ".say-id " in msg.text:
                query = msg.text.replace(".say-id ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                    params = {'language': 'id', 'speed': '1', 'query': query}
                    r = s.get(url, params=params)
                    mp3 = r.url
                    cl.sendAudioWithURL(msg.to, mp3)   
            
            elif ".say-jpn " in msg.text:
                query = msg.text.replace(".say-jpn ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'https://google-translate-proxy.herokuapp.com/api/tts'
                    params = {'language': 'ja', 'speed': '1', 'query': query}
                    r = s.get(url, params=params)
                    mp3 = r.url
                    cl.sendAudioWithURL(msg.to, mp3)   
                    
            elif ".image " in msg.text:
                  cl.sendText(msg.to, "ちょっと待って下さい。。。")
                  start = time.time()
                  keyword = msg.text[7:]
                  key = keyword.strip('@#$&?!/_,*"\£¢€¥^°={}~`|•√π÷×¶∆<>`[]|;')
                  search = key.replace(' ','%20')
                  url = 'https://www.google.com/search?q=' + search +  '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
                  raw_html =  (download_page(url))
                  items = []
                  items = items + (_images_get_all_items(raw_html))
                  path = random.choice(items)
                  elapsed_time = time.time() - start
                  try:
                      cl.sendImageWithURL(msg.to,path)
                  except:
                     pass   
                 
#--------------------------------------------------------

            elif msg.text.lower() == '.tagall':
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8),"M":i.mid})
                        s += 9
                        txt += u'@Plerzzz\n'
                    msg.text = txt+'\nDone : '+str(len(group.members))+' Members'
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                   
                    cl.sendMessage(msg)     

#	    elif msg.text in [".tagall"]:
#                  group = cl.getGroup(msg.to)
#                  nama = [contact.mid for contact in group.members]
#
#                  cb = ""
#                  cb2 = ""
#                  strt = int(0)
#                  akh = int(0)
#                  for md in nama:
#                      akh = akh + int(6)
#
#                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
#
#                      strt = strt + int(7)
#                      akh = akh + 1
#                      cb2 += "@nrik \n"
#
#                  cb = (cb[:int(len(cb)-1)])
#                  msg.contentType = 0
#                  msg.text = cb2
#                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
#
#                  try:
#                      cl.sendMessage(msg)
#                  except Exception as error:
#                      print error
                      
#--------------------------------------------------------   
	    elif ".backup" in msg.text:
		try:
		    cl.updateDisplayPicture(profile.pictureStatus)
		    cl.updateProfile(profile)
		    cl.sendText(msg.to, "Success backup profile")
		except Exception as e:
		    cl.sendText(msg.to, str(e))
#--------------------------------------------------------
	    elif ".copy " in msg.text:
                copy0 = msg.text.replace("Copy ","")
                copy1 = copy0.lstrip()
                copy2 = copy1.replace("@","")
                copy3 = copy2.rstrip()
                _name = copy3
		group = cl.getGroup(msg.to)
		for contact in group.members:
		    cname = cl.getContact(contact.mid).displayName
		    if cname == _name:
			cl.CloneContactProfile(contact.mid)
			cl.sendText(msg.to, "Success~")
		    else:
			pass
#--------------------------------------------------------            
            elif msg.text in [".ban"]:
             if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")

            elif msg.text in [".unban"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
#--------------------------CEK SIDER------------------------------
            elif ".lurkset" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to, "Lurk has been set!")
                print "@.lurkset"

            elif ".lurkview" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' 「'+timeSeen[v]+'」')
                        pass
                    if len(dataResult) > 0:
                        tukang = "List Viewer\n➠"
                        grp = '\n➠ '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers 「%s」' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        cl.sendText(msg.to, "Autolurk has been set!")
                        print "@autolurk"
                    else:
                        cl.sendText(msg.to, "Viewers not found.")
                    print "@lurkview"
#--------------------------------------------------------

#KICK_BY_TAG
	    elif "Boom " in msg.text:
		if msg.from_ in APC:
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    cl.kickoutFromGroup(msg.to,[mention['M']])
		else:
		    cl.sendText(msg.to, "Creator permission required.")
#--------------------------------------------------------
	    elif "Set member: " in msg.text:
		if msg.from_ in admin:
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)
		else:
		    cl.sendText(msg.to, "Admin permission required.")
#--------------------------------------------------------
	    elif "Add all" in msg.text:
		if msg.from_ in admin:
		    thisgroup = cl.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    cl.findAndAddContactsByMids(mi_d)
		    cl.sendText(msg.to,"Success Add all")
		else:
		    cl.sendText(msg.to, "Admin permission required.")
#--------------------------------------------------------
#	    elif "Recover" in msg.text:
#		thisgroup = cl.getGroups([msg.to])
#		Mids = [contact.mid for contact in thisgroup[0].members]
#		mi_d = Mids[:33]
#		cl.createGroup("Recover", mi_d)
#		cl.sendText(msg.to,"Success recover")
#--------------------------------------------------------
	    elif msg.text in ["Remove all chat"]:
		cl.removeAllMessages(op.param2)
		cl.removeAllMessages(op.param2)
		cl.removeAllMessages(op.param2)
		cl.removeAllMessages(op.param2)
		cl.sendText(msg.to,"Complete.")
		
#--------------------------------------------------------
            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------------
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------------
#            elif msg.text in ["#welcome","Welcome","welcome","Welkam","welkam"]:
#                gs = cl.getGroup(msg.to)
#                cl.sendText(msg.to,"Welcome to "+ gs.name)
#--------------------------------------------------------
	    elif "Kbc " in msg.text:
		bctxt = msg.text.replace("Kbc ", "")
		n = cl.getGroupIdsJoined()
		if msg.from_ in admin:
		    for manusia in n:
			cl.sendText(manusia, (bctxt))	    
		else:
		    cl.sendText(msg.to,"Admin permission required.")
		    
#--------------------------------------------------------
            elif '.wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace(".wikipedia ","")
                      cl.sendText(msg.to,"ちょっと待って下さい。。。")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Woops, i think this to much. Please read this article.\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
                
            elif ".id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace(".id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"ғʀᴏᴍ ɪᴅ:\n" + "" + kata + "\n\nᴛᴏ ᴇɴ:\n" + "" + result)        
                
            elif ".en@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace(".en@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                cl.sendText(msg.to,"ғʀᴏᴍ ᴇɴ\n" + "" + kata + "\n\nᴛᴏ ɪᴅ:\n" + "" + result)
                
            elif ".text " in msg.text:
                cl.sendText(msg.to, "ちょっと待って下さい。。。")
                text = msg.text[5:]
                txt = text.replace(' ','%20')
                lo = subprocess.check_output('curl -s http://api.img4me.com/?text='+txt+'&font=arial&fcolor=FFFFFF&size=35&bcolor=000000&type=jpg',shell=True)
                path = lo
                cl.sendImageWithURL(msg.to,path)
                
            elif msg.text in ["Quote"]:
                path = "http://www.baltana.com/download/802/1024x1024/crop/code-quotes-hd-wallpaper-00768.jpg"
                cl.sendImageWithURL(msg.to,path)   
             
#--------------------------------------------------------------------------------------------------------------------------------------            
            elif msg.text in ["Bbc ruz"]:
                path = "https://i.imgur.com/fHvNvKw.jpg"
                cl.sendImageWithURL(msg.to,path) 
            
            elif msg.text in ["Hmm","hmm"]:
                path = "https://transfer.sh/n1KmG/1515995348782.jpg"
                cl.sendImageWithURL(msg.to,path)
                
            elif ".show " in msg.text:
                 linkfoto = msg.text.replace(".show ","")
                 cl.sendImageWithURL(msg.to, linkfoto)

            elif msg.text in ["Hore"]:
                path = "https://transfer.sh/fZD6A/voice_527867.aac"
                cl.sendAudioWithURL(msg.to,path)
                
            elif msg.text in ["/anuan"]:    
                path = "https://transfer.sh/Ikmsb/voice_35806.aac"    
                cl.sendAudioWithURL(msg.to,path)
                
            elif msg.text in ["/play garox circulation"]:  
                path = "https://transfer.sh/10GzvC/Garox%20Circulation.mp3"    
                cl.sendAudioWithURL(msg.to,path)    
                
            elif msg.text in ["/play kururu ifudoudou"]:  
                path = "https://transfer.sh/gZKLU/Kururu%20-%20Ifudodou.mp3"    
                cl.sendAudioWithURL(msg.to,path)
                
            elif msg.text in ["/play garox miru"]:  
                path = "https://transfer.sh/xRFuD/Garox%20Miru%20%28Sub%20CCLyric%29.mp3"    
                cl.sendAudioWithURL(msg.to,path)    
                
            elif msg.text in ["Semangat ya"]:    
                path = "https://transfer.sh/dMQZ5/voice_1746939.aac"
                cl.sendAudioWithURL(msg.to,path)
                
            elif msg.text in ["Bbc ari"]:
                path = "https://i.imgur.com/u2Ysrsr.jpg"
                cl.sendImageWithURL(msg.to,path) 
                
            elif msg.text in ["Kucing terjun"]:
                path = "https://media3.giphy.com/media/l4KibK3JwaVo0CjDO/giphy.gif"
                cl.sendGifWithURL(msg.to,path) 
              
            elif "Kacang" in msg.text:
                peanut = ("https://cdn.pixabay.com/photo/2010/12/13/09/51/peanut-1750_960_720.jpg")
                cl.sendImageWithURL(msg.to,peanut)
            
            elif msg.text in [".server time"]:
                a = datetime.now().strftime('%d %B %Y. %H:%M%p') + "♪♪"
                cl.sendText(msg.to, a)
     
            elif "Filter mem" in msg.text:
              if msg.from_ in Creator:
                G = cl.getGroupIdsJoined()
                _list = ""
                for i in G:                   
	            group = cl.getGroup(i)
                gMembMids = [contact.mid for contact in group.members]
                if len(gMembMids) <= 20:
                       _list += group.name
                       time.sleep(1)
                       cl.leaveGroup(i)
                       cl.sendText(msg.to,"Terfilter :" + _list)
             
            elif ".quotes" in msg.text:
					  r = requests.get('https://talaikis.com/api/quotes/random/')
					  data = r.text
					  data = json.loads(data)
					  a = data['quote']
					  b = data['author']
					  c = data['cat']
					  hasil = ("[Random Quote]"+"\n"+"Author: "+b+"\n"+"Category: "+c+"\n"+"Quote: "+a)
					  cl.sendText(msg.to, hasil)
            
            elif "Accall" in msg.text:
                 if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)                   
                            _list += gids.name
                            cl.acceptGroupInvitation(i)         
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil masuk ke group :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")
                        
#--------------------------------------------------------
            elif ".instagram " in msg.text.lower():
                   try:
                        nk1 = msg.text.replace(".instagram ","")
                        response = requests.get('https://www.instagram.com/'+nk1+'/?__a=1')
                        data = response.json()
                        username = str(data['user']['username'])
                        fullname = str(data['user']['full_name'])
                        path = data['user']['profile_pic_url_hd']
                        followers = str(data['user']['followed_by']['count'])
                        following = str(data['user']['follows']['count'])
                        media = str(data['user']['media']['count'])
                        bio = str(data['user']['biography'])
                        url = str(data['user']['external_url'])
                        cl.sendImageWithURL(msg.to,path)
                        cl.sendText(msg.to,"Profile "+username+"\n\nUsername : "+username+"\nFull Name :"+fullname+"\nFollowers : "+str(followers)+"\nFollowing : "+str(following)+"\nPost :"+str(media)+"\nBio : "+bio)
                        print '[Command] Instagram'
                   except Exception as e:
                        cl.sendText(msg.to,str(e))
 #------------------------------------------------------------------           
            elif ".steal home @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace(".steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#------------------------------------------------------------------
            elif ".steal dp @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace(".steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#--------------------------------------------------------            
            elif msg.text in [".gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            
            elif ".crash @" in msg.text:
                if msg.contentType == 13:
                    msg.contentMetadata = {'mid': "u5a8a1411d308a0d4a966c437e21297c8,'"}
                    _name = msg.text.replace(".crash @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           cl.sendText(g.mid,msg)
                           
            elif msg.text in ["Kernel","kernel"]:
                 if msg.from_ in admin:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     cl.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
                 else:
                     cl.sendText(msg.to,"Command denied.")
                     cl.sendText(msg.to,"Admin permission required.")
            elif msg.text.lower() == 'ipconfig':     
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
#--------------------------------------------------------
	    elif msg.text in ["Kantai like"]:
		try:
		    print "activity"
		    url = cl.activity(limit=1)
		    print url
		    cl.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    cl.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Auto like by Hiromitsu.\nPlease support me by inviting me to your group.")
		    cl.sendText(msg.to, "Success~")
		except Exception as E:
		    try:
			cl.sendText(msg.to,str(E))
		    except:
			pass
			
#--------------------------------------------------------
	    elif "Kname: " in msg.text:
	      if msg.from_ in admin: 
                string = msg.text.replace("Kname: ","")
                if len(string.decode('utf-8')) <= 60000000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
        
#--------------------------------------------------------
            elif msg.text in ["timeline"]:
		try:
                    url = cl.activity(limit=5)
		    cl.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E
#--------------------------------------------------------
            elif msg.text in ["@bye"]:
		    cl.sendText(msg.to,"Good bye. See you next time.")
		    cl.leaveGroup(msg.to)
#--------------------------------------------------------
            elif msg.text in ["Sp","Speed"]:
                if msg.from_ in admin:        
                    start = time.time()
                    cl.sendText(msg.to, "ちょっと待って下さい。。。")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%ss" % (elapsed_time))
                    
            elif msg.text in [".speed"]:
                cl.sendText(msg.to, "ちょっと待って下さい。。。")
                start = time.time()
                time.sleep(0.09)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s sᴇᴄᴏɴᴅs♪♪" % (elapsed_time))    
                print "[Command]Speed executed"
            
            elif msg.text in [".status"]:
                start = time.time()
                time.sleep(0.08)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "「sʏsᴛᴇᴍ sᴇᴛᴛɪɴɢ」\nᴀᴜᴛᴏ ʟᴜʀᴋ: on\nsᴘᴇᴇᴅ: %s\nᴠᴇʀsɪᴏɴ: 1.7.9" % (elapsed_time))
                print "[Command]Speed executed"
            
            elif msg.text in [".shutdown"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,"「Shutdown」\nsʜᴜᴛᴅᴏᴡɴ sᴛᴀʀᴛɪɴɢ ɪɴ 10 sᴇᴄ♪\nᴛʏᴘᴇ「.abort」ᴛᴏ ᴄᴀɴᴄᴇʟ.")
                    time.sleep(10.00)
                    cl.sendText(msg.to,"ʙᴏᴛ ʜᴀs ʙᴇᴇɴ sʜᴜᴛᴅᴏᴡɴ.")
                    exit(1)
            
            elif ".repeat: " in msg.text:
                if msg.from_ in admin:
					bctxt = msg.text.replace(".repeat: ","")
					cl.sendText(msg.to,(bctxt))
					cl.sendText(msg.to,(bctxt))
					cl.sendText(msg.to,(bctxt))
					cl.sendText(msg.to,(bctxt))
#--------------------------------------------------------
            elif msg.text in [".me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg)
                
            elif msg.text in ["Respon"]:
              if msg.from_ in admin:    
		cl.sendText(msg.to,"Annda here  \(ˆ▿ˆ)/")
		    
		    
#--------------------------------------------------------
            elif ".buldozer" == msg.text:
		if msg.from_ in Creator:
                    if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Buldozer","")
                        gs = cl.getGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"Sampai jumpaa~")
                        cl.sendText(msg.to,"Dadaaah~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found.")
                            cl.sendText(msg.to,"Not found.")
                            cl.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        klist=[cl]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        cl.sendText(msg.to,str(e))
			    cl.inviteIntoGroup(msg.to, targets)
			    
			    
#--------------------------------------------------------
#Restart_Program
	    elif msg.text in ["bot:restart"]:
		if msg.from_ in Creator:
		    cl.sendText(msg.to, "Bot has been restarted.")
		    restart_program()
		    print "@Restart"
		else:
		    cl.sendText(msg.to, "No Access.")

#Refresh_Program
	    elif msg.text in [".refresh"]:
		    cl.sendText(msg.to, "Bot has been refreshed.")
		    restart_program()
		    print "@Refresh"
		    
        if op.type == 59:
            print op


    except Exception as error:
        print error


#thread2 = threading.Thread(target=nameUpdate)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

