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
 
 Here is the example of the States List It will create Game States by your own Library  
 ![image](https://user-images.githubusercontent.com/55416314/120901307-d61c4f80-c5ee-11eb-8e92-7b65ce5e7a95.png)
 
 ## Installation
 1. Go to <a target="_blank" href="https://github.com/KillerBOSS2019/TP-Steam-Friend-Plugin/releases" > Releases </a>
 2. Make Sure Download Right file for Your System **Mac-TouchPortalSteamPlugin.tpp** is for Mac OS and **Win-TouchPortalSteamPlugin.tpp** For Windows 10 User.
 3. After You have the File Head over to TouchPortal App on your Win/Mac PC
 4. On Top Right You should see Something Like this.  
![image](https://user-images.githubusercontent.com/55416314/120901464-ee409e80-c5ef-11eb-907e-fbafd58a8c59.png)
 6. Click `Import plugin-in...` And Select The .tpp File you've Downloaded in Step 2
 7. Next We need to create a API Key for it to get your Data (This is Safe I Do NOT Collect Data from you You're welcome to see the code!)  
 8. Go Here to Create [Steam API Key](https://steamcommunity.com/dev/apikey)
    - If You see This then Just login to your Steam Account:  
![image](https://user-images.githubusercontent.com/55416314/120901588-cd2c7d80-c5f0-11eb-82e1-00b482a9338b.png)
    - If You already Login You should see This:  
![image](https://user-images.githubusercontent.com/55416314/120901648-154ba000-c5f1-11eb-90bb-80a5e2cd0803.png)
 9. For me I just Input `TPSteamPlugin` in the Domain Name and Click `I agree to the Steam Web API Terms of Use` and Click Register.  
 ![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/KeyRegister.png)
 10. After You Clicked Register it should take you to a page like this.  
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/SteamKey.png)
 11. Copy The key in that page for me it would be `F7E05969F64A0B5134FCB14B96063E60` (This Key is just a example It wont work for you!)  
 12. Save that Key somewhere like in Nodpade
 13. In That Same Page Click Your Profile.  
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/Profileclick.png)
 14. Now it should take you somewhere Like this Page.  
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/SteamProfile.png)
 15. Copy that thing that are under the blue line in that ScreenShot and put that also in a Notepad like This:  
![image](https://user-images.githubusercontent.com/55416314/120901930-63ad6e80-c5f2-11eb-8ece-f907454a49f8.png)
 16. After all that Work Let's head over to TouchPortal App On Desktop again Click. 
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/PluginIcon.png) 
 17. And it'll Open another Window and Next Click Plug-ins On The Sidebar
![image](https://github.com/cj2tech/TP-Steam-Friend-Plugin/blob/main/Images/Install/PluginSetUp.gif)
 19. And Now You should see a Drop Down Menu Should be Next to `Import plug-in...` Button And Select `TouchPortal Steam Plugin` (If You Dont see that Item in the Menu Dont warry just Restart your TouchPortal)
 20. Now You can popup the Nodpade you've saved And enter the Info in the Settings.  
 ![image](https://user-images.githubusercontent.com/55416314/120902077-209fcb00-c5f3-11eb-9d50-ca5e808dcbc9.png)
 20. After You inserted Everything like mine Click Save
 21. After You've Saved the Settings you should go back to the settings again and select Steam Plugin You should see Status shows `Connected` Just like this  
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

