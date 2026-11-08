# RuneScape: Dragonwilds (RSDWServerAPI)

The [RuneScape: Dragonwilds](../) dedicated server with the [RSDWServerAPI](https://github.com/CobraTrinity/RSDWServerAPI) mod preloaded. Everything from the vanilla egg applies here too, including the Owner ID and the Beacon Port; see its [README](../README.md).

## Author & Contributors

| Name | Github Profile |
|------|----------------|
| CobraTrinity | https://github.com/CobraTrinity |

RSDWServerAPI was created by [dkoz](https://github.com/dkoz/RSDWServerAPI). This egg installs it from [CobraTrinity/RSDWServerAPI](https://github.com/CobraTrinity/RSDWServerAPI), which is kept up to date with the current game build.

## RSDWServerAPI

A Linux library (`librsdwapi.so`) that the startup command loads into the server with `LD_PRELOAD`. It adds:

- A REST API with bearer-token auth: server health, online players with stats, kick, ban, give items, broadcast.
- Source RCON (works with mcrcon, rcon-cli and panel RCON consoles).
- In-game chat commands for admins.
- A Discord relay for chat, joins, leaves and deaths.

It only loads into the game binary itself and does not modify any game files. To run the server without it, use the vanilla egg.

## Install and updates

The mod is downloaded during installation from a GitHub release of **RSDWServerAPI Repository**:

| RSDWServerAPI Release | Installs |
|---|---|
| `latest` (default) | The newest release |
| a tag, e.g. `0.1.6` | That release |
| `manual` | Nothing; keeps a `librsdwapi.so` you uploaded to the server root |

**To update the mod, reinstall the server** (Settings > Reinstall Server). Reinstalling keeps your world, `DedicatedServer.ini` and the mod's settings. If the download fails, the build already installed is kept.

A game update can break the mod until a matching RSDWServerAPI release is published. Reinstall once it is out.

## Configuration

Settings are passed as panel variables. The mod also writes them to `rsdwapi/settings.ini`, together with anything you leave empty:

- **API Bearer Token** and **RCON Password**: when left empty, a random value is generated on first start. Look it up in `rsdwapi/settings.ini`.
- **API IP Whitelist**: empty allows any client that has the token.

Logs are in `rsdwapi/logs/`.

## Server Ports

The game and beacon ports are the same as in the vanilla egg. The API needs its own allocation, and so does RCON when it is enabled. Set each variable to the port of its allocation.

| Port | Default | Protocol | Purpose |
|------|---------|----------|---------|
| Game | 7777 | UDP | Main game traffic |
| Beacon | 8888 | UDP | World settings beacon |
| API | 8080 | TCP | REST API |
| RCON | 27020 | TCP | Source RCON (optional, off by default) |
