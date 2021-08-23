import requests, json, socket, datetime,threading, base64, sys

# Touch Portal connection
HOST = '127.0.0.1'
PORT = 12136

# Connect & pair
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'{"type":"pair","id":"SteamAPI"}\n')
data = s.recv(1024)
print(repr(data))

# Steam API Key
Key = json.loads(data)['settings'][0]['API Key: ']
UserID = json.loads(data)['settings'][1]['Steam ID: ']

# Var
running = True
useringame = 0


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
def getGameAchievements():
    game_achievementlist = []
    GameID_list = []
    gamelist = requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={Key}&steamid={UserID}&format=json').json()
    for game in gamelist['response']['games']:
        if round(int(game['playtime_forever'])/60) < 1:
            gameplaytime = str(game['playtime_forever'])+" minutes"
        else:
            gameplaytime = str(round(int(game['playtime_forever'])/60))+" hours"
        GameID_list.append((game['appid'], gameplaytime))
    for x in GameID_list:
        game_achievements = requests.get(f'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={x[0]}&key={Key}&steamid={UserID}').json()
        number_achievements = 0
        maxium_achievements = len(game_achievements['playerstats']['achievements'])
        game_name = game_achievements['playerstats']['gameName']
        for achievement in game_achievements['playerstats']['achievements']:
            if achievement['achieved'] == 1:
                number_achievements = number_achievements + 1
        game_achievementlist.append({game_name: {"maximum achievements": int(maxium_achievements), "Current Number achievements": int(number_achievements), "complete": int(int(number_achievements)/maxium_achievements*100), "Play time": x[1]}})
    return game_achievementlist
def getPlayerGameData():
    global useringame
    friendlist = requests.get('http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=%s&steamid=%s&relationship=friend' % (Key, UserID)).json()['friendslist']['friends']

    print(friendlist)
    Gamelist = []
    useringame = []
    offlineuser = []
    onlineuser = []
    busyuser = []
    awayuser = []
    snoozeuser = []
    lttuser = []
    ltpuser = []
    ImageData = requests.get(requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s' % (Key, UserID)).json()['response']['players'][0]['avatarfull']).content
    ImageData = base64.b64encode(ImageData)
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.Base64_UserIcon", "value":"%s"}\n' % ImageData.decode("ascii")).encode())
    for friend in friendlist:
        gamerequests = requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s' % (Key, friend['steamid'])).json()
        try:
            Gamelist.append((gamerequests['response']['players'][0]['personaname'], gamerequests['response']['players'][0]['gameextrainfo']))
            useringame.append(gamerequests['response']['players'][0]['personaname'])
        except:
            if gamerequests['response']['players'][0]['personastate'] == 0:
                offlineuser.append(gamerequests['response']['players'][0]['personaname'])
            elif gamerequests['response']['players'][0]['personastate'] == 1:
                onlineuser.append(gamerequests['response']['players'][0]['personaname'])
            elif gamerequests['response']['players'][0]['personastate'] == 2:
                busyuser.append(gamerequests['response']['players'][0]['personaname'])
            elif gamerequests['response']['players'][0]['personastate'] == 3:
                awayuser.append(gamerequests['response']['players'][0]['personaname'])
            elif gamerequests['response']['players'][0]['personastate'] == 4:
                snoozeuser.append(gamerequests['response']['players'][0]['personaname'])
            elif gamerequests['response']['players'][0]['personastate'] == 5:
                lttuser.append(gamerequests['response']['players'][0]['personaname'])
            elif gamerequests['response']['players'][0]['personastate'] == 6:
                ltpuser.append(gamerequests['response']['players'][0]['personaname'])
    game_dict = {}
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Number.Ingame", "value":"%s"}\n' % len(useringame)).encode())
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Number.Online_User", "value":"%s"}\n' % len(onlineuser)).encode())
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Number.Offline_User", "value":"%s"}\n' % len(offlineuser)).encode())
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Number.Busy_User", "value":"%s"}\n' % len(busyuser)).encode())
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Number.Away_User", "value":"%s"}\n' % len(awayuser)).encode())
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Number.Snooze_User", "value":"%s"}\n' % len(snoozeuser)).encode())
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Number.Looking_to_trade", "value":"%s"}\n' % len(lttuser)).encode())
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Number.Looking_to_play", "value":"%s"}\n' % len(ltpuser)).encode())


    for c in "]['":
        useringame = str(useringame).replace(c, '')
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.User.Ingame", "value":"%s"}\n' % useringame).encode())
    for c in "]['":
        onlineuser = str(onlineuser).replace(c, '')
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Online_User", "value":"%s"}\n' % onlineuser).encode())
    for c in "]['":
        offlineuser = str(offlineuser).replace(c, '')
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Offline_User", "value":"%s"}\n' % offlineuser).encode())
    for c in "]['":
        busyuser = str(busyuser).replace(c, '')
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Busy_User", "value":"%s"}\n' % busyuser).encode())
    for c in "]['":
        awayuser = str(awayuser).replace(c, '')
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Away_User", "value":"%s"}\n' % awayuser).encode())
    for c in "]['":
        snoozeuser = str(snoozeuser).replace(c, '')
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Snooze_User", "value":"%s"}\n' % snoozeuser).encode())
    for c in "]['":
        lttuser = str(lttuser).replace(c, '')
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Looking_to_trade", "value":"%s"}\n' % lttuser).encode())
    for c in "]['":
        ltpuser = str(ltpuser).replace(c, '')
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.Looking_to_play", "value":"%s"}\n' % ltpuser).encode())
    s.sendall(('{"type":"stateUpdate", "id":"KillerBOSS.TPPlugin.DefaultStatus.TotalFriends", "value":"%s"}\n' % len(friendlist)).encode())
    for player, game in Gamelist:
        game_dict.setdefault(game,list())
        game_dict[game].append(player)
    return game_dict


def CheckAPIKey(API,ID):
    global Key, UserID, UpdateStart
    check = requests.get('http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=%s&steamid=%s&relationship=friend' % (API, ID)).status_code
    if check == 200:
        s.sendall(('{"type":"settingUpdate", "name":"status", "value":"Connected"}\n').encode())
        Key = API
        UserID = ID
        UpdateStart = True
    else:
        s.sendall(('{"type":"settingUpdate", "name":"status", "value":"Disconnected"}\n').encode())
        UpdateStart = False
UpdateStart = False
if Key != "" or UserID != "":
    CheckAPIKey(Key,UserID)
else:
    UpdateStart = False
OLD_Gamelist = []
oldgameAchievements_list = 0
def update():
    global OLD_Gamelist, oldgameAchievements_list
    if running:
        thread = threading.Timer(60, update)
        thread.start()
        print('test')
        if UpdateStart:
            print('getting data')
            New_list = getPlayerGameData()
            print(New_list)
            if New_list != OLD_Gamelist:
                for x in New_list.keys():
                    print(f'creating new Game value {x}')
                    s.sendall(('{"type":"createState", "id":"%s", "desc":"Player playing %s", "defaultValue":"0"}\n' % ("SteamPlugin."+x,x)).encode())
                    s.sendall(('{"type":"createState", "id":"%s", "desc":"Player playing (in Number) %s", "defaultValue":"0"}\n' % ("SteamPlugin."+x+".Number",x)).encode())
                for x in OLD_Gamelist:
                    if x not in New_list:
                        print(f'removing {x}')
                        s.sendall(('{"type":"removeState","id":"%s"}\n' % ("SteamPlugin."+x)).encode())
                        s.sendall(('{"type":"removeState","id":"%s"}\n' % ("SteamPlugin."+x+".Number")).encode())
                OLD_Gamelist = New_list
            for x in New_list.keys():
                NormalGamedata = str(New_list[x]).replace(']','')
                NormalGamedata = NormalGamedata.replace('[','')
                NormalGamedata = NormalGamedata.replace("'",'')
                print(New_list.keys(), New_list[x])
                s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("SteamPlugin."+x,NormalGamedata)).encode())
                s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("SteamPlugin."+x+".Number",len(New_list[x]))).encode())
            if getGameAchievements() != oldgameAchievements_list:
                for i in getGameAchievements():
                    s.sendall(('{"type":"createState", "id":"%s", "desc":"%s", "defaultValue":"0"}\n' % ("SteanPlugin.Achievements.game."+list(i.keys())[0]+".maximum_achievements", f"Achievement {list(i.keys())[0]} maximum achievements")).encode())
                    s.sendall(('{"type":"createState", "id":"%s", "desc":"%s", "defaultValue":"0"}\n' % ("SteanPlugin.Achievements.game."+list(i.keys())[0]+".current_achievements", f"Achievement {list(i.keys())[0]} current achievements")).encode())
                    s.sendall(('{"type":"createState", "id":"%s", "desc":"%s", "defaultValue":"0"}\n' % ("SteanPlugin.Achievements.game."+list(i.keys())[0]+".achievement_percent", f"Achievement {list(i.keys())[0]} Achievement percent")).encode())
                    s.sendall(('{"type":"createState", "id":"%s", "desc":"%s", "defaultValue":"0"}\n' % ("SteanPlugin.Achievements.game."+list(i.keys())[0]+".totalPlaytime", f"Achievement {list(i.keys())[0]} total playtime")).encode())
                    oldgameAchievements_list = getGameAchievements()
            else:
                for x in oldgameAchievements_list:
                    print(x[list(x.keys())[0]])
                    s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("SteanPlugin.Achievements.game."+list(x.keys())[0]+".maximum_achievements", x[list(x.keys())[0]]['maximum achievements'])).encode())
                    s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("SteanPlugin.Achievements.game."+list(x.keys())[0]+".current_achievements", x[list(x.keys())[0]]['Current Number achievements'])).encode())
                    s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("SteanPlugin.Achievements.game."+list(x.keys())[0]+".achievement_percent", x[list(x.keys())[0]]['complete'])).encode())
                    s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("SteanPlugin.Achievements.game."+list(x.keys())[0]+".totalPlaytime", x[list(x.keys())[0]]['Play time'])).encode())
                
    else:
        thread.cancel()
update()
def buffered_readLine(socket):
    line = bytearray()
    while True:
        part = socket.recv(1)
        if part != b'\n':
            line.extend(part)
        else:
            break
    return line
while running:
    try:
        d = json.loads(buffered_readLine(s))
    except:
        sys.exit()
    if d['type'] != 'settings':
        print(d)
    if d['type'] == 'closePlugin':
        if d['pluginId'] == 'SteamAPI':
            running = False
            s.sendall(('{"type":"settingUpdate", "name":"status", "value":"Disconnected"}\n').encode())
            print('Touch Portal Plugin has been closed')
            sys.exit()
    if d['type'] == "settings":
        CheckAPIKey(d['values'][0]['API Key: '],d['values'][1]['Steam ID: '])
