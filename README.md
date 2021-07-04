![Banner 2](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Banners/Steam_Friends_by_Killer_Boss.gif)

## TouchPortal SteamFriend Plugin
- [TouchPortal SteamFriend Plugin](#TouchPortal-SteamFriend-Plugin)
  - [Description](#description)
  - [Actions/States](#SteamFriend-Actions/States)
  - [Action](#Actions)
  - [States](#States)
  - [Installation Guide](#Installation)
  - [Demo Page](#demo)
	- [Import Demo](#import-demo-page)

## Description
SteamFriend is a Plugin that allow you to see which your friend is online, offline, away etc.. and also see your own games too!

## SteamFriend Actions/States
### Actions
 - Currently This Plugin does Not have any actions 

### States Summary
 - Get Current Online, Offline, Aaway, Busy, Snooze and more!
 - Get Total Friends
 - Get Total Number of Friends in-Game (Any Game)
 - Get List User In-Game
 - Get My Own Icon
 - Get Current X Game maximum achievements
   - Maximum Achievements is What is the Maximum Number of Achievements that the game have
 - Get Current X Game Current Achievements
   - Curret X Game Achievements is whats the current Number of Achievements you've reached 
 - Get Current X Game Achievement percent
   - Shows Percent of Current Achievements / Maximum Number of Achievements
 - Get Total X Game Playtime
 
 #### States Definitions
 - Get
 
Here is the example of the states list it will create game states by your own library.  
 ![image](https://user-images.githubusercontent.com/55416314/120901307-d61c4f80-c5ee-11eb-8e92-7b65ce5e7a95.png)
 
 ## Installation
 1. Go to <a target="_blank" href="https://github.com/KillerBOSS2019/TP-Steam-Friend-Plugin/releases" > Releases </a> ont the main page of this github.
 2. Make sure download right file for your system **Mac-TouchPortalSteamPlugin.tpp** is for macOS users and **Win-TouchPortalSteamPlugin.tpp** for Windows 10 users.
 3. After you have the file head over to touchportal app on your Mac/Win pc.
 4. On the top right click the wrench icon.  
![image](https://user-images.githubusercontent.com/55416314/120901464-ee409e80-c5ef-11eb-907e-fbafd58a8c59.png)
 5. Click `Import plugin-in...` and select the .tpp file you've downloaded in step 2.
 6. Next we need to get an API Key to retrieve data from Steam.(All data is only transfered between Steam and you. I do not collect any data. Feel free to check my code!)  
 7. Go to the following Steam website to attain an [Steam API Key](https://steamcommunity.com/dev/apikey)
    - Login to your steam account if you reach this login page:  
![image](https://user-images.githubusercontent.com/55416314/120901588-cd2c7d80-c5f0-11eb-82e1-00b482a9338b.png)
    - If are already logged in you will see the API key registration page:  
![image](https://user-images.githubusercontent.com/55416314/120901648-154ba000-c5f1-11eb-90bb-80a5e2cd0803.png)
 8. For me i just entered `TPSteamPlugin` for the domain name and checked the box next to `I agree to the Steam Web API Terms of Use` and clicked the green register button.  
 ![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/KeyRegister.png)
 9. After You Clicked Register it will generate your personal API Key. (You can comeback to the same page to revoke the API Key)
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/SteamKey.png)
 10. The API key that I got was `F7E05969F64A0B5134FCB14B96063E60` (This Key is just a example It wont work for you!)  
 11. Save the API key in Notepad for later use.
 12. On the same page click your profile picture in the top right.  
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/Profileclick.png)
 13. Your profile page will look something simalar to this.  
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/SteamProfile.png)
 14. Copy highlighted 17 digit number SteamID in the URL and copy it to Notepad for later use like this:  
![image](https://user-images.githubusercontent.com/55416314/120901930-63ad6e80-c5f2-11eb-8ece-f907454a49f8.png)
 15. Now that we have the API Key and your SteamID goto the TouchPortal App On Desktop again Click the cog icon. 
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/PluginIcon.png) 
 16. This will open another window.
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/PluginSetUp.gif)
 17. Click Plug-ins.  
 18. You will see a drop-down menu next to the `Import plug-in...` Button, if not restart TouchPortal.  
 19. Enter in the SteamID and the API Key into their respective fields.
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/KeyToPlugin.png)
 20. After You inserted everything Click Save.
 21. After you've saved the settings you should go back to the settings again and select steam plugin you should see status shows `Connected` just like this:
 ![image](https://user-images.githubusercontent.com/55416314/120902132-88eeac80-c5f3-11eb-88b4-b3ac73751907.png)

## Demo
A Demo page that shows off some of the features and functionality of TouchPortal Plugin can be found [Here](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Demo/steam-friends.tpz).
Once install it will look like the image below
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Demo/DemoDevice.png)

### Import Demo Page
 1. Download demo page from [Here](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Demo/steam-friends.tpz).  
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Demo/ImportDemo.png)
 2. Click "Manage Page..." button on Touch Portal Main Menu. 
 3. Click "Import Page"
 4. Find the downloaded file steam-friends.tpz and click open  
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Demo/ImportConfirm.png)
 5. Click Yes when this pop-up appears  
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Demo/ImportSucces.png)
 6. Click Ok button to close the import confirmation page  
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Demo/DemoPage.png)
 7. You will now have a new page names steam-friends showing of most fuctions of the plugin.
*Note: Though the page in touch portal does look like it's not doing anything it is. You will see it update with infomation once you are using the app on a device.*  

