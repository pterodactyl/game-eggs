# FotressCraft Evolved

FortressCraft Evolved is a unique blend of Voxel Landscapes, Tower Defense, Crafting, Logistics, Exploration, Combat and Assembly lines. Players begin by crash-landing on a strange alien world, left with only a small handful of starting machines.

[Steam Page](https://store.steampowered.com/app/254200/FortressCraft_Evolved/)

 ### Author & Contributers
| Name        | Github Profile  |
| ------------- |-------------|
|   brainshead   | https://github.com/brainshead |

## Server Ports

FotressCraft Evolved requires up to 2 ports

| Port    | default       |
|---------|---------------|
| Game    | 27000         |
| RCON    | 27001         | 

This can be changed to any port.

## Install Notes

| Requirements        | Memory| Storage | CPU   | Network|
|---------------------|-------|---------|-------|-----------|
| Minimal             | 8 GB   | 10GB   |Decent Quad-Core CPU (3.2GHz+)| 1-2Mbit/s per client is a rough guide|
| Recommended         | 8+ GB  | 20GB+ (SSD)  |   | |

## Settings

Most setting can be done by Panel Variable Settings.

World are saved at location : .config/unity3d/ProjectorGames/FortressCraft/Worlds

## Modding 

Copied from [Steam Source](https://steamcommunity.com/sharedfiles/filedetails/?id=788739671)

As always shutdown your server cleanly before youre toying around with the gamefiles.

The following Lines are copied (sort off) from the "FortressCraft Evolved Modding API.pdf" that can be found in the Installationdirectory fo FortressCraft in "...\SteamApps\common\FortressCraft\64\Default" (or ..\32\.. when your playing in 32-Bit).
(see Chapter 3 - 4 (specialy 4.1))

First get your Mod(s) to your Computer.
Subscribe to it/them in the Workshop and wait for the Download to finish.

You will find the mods in the "...\Steam\steamapps\workshop\content\254200\WorkshopID" directory.

Head to the Directroy tree where the world and such is stored.
(copy from the ModAPI.pdf)
go to

Linux: `/home/<user_name>/.config/unity3d/ProjectorGames/FortressCraft/`

Windows: `C:\Users\USERNAME\AppData\Local\ProjectorGames\FortressCraft\`

and create the new Directory named WorkshopMods.

Now copy the files 1:1 over there with your favorite methode (i recommend zipping it, transfer with FTP and unzip it again in this folder).

Now open the local version of your world in FCE and configure which mods you want to use. Get the "modsettings.xml" from your World safe directory and upload it in the World on the server (same spot as local).
Make sure you get the modsettings.crc, modsettings.bak and modsettings.bak.crc as well on the server. FCE tries to repair a changed File (which it uses the CRC's for). Alternativly, delete the just mentioned files on the server so you only have the modsettings.xml left.


Start your server, select the mods you activated on the world, join and have fun with your new Content.
