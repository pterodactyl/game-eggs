# Plutonium T5

Plutonium is a community modification for Call of Duty: Black Ops that provides dedicated server support, modding, and an enhanced multiplayer experience.

See https://plutonium.pw/docs/server/t5/setting-up-a-server/

## Server Ports

Plutonium T5 requires 1 port.

| Port | Default |
|------|---------|
| Game | 28961   |

This can be changed to any available port. The port must be allocated in the Pterodactyl panel and forwarded as **UDP**.

## Prerequisites

> [!IMPORTANT]
>
> Before installing, you need to obtain a legitimate copy of [Call of Duty: Black Ops on Steam](https://store.steampowered.com/app/42700/Call_of_Duty_Black_Ops/).
>
> - Game files are downloaded via SteamCMD using the App ID for your selected mode:
>   - **Multiplayer (t5mp)**: `42710`
>   - **Zombies (t5sp)**: `42700`
> - Set **Game Mode** before installing — the installer downloads the matching component.
> - To switch modes later, change **Game Mode** / **Config File** and **reinstall** the server.
> - Your Steam account credentials must be set in the egg variables. Anonymous login is **not** supported.

> [!CAUTION]
> Only Steam is supported. The game must be owned on the Steam account used for installation.

### Server key

Create a server key at https://platform.plutonium.pw/serverkeys and set it in the **Server Key** egg variable.

## Install Notes

- Minimum **2 GB RAM** and **15 GB storage** recommended
- Game files are downloaded via SteamCMD using your Steam credentials (Windows depot for Wine)
- Plutonium client files are downloaded automatically during installation via [plutonium-updater](https://github.com/mxve/plutonium-updater.rs)
- The server runs under Wine using 1st-party `ghcr.io/ptero-eggs/yolks:wine_*` images
- Enable **Auto Update** to keep Plutonium client files current on each server start
- Reinstall the server to re-download or validate game files from Steam

### File layout

After installation:

```
game/                              # Steam game files
plutonium/                         # Plutonium client (from plutonium-updater)
plutonium/storage/t5/
├── dedicated.cfg                  # Multiplayer config (created if missing)
└── dedicated_sp.cfg               # Zombies config (created if missing)
```

## Game Modes

| Mode        | GAME_MODE | CONFIG_FILE      |
|-------------|-----------|------------------|
| Multiplayer | `t5mp`    | `dedicated.cfg`  |
| Zombies     | `t5sp`    | `dedicated_sp.cfg` |

When switching modes, update **Game Mode**, **Config File**, and **Max Clients** (Zombies typically uses 1–4 players), then reinstall if game files for the other mode are needed.

## Settings

Server settings are configured in `plutonium/storage/t5/dedicated.cfg` (Multiplayer) or `plutonium/storage/t5/dedicated_sp.cfg` (Zombies).

The **Server Name** egg variable automatically updates `sv_hostname` in both config files on server start.

Common settings to edit in your config file:

- `rcon_password` — required for RCON and admin tools like IW4MAdmin
- `g_password` — optional server join password (Multiplayer)
- `sv_maxclients` / **Max Clients** variable — player limit
- `sv_maprotation` — map and gametype rotation
- `playlist_enabled 0` — required for custom map rotations (Multiplayer)

See the [Plutonium T5 server documentation](https://plutonium.pw/docs/server/t5/setting-up-a-server/) and [T5ServerConfig](https://github.com/xerxes-at/T5ServerConfig) for advanced configuration examples.

## Mods and Custom Maps

| Type    | Location                         |
|---------|----------------------------------|
| Mods    | `plutonium/storage/t5/mods/`     |
| Scripts | `plutonium/storage/t5/scripts/`  |
| Logs    | written under `logs/` per config |

Set the **Mod Directory** variable (e.g. `mods/my_mod`) to load a mod via `fs_game`.

## Troubleshooting

- **Steam install fails**: Verify the account owns Black Ops and credentials are correct. If 2FA is enabled, set **Steam Auth** with your login code.
- **Server not in browser**: Confirm the UDP port is open and forwarded. It can take several minutes to appear in the server list after first start.
- **Wine display errors**: These are harmless; the dedicated server runs as a console application.
- **binkw32.dll errors**: Reinstall the server to re-download game files, or verify the `game/` directory contains a complete Steam install.
- **Map rotation ignored**: Set `playlist_enabled 0` in your Multiplayer config.
- **Startup detection**: If the panel stays on "Starting", check console output and adjust the `done` detection string if needed.
