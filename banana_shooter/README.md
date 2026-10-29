# Banana Shooter

## [Steam Page](https://store.steampowered.com/app/1949740/Banana_Shooter/)

Banana Shooter is a free-to-play, fast-paced multiplayer FPS. Play classic and chaotic game modes, workshop maps and a lot of bananas, online or with friends.

The egg installs the Banana Shooter Dedicated Server (Steam app `2406780`).

## Requirements

- The server files can't be downloaded anonymously. Use a Steam account that owns Banana Shooter (it is free to play).
- A Game Server Login Token is optional. It gives the server a fixed Steam ID. Create one for app `1949740` on the [Steam game server page](https://steamcommunity.com/dev/managegameservers).

## Configuration

Server settings live in `Servers/PterodactylServer/Config.json`. Workshop maps go in `Servers/PterodactylServer/SteamWorkshopConfig.json`, which the server writes on first start.

Console commands: `status`, `kick <id>`, `start`, `restart`, `quit`.

## Server Ports

Banana Shooter needs two ports. The Steam query port is always the game port + 1.

| Port              | Default |
|-------------------|---------|
| Game (UDP)        | 27015   |
| Steam query (UDP) | 27016   |
