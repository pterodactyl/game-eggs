# RuneScape: Dragonwilds Pterodactyl Egg

A Pterodactyl egg for the RuneScape: Dragonwilds dedicated server.

## Resources
RAM required is 2Gb + 1Gb per player. 

The server can support up to 6 players.


## Mandatory configuration values
**Owner ID**: This is your RuneScape: Dragonwilds Player ID. It can be found in game at the bottom of the Settings Menu.

**Server Name**: The name of your server, no matter what world it may run.

**Default World Name**: Upon startup, your Dedicated Server will create a default world. This configuration value allows you to decide how you want it to be named.

**Admin password**: Anyone who knows this password can enter the Server Management tab in the Pause Menu > Settings menu. 

**World Password**: (Optional) The password required to join the world. Leave empty for public access.

## Find your world
To find your dedicated server, go to the Public tab of the Worlds screen, then in the search tab, enter your exact World name, case sensitive.

## Network & Ports
By default, the server uses the following ports. If you are using Pterodactyl, ensure you have allocated these to your server instance.
| Port | Default | Protocol | Purpose |
|------|---------|----------|---------|
| Game | 7777 | UDP | Main game traffic |
| Query | 27015 | UDP | Steam Server Browser traffic |

**Note on Allocations:**
The **Game** Port will automatically use the port assigned to your server's primary allocation if you configure it in the Pterodactyl panel. If you do not, it will default to 7777.