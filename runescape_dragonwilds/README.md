# RuneScape: Dragonwilds Pterodactyl Egg

A Pterodactyl egg for the RuneScape: Dragonwilds dedicated server.

## Resources & Requirements
- **RAM**: 2GB base + 1GB per player. 
- **CPU**: Requires **AVX instruction support**.
- **Players**: The server can support up to 6 players.


## Mandatory configuration values
**Owner ID**: This is your RuneScape: Dragonwilds Player ID. It can be found in game at the bottom of the Settings Menu.

**Server Name**: The name of your server, no matter what world it may run.

**Default World Name**: Upon startup, your Dedicated Server will create a default world. This configuration value allows you to decide how you want it to be named.

**Admin password**: Anyone who knows this password can enter the Server Management tab in the Pause Menu > Settings menu. 

**World Password**: (Optional) The password required to join the world. Leave empty for public access.

**Extra Arguments**: If you need to pass additional startup flags (such as `-multihome`), you can add them here. 

Only use `-multihome` if you specifically need to bind to a specific IP and your networking environment supports it.

## Find your world
To find your dedicated server, go to the Public tab of the Worlds screen, then in the search tab, enter your exact World name, case sensitive.

## Network & Ports
By default, the server uses the following ports.

However, Pterodactyl ensures that the **Game** Port will automatically use the port assigned by your server's primary allocation.

| Port | Default | Protocol | Purpose |
|------|---------|----------|---------|
| Game | 7777 | UDP | Main game traffic |
| Query | 27015 | UDP | Steam Server Browser traffic |