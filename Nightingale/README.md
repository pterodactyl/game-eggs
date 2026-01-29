# Nightingale

Nightingale is an open world survival crafting game, where you’ll adventure across the mysterious and dangerous Fae Realms. As a daring Realmwalker, you’ll defeat monstrous enemies, survive hostile environments, and build elaborate estates in a visually stunning Gaslamp Fantasy world

 ### Author & Contributers
| Name        | Github Profile  |
| ------------- |-------------|
|   brainshead   | https://github.com/brainshead |

## Server Ports

Nightingale requires up to 1 ports

| Port    | default       |
|---------|---------------|
| Game    | 7777          |

This can be changed to any port.

## Install Notes

| Requirements        | Memory| Storage | 
|---------------------|-------|---------|
| Minimal             | 4GB   | 15 GB   |
| Recommended         | 6-8+ GB| 40GB+  |


## Settings

Most setting can be done by Panel Variable Settings.

Location of server Files : NWX/Config/ServerSettings.ini

## Persistence (Saved Data)

Realm data is be stored in: NWX/Saved/Offline/DedicatedServer/Deploy

Character data is stored in: NWX/Saved/Offline/<PlatformID>/Profiles where

PlatformID is the Steam or Epic ID of each connecting user.

Backups

Copying the following directories to a backup location is sufficient to capture the state of a Nightingale dedicated server:

● NWX/Saved/Offline

● NWX/Saved/Config

● NWX/Config

The first time the dedicated server is launched on a particular weekday, it will copy the Offline

directory into the OfflineBackup directory.

## Resetting Server Persistence

To reset the server to an empty state, remove the following directories:

● NWX/Saved/Offline

● NWX/Saved/Config

## Enabling Cheats Mode on Clients
To enable debug/cheats, the client must be launched with the -EnableCheats commandline argument.

Players will need to authenticate with the admin password to use the cheats in-game
> [!IMPORTANT]
> Also Server need to have Cheats enabled

## Further Adjustements available

Status Endpoint (not built in egg )

To enable scraping server status from an http endpoint, add -statusPort=<port> to the commandline, where <port> is a port in the range 1024-65535.

Status can be scraped from  the /status endpoint periodically.

By default this will bind to localhost only. To bind to a specific IP, 

add -ini:Engine:[HTTPServer.Listeners]:+ListenerOverrides=(Port=<port>,BindAddress=<IP>) to the commandline as well, or use 0.0.0.0 to bind to all available interfaces.

If the server is still loading and not yet ready for players, it will return a 503 Server Unavailable http status and a JSON object

Once the server is ready for players, it will return a 200 OK status and a JSON object

## Mod Support
No Official Support!

Not tested

