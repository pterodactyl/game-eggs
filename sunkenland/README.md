# Sunkenland


### Author & Contributers
| Name        | Github Profile  | Buy me a Coffee |
| ------------- |-------------|-------------|
|   Brainshead  | https://github.com/brainshead

## [Documentation](https://www.sunkenlandgame.com/post/dedicated-server-user-manual)
> [!NOTE]
> Latest document can also be found in root of your container when installing server.

Sunkenland is a Waterworld-themed survival game. Explore sunken cities, build your base, craft items, trade, and fight pirates as you struggle to survive in an aquatic post-apocalypse world plagued by hunger and violence.

## Install notes

To launch properly, the Sunkenland dedicated server software requires a map. However, the software does not generate the map itself.

This egg includes a default map created through the game. If the user desires a different map, they must create it through Sunkenland and import it to the server manually.

To locate your save files on Windows, go to the following directory:
`%USERPROFILE%\AppData\LocalLow\Vector3 Studio\Sunkenland\Worlds`

On the server, you can find the map here:
`/.wine/drive_c/users/container/AppData/LocalLow/Vector3 Studio/Sunkenland/Worlds`

On this location you also find AdminSteamIDs.txt and BanSteamIDs.txt

Put in Steam ID line by line of users to be admins or to be banned.


> [!CAUTION]
> **Remember** to change the `WORLD_GUID` variable, if you upload a new world to your server! Otherwise the server will crash upon launching it.

## Installation/System Requirements
<!--Make changes to reflect the server minimum/recommended hardware specs-->
|  | Bare Minimum | Recommended |
|---------|---------|---------|
| Game Ownership | *Server can start without it* | *Game is needed for creating custom maps* |
| RAM | 4 GB+ | 8 GB+ |
| Storage | 5 GB+ | 20 GB+ |

## Server Ports

Ports required to run the server in a table format.

| Port    | Default |
|---------|---------|
| Game Port | 25000 |


 ### Notes
 > [!NOTE]
> - There's no strict "server name" variable. It's tied to the World/Map Name. The install script is modified to rename the folder to whatever the users sets as `SERVER_NAME`.
> - When you want change the server name, a reinstall is required to let the script run the renaming of the world name. 
