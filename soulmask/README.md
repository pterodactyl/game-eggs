# Soulmask

### Game Description

 Escaping a deadly sacrificial ritual, you find an ancient mystical mask on your journey. This mask holds potent knowledge, changing the world you knew. Face the harsh challenges of nature, survive, rally followers, and build your own tribe. Explore and unveil the truths behind the enigmatic mask. 

### Useful links

Steam: https://store.steampowered.com/app/2646460/Soulmask/

### Author & Contributers
| Name        | Github Profile  | Buy me a Coffee |
| ------------- |-------------|-------------|
|   QuintenQVD0   | https://github.com/QuintenQVD0 | [![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/J3J2HGECS) |


### Server Ports

Soulmask requires up to 4 ports. You can choose every port you want.

| Port     | default       |
|--------- |---------------|
| Game     |     7777      |
| Query    |     27015     |
| EchoPort |     18888     |
|ClusterPort|   2000       |

## Important Server Files Locations
|File          | Path      |
|--------------|-----------|
|World Save    | WS\Saved\Worlds\Dedicated\(selectedmap)\world.db|
|Server Config | WS\Saved\Config\LinuxServer\ |
|Gameplay Settings| WS\Saved\Gameplaysettings\GameXishu.json|
|Server Logs | WS\Saved\Logs|
|Backups | WS\Saved\Worlds\Dedicated\(selectedmap\backup|

## Special Note

- A single game process requires at least 16GB of memory and 2-4 CPU cores.
- Bandwidth requirements: Each game server's inbound/outbound bandwidth is about 100kbps/player.
- The game package size is about 1-2GB, requiring about 20GB of free disk space for operation.
- Cluster Port : The TCP broadcast port that client server will connect to. The presence of this parameter designates the server as a main server for a cluster. This port should not be open to the public, but needs to be accessible to servers within the cluster. Any server with access to the port can register as a client server.

## Mods 
- When you want to join your modded server, activate the mods ingame in the Main menu before joining your server.
- When adding mods , be sure there are no spaces as example: MODID1,MODID2,MODID3

## Extra Info
Extra info can be found on [saraserenity.net](https://saraserenity.net/soulmask/server_cluster_guide.php)
