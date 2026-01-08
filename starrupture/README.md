# StarRupture

StarRupture is a first-person open world base-building game with advanced combat and tons of exploration. Play alone or in a group on this sublime and ever-changing planet, extract and manage resources, create your complex industrial system and fight off hordes of alien monsters.

## Server software is still in experimental fase.
So expect some breaks in future!

 ### Author & Contributers
| Name        | Github Profile  |
| ------------- |-------------|
|   brainshead   | https://github.com/brainshead |
|   SavageCore   | https://github.com/SavageCore |

## Server Ports

StarRupture requires up to 1 ports

| Port    | default       |
|---------|---------------|
| Game    | 7777          |

This can be changed to any port.

## Install Notes

| Requirements        | Memory| Storage |
|---------------------|-------|---------|
| Minimal             | 2GB   | 25 GB   |
| Recommended         | 4+ GB| 40GB+  |


## Settings
 ### Password protecting your server
 > ⚠️ Anyone that knows your IP and port can join your server if no password is set!

  If you wish to setup a password you will have to do this before using DSSettings.txt below. We are currently not aware of any method to configure a password either via parameters or DSSettings.txt.

  1. Start your server, ensuring no DSSettings.txt file exists
  2. Open the StarRupture game client
  3. Connect to your server using the in game Server Manager from the main menu
  4. The game will first ask you to configure an Admin Password, do this
  5. Click the Change Password button in the Server Manager dialog
  6. Enter the join password that players will use when connecting to your server.
  7. Click Back (or press ESC) Do not attempt to create a new game or load a game at this point
  8. Stop your server and contiune with the DSSettings.txt configuration above

 ### Creating and Loading Save Games
1. ### By using in-game Server management.
   On the main menu of the game, click on Manage Server and enter your ip and port to connect to your server.
   From here you can create a new world or load an existing save.

2. ### Manual way (no password protection)
   Create `DSSettings.txt` in root `(/home/container/)`
   Paste this inside

  ```
{
  "SessionName": "MySaveGame",
  "SaveGameInterval": "300",
  "StartNewGame": "false",
  "LoadSavedGame": "true",
  "SaveGameName": "AutoSave0.sav"
}
```
### Configuration Options
  ### SessionName
  Name of the save game session.
  Can not exceed 20 characters.

  ### SaveGameInterval
  Time between automatic saves (in seconds).
  300 = 5 minutes.
> ⚠️ Only set this to true once when creating a new world!
  ### StartNewGame
  true → Forces creation of a new world.

  false → Prevents new save creation.
  ### LoadSavedGame
  true → Loads an existing save

  false → Skips loading saved data

  ### Creating a New Save (New World)
  1. Stop the server
  2. Set:
  ```
  "StartNewGame": "true",
  "LoadSavedGame": "false"
  ```
  4. Start the server and wait for it to finish loading
  5. Stop the server.
  6. Revert:
  ```
  "StartNewGame": "false",
  "LoadSavedGame": "true"
  ```
  7. Start the server and join it.
   ### Loading an Existing Save
  1. Stop the server.
  2. Ensure :

  ```
  "StartNewGame": "false",
  "LoadSavedGame": "true",
  "SaveGameName": "AutoSave0.sav"
  ```
  3. Upload your save game .sav and .met file to the server
     Location of saves : `/home/container/StarRupture/Saved/SaveGames`
  5. Rename these files to be AutoSave0.sav and AutoSave0.met
  6. Start the server and join it.
