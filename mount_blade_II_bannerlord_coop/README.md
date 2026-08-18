# Mount & Blade II: Bannerlord Coop

## [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3770450698) · [GitHub](https://github.com/Bannerlord-Coop-Team/BannerlordCoop) · [Setup video](https://www.youtube.com/watch?v=laZM967Eals)

Bannerlord Coop lets players share one persistent Bannerlord campaign, each running their own character, party and clan - no fixed player cap, limited by what the server can handle (the mod's Steam page cites servers running with 32+ players). It's a separate mod with its own dedicated server binary — not the same thing as vanilla multiplayer, and a different egg from `mount_blade_II_bannerlord`. Don't mix the two up.

## Installation/System Requirements

No official hardware spec from the mod authors, and no fixed player cap - the mod page says it's limited by what the server can handle, and cites servers running with over 32 players.

|  | Requirement |
|---------|---------|
| Processor | AMD64 only |
| Game Ownership | A Steam account that owns Mount & Blade II: Bannerlord is required to install |

## Server Ports

| Port | default |
|---------|---------|
| Game | 4200-4201 (UDP) |

> The port is fixed at UDP 4200, not configurable. Allocate `4200` as the primary port and add `4201`.

## Configuration

Panel variables get written into `server-config.json` at boot:

| Variable | Setting | Default |
|---|---|---|
| `SAVE_NAME` | `saveName` - world to host; created from `default_new_game.sav` if it doesn't exist | `saveauto1` |
| `AUTOSAVE_MINUTES` | `autosaveMinutes` - minutes between autosaves, `0` disables | `5` |
| `SERVER_PASSWORD` | `password` - join password, blank for none | *(blank)* |
| `STEAM_ENABLED` | `steam` - advertise on Steam vs. direct-connect only | `0` |
| `LOG_FILE` | `logFile` - also write `logs/coop-server-*.log` | `1` |

`server-config.json` doesn't exist until the server has run once, so panel settings only take effect from the second start onward. Edits are line-level and preserve the file's comments, the same way the mod's own tooling edits it.

`STEAM_ENABLED` defaults to off because a dedicated container normally has no Steam client running, and turning it on without one hangs the server at boot with no error - confirmed on this egg.

The diagnostic switches (`traceTick`, `tracePublish`, `traceBandits`) aren't exposed as variables - the config file itself says to only turn them on when capturing logs for a bug report. Edit the file directly if you need them.

Campaign difficulty and other gameplay options live in `mod-config.json`, one level up in `CoopData/`, shared with player-hosted sessions - edit that file directly, it's out of scope here.

## Notes

- `BannerlordCoopServer.exe` ships inside the Workshop item itself, under the base game's App ID (`261550`), rather than as a separate download. Anonymous Steam login can't fetch it - you need a Steam account that owns Bannerlord, set in the Steam User / Steam Password variables. The engine and a .NET runtime are bundled in the item too, so the free Dedicated Server tool (app `1863440`) isn't needed.
- Install uses [DepotDownloader](https://github.com/SteamRE/DepotDownloader), not SteamCMD's `workshop_download_item` - that command can't finish an item this size, it just times out with `ERROR! Timeout downloading item` (reproduced here across 24 consecutive resume attempts). DepotDownloader fetches the same content via `-pubfile` without that limit. Its linux-x64 build is self-contained, so it doesn't add a system .NET runtime to the image.
- If the Steam account has a mobile authenticator, install pauses waiting for you to confirm the login on your phone. `-remember-password` keeps the session so later reinstalls for the same account shouldn't prompt again. There's no way to pass a Steam Guard code non-interactively, which is why there's no auth-code variable here.
- The install counts against your disk quota - budget at least 10 GB. Files stage inside the server directory and the staging area is removed once install succeeds.
- The server writes `server-config.json` (JSONC - it has comments) on its first boot, under `CoopData/DedicatedServer/`. A password set before that first boot won't apply until the second one.
- Don't add a Configuration Files block for `server-config.json` in the panel - Pterodactyl's `json` parser creates an empty file before the server can write a real one, and mangles JSONC besides. `config.files` is left empty on purpose.
- The console shows `logs/coop-server-*.log`, not the process's real stdout. Stdout is unusable either way - a full-screen TUI on a real TTY, silently block-buffered through a pipe - so the egg parks it in `server-stdout.log` and tails the log file to the console instead, the same channel the mod's own tooling reads. Keep `logFile` on.
- Startup detection doesn't rely on anything the server prints. Its boot banner tells you to watch for `[DedicatedServer] SERVING`, but the binary never actually prints that line - matching on it just matched the banner's own instructions and reported "running" seconds after boot. Instead the egg polls `/proc/net/udp` for something bound to UDP 4200 and prints its own ready line once that happens. That's a proxy for readiness, not a confirmed "accepting players" signal - the socket could open before the campaign's fully loaded, and how big that gap is in practice hasn't been checked.
- Stop sends `SIGINT` (`^C`), not a `stop` command over stdin - redirecting stdout to a file breaks Wine's console input handling, so anything written to stdin never reaches the process. Use the panel's Stop button, not Kill. Whether `SIGINT` saves the campaign the way the mod's own docs say `stop` does hasn't been verified.
- `server-config.json` also covers autosave interval, log toggle, Steam toggle, and the diagnostic trace switches above. The server also takes a `--trace` flag for MonoMod and crash-dump diagnostics.
- Full session logs, more detailed than the console, live at `CoopData/DedicatedServer/logs/coop-server-*.log`.
- Support/setup help: the mod's [Discord](https://discord.com/invite/bannerlordcoop).
