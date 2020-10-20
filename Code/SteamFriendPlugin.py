from datetime import datetime
from time import sleep
import json, requests, socket, os, threading, base64, sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
from time import sleep
HOST = '127.0.0.1'
PORT = 12136
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'{"type":"pair","id":"SteamAPI"}\n')
data = s.recv(1024)
print(repr(data))
global running,Key,UserID, canrun
running = False
canrun = False
path = os.getcwd()
filepath = os.path.join(path, "Login.json")
if not os.path.isfile("Login.json"):
        print("Could not find Config.json file. Restoring default settings")
        LoginData = {}
        LoginData["SteamKey"] = "XXXXXXXXXXXXXXXXXXXXXX"
        LoginData["SteamID"] = 0000

        with open("Login.json", "w") as openFile:
            json.dump(LoginData, openFile)
            openFile.close()
loginData = open(filepath).read()
print(loginData)
LoginInfo = json.loads(loginData)
Key = LoginInfo['SteamKey']
UserID = LoginInfo['SteamID']
def nice_time(unixtime1, unixtime2=-1):
    global nicetime
    unixtime1 = int(unixtime1)
    dt1 = datetime.fromtimestamp(unixtime1)

    if unixtime2 == -1:
        unixtime2 = int(datetime.now().timestamp())
    else:
        unixtime2 = int(unixtime2)

    dt2 = datetime.fromtimestamp(unixtime2)

    td = dt1 - dt2

    secs = int(td.total_seconds())
    when = "from now"
    if secs < 0:
        secs = int(abs(secs))
        when = "ago"

    total_minutes, seconds = divmod(secs, 60)
    total_hours, minutes   = divmod(total_minutes, 60)
    total_days, hours      = divmod(total_hours, 24)
    if total_days == 0:
        nicetime = f"{hours} hours, {minutes} minutes, {seconds} seconds {when}"
    if total_hours == 0:
        nicetime = f"{minutes} minutes, {seconds} seconds {when}"
    if total_minutes == 0:
        nicetime = f"{seconds} seconds {when}"
    if total_days != 0:
        nicetime = f"{total_days} days, {hours} hours, {minutes} minutes, {seconds} seconds {when}"
    return nicetime
def Success(SteamKey_Input, SteamID_Input, win):
        global userinfo
        tk.messagebox.showinfo(title="Check Credentials", message='Successfully connect to your Steam!')
        userinfo = json.loads(userinfo.text)
        LoginData = {}
        LoginData['SteamKey'] = SteamKey_Input.get()
        LoginData['SteamID'] = int(SteamID_Input.get())
        with open(os.path.join('Login.json'),'w') as openFile:
                json.dump(LoginData, openFile)
                openFile.close()
                filepath = os.path.join(path, "Login.json")
                loginData = open(filepath).read()
                LoginInfo = json.loads(loginData)
                Key = LoginInfo['SteamKey']
                UserID = LoginInfo['SteamID']
                canrun = True
                win.destroy()
def CheckLogin(SteamKey_Input, SteamID_Input, win):
    global SteamKey, SteamID, Key, UserID
    Key = SteamKey_Input.get()
    UserID = SteamID_Input.get()
    global userinfo
    userinfo = requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s' % (SteamKey_Input.get(), SteamID_Input.get()))
    try:
        try:
                if 'Forbidden' in userinfo.text:
                        print(Error)
                if  Key == '' or UserID == '':
                        print(Error)
                if 'steamid' not in userinfo.text:
                        print(Error)
                Success(SteamKey_Input, SteamID_Input, win)
        except:
                tk.messagebox.showinfo(title="Check Credentials", message='Ether SteamID or SteamKey is invalid. Please Check your SteamKey and SteamID')
    except KeyError:
        print('Key Error')
        tk.messagebox.showinfo(title="Check Credentials", message='Ether SteamID or SteamKey is invalid. Please Check your SteamKey and SteamID')
def createGui():
    win = tk.Tk("Steam Plugin")
    win.title("Steam Plugin")
    win.iconphoto(True, tk.PhotoImage(file=os.path.join("icon.png")))
    def center(w=255, h=180):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        x = (screen_width/2) - (w/2)
        y = (screen_height/2) - (h/2)

        win.geometry("%dx%d+%d+%d" % (w, h, x, y))
    center()
    win.resizable(0,0)
    SteamKey_label = tk.Label(win, text="SteamKey: ")
    SteamID_label = tk.Label(win, text="SteamID: ")

    SteamKey_Input = tk.Entry(win)
    SteamID_Input = tk.Entry(win)
    Submit_button = tk.Button(win, text="Submit", command= lambda: CheckLogin(SteamKey_Input, SteamID_Input, win))
    SteamKey_label.place(x=4,y=30)
    SteamKey_Input.place(x=70,y=30, width=140)

    SteamID_label.place(x=12, y=60)
    SteamID_Input.place(x=70, y=60, width=140)
    Submit_button.place(x=85, y=90)
    win.mainloop()
def CheckLoginJson():
    userinfo = requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s' % (Key, UserID))
    try:
        userinfo = json.loads(userinfo.text)
    except:
        print('test')
        createGui()


running = True
CheckLoginJson()
def start():
    global userinfo, Key, usersteamid, personaname, usericon, friend_steams, UnixTime, td, UserID, TimeGos, friendlistname, Online_User,Offline_User,Busy_User,Away_User,Snooze_User,Looking_to_trade_user,Looking_to_play_User
    global Ingame_User, TotalFriends, raw_icon_Done
    Ingame_User = []
    userinfo = requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s' % (Key, UserID))
    userinfo = json.loads(userinfo.text)
    try:
        usersteamid = userinfo['response']['players'][0]['steamid']
    except IndexError:
            createGui()
    personaname = userinfo['response']['players'][0]['personaname']
    usericon = userinfo['response']['players'][0]['avatarfull']
    raw_icon = requests.get(usericon).content
    raw_icon_Done = base64.b64encode(raw_icon)
    #UnixTime = userinfo['response']['players'][0]['lastlogoff']
    friendlist = requests.get('http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=%s&steamid=%s&relationship=friend' % (Key, UserID))
    friendlist = json.loads(friendlist.text)
    friends = friendlist['friendslist']['friends']
    friend_steams = {}
    friend_games = {}
    TotalFriends = []
    for f in friends:
        gamerequests = requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s' % (Key, f['steamid']))
        gamejson = json.loads(gamerequests.text)
        f_name = gamejson['response']['players'][0]['personaname']
        TotalFriends.append(f_name)
        try:
            gamename = gamejson['response']['players'][0]['gameextrainfo']
        except KeyError:
            if gamejson['response']['players'][0]['personastate'] == 0: 
                gamename = 'Offline'
            if gamejson['response']['players'][0]['personastate'] == 1: 
                gamename = 'Online'
            if gamejson['response']['players'][0]['personastate'] == 2: 
                gamename = 'Busy'
            if gamejson['response']['players'][0]['personastate'] == 3: 
                gamename = 'away'
            if gamejson['response']['players'][0]['personastate'] == 4: 
                gamename = 'Snooze'
            if gamejson['response']['players'][0]['personastate'] == 5: 
                gamename = 'Looking to Trade'
            if gamejson['response']['players'][0]['personastate'] == 6: 
                gamename = 'Looking to play'
            pass
        if gamename in friend_games:
            if not f_name in friend_games[gamename]:
                friend_games[gamename].append(f_name) # add to list
        else:
            friend_games[gamename] = [f_name] # make new list for this game
        try:
            if 'gameid' in gamejson['response']['players'][0]:
                Ingame_User.append(gamejson['response']['players'][0]['personaname'])
        except KeyError:
            Ingame_User = 'Ingame User: No One'
        
        x = nice_time(f['friend_since'])
        friend_steams[f_name] = x
    friendsnumber = 0
    friendinfo = gamejson['response']['players'][0]
    #Getting all the default group states
    try:
        Online_User = friend_games['Online']
    except KeyError:
        Online_User = 'Online User: No One'
    try:
        Offline_User = friend_games['Offline']
    except KeyError:
        Offline_User = 'Offline User: No One'
    try:
        Busy_User = friend_games['Busy']
    except KeyError:
        Busy_User = 'Busy User: No One'
    try:
        Away_User = friend_games['away']
    except KeyError:
        Away_User = 'Away User: No One'
    try:
        Snooze_User = friend_games['Snooze']
    except KeyError:
        Snooze_User = 'Snooze User: No One'
    try:
        Looking_to_trade_user = friend_games['Looking to Trade']
    except KeyError:
        Looking_to_trade_user = 'Looking to trade user: No One'
    try:
        Looking_to_play_User = friend_games['Looking to play']
    except KeyError:
        Looking_to_play_User = 'Looking to play: No One'

        
    if Online_User != 'Online User: No One':
        Online_User = 'Online User: '+ ', '.join(Online_User)
    if Offline_User != 'Offline User: No One':
        Offline_User = 'Offline User: '+ ', '.join(Offline_User)
    if Busy_User != 'Busy User: No One':
        Busy_User = 'Busy User: '+ ', '.join(Busy_User)
    if Away_User != 'Away User: No One':
        Away_User = 'Away User: '+ ', '.join(Away_User)
    if Snooze_User != 'Snooze User: No One':
        Snooze_User = 'Snooze User: '+ ', '.join(Snooze_User)
    if Looking_to_trade_user != 'Looking to trade user: No One':
        Looking_to_trade_user = 'Looking to Trade User: '+ ', '.join(Looking_to_trade_user)
    if Looking_to_play_User != 'Looking to play: No One':
        Looking_to_play_User = 'Looking to Play User: '+ ', '.join(Looking_to_play_User)
    if Ingame_User != 'Ingame User: No One':
        Ingame_User = 'Ingame User: '+ ', '.join(Ingame_User)

    TotalFriends = len(TotalFriends)
    while friendsnumber != len(friend_steams):
        key, val = list( friend_steams.items() ) [friendsnumber]
        friendlistname = key+' Friended Since '+ val
        friendsnumber=friendsnumber+1
def updateStates():
        timer = threading.Timer(10, updateStates)
        timer.start()
        if running:
                start()
                s.sendall(('{"type":"stateUpdate", "id":"Online_User", "value":"%s"}\n' % Online_User).encode())
                s.sendall(('{"type":"stateUpdate", "id":"Offline_User", "value":"%s"}\n' % Offline_User).encode())
                s.sendall(('{"type":"stateUpdate", "id":"Busy_User", "value":"%s"}\n' % Busy_User).encode())
                s.sendall(('{"type":"stateUpdate", "id":"Away_User", "value":"%s"}\n' % Away_User).encode())
                s.sendall(('{"type":"stateUpdate", "id":"Snooze_User", "value":"%s"}\n' % Snooze_User).encode())
                s.sendall(('{"type":"stateUpdate", "id":"Looking_to_trade", "value":"%s"}\n' % Looking_to_trade_user).encode())
                s.sendall(('{"type":"stateUpdate", "id":"Looking_to_play", "value":"%s"}\n' % Looking_to_play_User).encode())
                s.sendall(('{"type":"stateUpdate", "id":"Ingame", "value":"%s"}\n' % Ingame_User).encode())
                s.sendall(('{"type":"stateUpdate", "id":"TotalFriends", "value":"%s"}\n' % TotalFriends).encode())
                s.sendall(('{"type":"stateUpdate", "id":"Base64_UserIcon", "value":"%s"}\n' % raw_icon_Done.decode("ascii")).encode())
        else:
             timer.cancel()

updateStates()
while running:
        data = s.recv(1024)
        sdata = data.decode()
        d = json.loads(sdata)
        print(d)
        if d['type'] == 'closePlugin':
                if d['pluginId'] == 'SteamAPI':
                        s.close
                        print('Touch Portal Plugin has been closed')
                        running = False
