# Stormworks: Build and Rescue

Join a world where you design, create and pilot your own air sea rescue service. Release your inner hero as you battle fierce storms out at sea to rescue those in need.
## Configuration Warning

As of the latest update, Stormworks server hosting now requires a Steam account that owns a copy of the game. You must provide valid Steam credentials (`STEAM_USER`, `STEAM_PASS`, and optionally `STEAM_AUTH` if your account uses two-factor authentication). Anonymous installation is no longer supported.

Due to the way the Stormworks configuration file is structured and how Pterodactyl handles configuration management, this egg can only partially preconfigure the `server_config.xml` file. During installation, the config file is generated and populated with values from several environment variables: `Server Name`, `Server Password`, `Server Admin`, and `Max Players`.

**Note:** These values are only applied once during the initial installation. Any changes made to these variables afterward, including changes to the port number, will not automatically update the configuration file. You must manually edit `/home/container/server_data/server_config.xml` for any changes made after installation to take effect.

Other configuration options not set during installation, such as `player_damage`, `npc_damage`, and various gameplay modifiers can still be freely edited in the `server_config.xml` file to customize the server to your liking.


## Server Ports

Stormworks requires 2 consecutive ports in order to run. The default ports are shown below. Using non-default ports is possible; however, they must remain consecutive.

The `server_config.xml` only sets the **first** port, the game automatically assumes the second port is the next consecutive number (`port + 1`).

| Port | default |
|------|---------|
| Game | 25564   |
| Game | 25565   |

## Final Note

It seems that the console will misreport TPS, always appearing at a steady 60-64. Ignore this reading. If you wish to check your server TPS, join your server and press the backquote/tilda key (`/~). 
