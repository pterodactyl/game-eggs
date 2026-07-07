# Romestead
 
## From their [Site](https://romestead.com/)
 
Rome has fallen! Rebuild civilization in this action-adventure survival game for 1-8 players. Fight, build towns and earn favor with the Roman gods! ...or just farm your crops.
 
> [!IMPORTANT]
> A restart of the server is recommended after installation, as it does not release the used memory in the world generation automatically. This is not required, but will reduce memory usage significantly.
 
## Minimum RAM warning
 
* This server requires about 6-8GB to install and generate the world
* This server requires about 2-3GB to run after initial installation/generation of the world
## Server Ports
 
| Port | Default |
|------|---------|
| Game | 8050    |
 
## Additional information
 
* `sed -i -E 's/^( )+/\1/' config.json;` at the start of the startup command normalises the indent in config.json so the game server doesn't crash
* Additional logs are shown in the console and can be found in `/home/container/logs/latest.log`
