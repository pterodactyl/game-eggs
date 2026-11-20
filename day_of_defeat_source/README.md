# Day of Defeat: Source

Day of Defeat: Source is Valve's team-based World War II multiplayer shooter built on the Source engine.

## Installation

The native Linux dedicated server is distributed as Steam App ID `232290` and installs with anonymous SteamCMD. The egg uses the stock Ptero-Eggs Debian installer and Source runtime images.

## Configuration

The main server configuration is `dod/cfg/server.cfg`. The egg creates this file on first install and lets Pterodactyl manage the server name, join password, and RCON password. Existing configuration is preserved on reinstall.

The default startup map is `dod_anzio`. SourceTV is disabled by the startup command, so it does not require a second allocation.

## Server Ports

Day of Defeat: Source needs one Pterodactyl allocation. The primary listen port carries game traffic and A2S queries over UDP; Source RCON uses TCP on the same port number.

| Purpose | Default | Protocol | Allocation |
|---------|---------|----------|------------|
| Game / A2S query | 27015 | UDP | Primary |
| RCON | 27015 | TCP | Primary |

No separate query-port variable or allocation is required.

## Links

- [Steam store page](https://store.steampowered.com/app/300/Day_of_Defeat_Source/)
- [Valve dedicated server list](https://developer.valvesoftware.com/wiki/Dedicated_Servers_List)
- [Valve Source server query protocol](https://developer.valvesoftware.com/wiki/Source_Server_Queries)
