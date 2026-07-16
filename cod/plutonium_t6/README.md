# Plutonium T6

Plutonium is a community modification for Call of Duty: Black Ops II that provides dedicated server support, modding, and an enhanced multiplayer experience.

See https://plutonium.pw/docs/server/t6/setting-up-a-server/

## Server Ports

Plutonium T6 requires 1 port.

| Port | Default |
|------|---------|
| Game | 4976    |

This can be changed to any available port. The port must be allocated in the Pterodactyl panel and forwarded as **UDP**.

## Prerequisites

> [!IMPORTANT]
>
> Before installing, you need to obtain a legitimate copy of [Call of Duty: Black Ops II on Steam](https://store.steampowered.com/app/202970/Call_of_Duty_Black_Ops_II/).
>
> - Game files are downloaded via SteamCMD using the App ID for your selected mode:
>   - **Multiplayer (t6mp)**: `202990`
>   - **Zombies (t6zm)**: `212910`
> - Set **Game Mode** before installing — the installer downloads the matching component.
> - To switch modes later, change **Game Mode** / **Config File** and **reinstall** the server.
> - Your Steam account credentials must be set in the egg variables. Anonymous login is **not** supported.

> [!CAUTION]
> Only Steam is supported. The game must be owned on the Steam account used for installation.

### Server key

Create a server key at https://platform.plutonium.pw/serverkeys and set it in the **Server Key** egg variable.

## Install Notes

- Minimum **2 GB RAM** and **20 GB storage** recommended
- Game files are downloaded via SteamCMD using your Steam credentials (Windows depot for Wine)
- Plutonium client files are downloaded automatically during installation via [plutonium-updater](https://github.com/mxve/plutonium-updater.rs)
- The server runs under Wine using 1st-party `ghcr.io/ptero-eggs/yolks:wine_*` images
- Enable **Auto Update** to keep Plutonium client files current on each server start
- Reinstall the server to re-download or validate game files from Steam

### Game file layout

After installation, game files are located in `game/`:

```
game/
├── main/
│   ├── dedicated.cfg      (created by installer if missing)
│   └── dedicated_zm.cfg   (created by installer if missing)
├── zone/
└── ...
```

Plutonium client files are installed to `plutonium/`.

## Game Modes

| Mode   | GAME_MODE | CONFIG_FILE      |
|--------|-----------|------------------|
| Multiplayer | `t6mp` | `dedicated.cfg`  |
| Zombies     | `t6zm` | `dedicated_zm.cfg` |

When switching modes, update both the **Game Mode** and **Config File** variables to match.

## Settings

Server settings are configured in `game/main/dedicated.cfg` (Multiplayer) or `game/main/dedicated_zm.cfg` (Zombies).

The **Server Name** egg variable automatically updates `sv_hostname` in both config files on server start.

Common settings to edit in your config file:

- `rcon_password` — required for RCON and admin tools like IW4MAdmin
- `g_password` — optional server join password
- `sv_maxclients` — player limit (1–18)
- `sv_maprotation` — map and gametype rotation

See the [Plutonium T6 server documentation](https://plutonium.pw/docs/server/t6/setting-up-a-server/) for map rotation syntax and gametype configuration.

## Mods and Custom Maps

| Type         | Location                              |
|--------------|---------------------------------------|
| Mods         | `plutonium/storage/t6/mods/`          |
| MP maps      | `game/usermaps/`                      |
| ZM maps      | `game/usermaps/`                      |
| Logs         | `plutonium/storage/t6/logs/`          |
| Stats        | `plutonium/storage/t6/stats/`         |

Set the **Mod Directory** variable (e.g. `mods/my_mod`) to load a mod via `fs_game`.

## Troubleshooting

- **Steam install fails**: Verify the account owns Black Ops II and credentials are correct. If 2FA is enabled, set **Steam Auth** with your login code.
- **Server not in browser**: Confirm the UDP port is open and forwarded. It can take several minutes to appear in the server list after first start.
- **Wine display errors**: These are harmless; the dedicated server runs as a console application.
- **binkw32.dll errors**: Reinstall the server to re-download game files, or verify the `game/` directory contains a complete Steam install.
- **Startup detection**: If the panel stays on "Starting", the `done` detection string may need adjustment after checking console output for the heartbeat message.
