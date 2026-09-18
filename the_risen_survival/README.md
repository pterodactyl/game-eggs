# The Risen Survival

The Risen Survival is an open-world multiplayer survival game. This egg manages the dedicated Linux server build with SteamCMD auto-installation, automatic updates, scheduled maintenance, and Unity Netick runtime support.

---

## Server Ports

| Port | Protocol | Description | Default |
| :--- | :--- | :--- | :--- |
| **Game Port** | UDP | Primary game traffic port (`{{SERVER_PORT}}`) | `27015` |
| **Query Port** | UDP | Steam server browser query port (`{{QUERY_PORT}}`) | `27016` |
| **RCON Port** | TCP | Remote Console management (Optional) | `27017` |

> [!IMPORTANT]
> When assigning allocations in your Pterodactyl panel, allocate both **27015/UDP** (Primary) and **27016/UDP** (Additional Allocation). Set the `Query Port` variable in the Startup tab to match your assigned query port.

---

## Hardware & System Requirements

| Resource | Minimum Recommended | Recommended |
| :--- | :--- | :--- |
| **CPU** | 2 Physical Cores (3.0 GHz+) | 4 Cores |
| **RAM** | 4 GB | 6 GB - 8 GB |
| **Storage** | ~10 GB | 15 GB (SSD) |
| **Operating System** | Debian / Ubuntu (x86_64) | Debian / Ubuntu (x86_64) |

---

## Environment Variables

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `SRCDS_APPID` | `5035520` | Steam Dedicated Server AppID for The Risen Survival |
| `SERVER_NAME` | `The Risen Survival Dedicated Server` | Name of the server visible in the Steam server list |
| `SERVER_PASSWORD` | *(Empty)* | Password required to connect (leave empty for public) |
| `SERVER_PORT` | `27015` | Dedicated server game port |
| `QUERY_PORT` | `27016` | Steam server query port |
| `MAX_PLAYERS` | `42` | Maximum concurrent player slots |
| `MAP_SCENE` | `Hollow Pines` | Starting game map scene to load |
| `GAME_MODE` | `0` | Game mode preset: `0`=Survival, `1`=Hardcore, `2`=Casual, `3`=PurgeMadness |
| `PVP_ENABLED` | `true` | Enables or disables PVP damage (`true` / `false`) |
| `SERVER_REGION` | `EU` | Server region tag for browser filtering (`EU`, `US-East`, `US-West`, `ASIA`) |
| `RESTART_INTERVAL` | `24` | Hours between automatic scheduled restarts (`0` = disabled) |
| `AUTO_UPDATE` | `1` | Checks and updates server files via SteamCMD on startup (`1`=yes, `0`=no) |
| `VALIDATE` | `0` | Validates game server files on boot (`1`=yes, `0`=no) |
| `STEAM_USER` | *(Empty)* | Steam username (leave empty for anonymous login) |
| `STEAM_PASS` | *(Empty)* | Steam account password if using an authenticated account |
| `SRCDS_BETAID` | *(Empty)* | Beta branch name (if testing experimental versions) |

---

## Configuration Files

The server stores its configuration and moderation data in the server root:

* `server_config.json`: Gameplay and server engine settings (auto-save interval, GC interval, tick rate).
* `ranks.json`: Custom player ranks, permission levels, chat prefixes, and colors.
* `admins.json`: Assigned player ranks by SteamID64.
* `whitelist.json`: Whitelisted SteamID64s (applied when `WhitelistEnabled` is `true`).
* `bans.json`: Active temporary and permanent player bans.
* `mutes.json`: Active text and voice chat mutes.
* `admin_log.txt`: Audit log of all administrative actions.
* `steam_appid.txt`: Steam AppID authentication file.

---

## Server & Console Commands

> [!NOTE]
> * **From the Pterodactyl Console**: Commands can be typed **with or without** the leading slash `/`. The console automatically executes with full Owner permissions.
> * **In-Game Chat**: Commands must begin with `/` and require the appropriate permission rank in `admins.json`.

### 1. General & Player Commands (Available to All)

| Command | Usage | Description |
| :--- | :--- | :--- |
| `help` | `/help [command]` | Lists available commands or displays syntax for a specific command (Alias: `/commands`). |
| `playerlist` | `/playerlist` | Lists all online players and SteamIDs (Aliases: `/players`, `/who`). |
| `kill` | `/kill` | Suicide command if your character is stuck (Alias: `/suicide`). |
| `ping` | `/ping` | Displays your network latency (ping) in milliseconds. |
| `roll` | `/roll [max]` | Rolls a random number between 1 and `max` (default 100). |

---

### 2. Moderator Commands (`Moderator` Rank+)

| Command | Usage | Description |
| :--- | :--- | :--- |
| `status` | `/status` | Shows tick FPS, players online, zombie count, memory usage, and uptime (Alias: `/info`). |
| `say` | `/say <message>` | Broadcasts an official server-wide message in chat. |
| `kick` | `/kick <player> [reason]` | Kicks a player from the server. |
| `kill` | `/kill <player>` | Force-kills a targeted player character. |
| `mute` | `/mute <player> <duration>` | Mutes player from text chat (e.g. `10m`, `1h`, `1d`). |
| `unmute` | `/unmute <player>` | Unmutes player from text chat. |
| `voicemute` | `/voicemute <player> <duration>` | Mutes player from proximity voice chat (e.g. `10m`, `1h`). |
| `voiceunmute` | `/voiceunmute <player>` | Unmutes player from proximity voice chat. |

---

### 3. Administrator Commands (`Admin` Rank+)

| Command | Usage | Description |
| :--- | :--- | :--- |
| `ban` | `/ban <player\|steamid> <duration/0> [reason]` | Bans a player (duration in minutes or `0` for permanent). |
| `unban` | `/unban <steamid>` | Removes a ban for a SteamID. |
| `whitelist` | `/whitelist <add\|remove\|list> [steamid]` | Adds, removes, or lists players on the server whitelist. |
| `tp` | `/tp <player> [targetPlayer]` | Teleports you to a player, or teleports a player to another (Alias: `/teleport`). |
| `give` | `/give <player> <item_name> [amount]` | Spawns items directly into a player's inventory. |
| `heal` | `/heal [player]` | Restores full health, hunger, thirst, and vitals. |
| `godmode` | `/godmode [player] [on\|off]` | Toggles invulnerability / god mode (Alias: `/god`). |
| `freebuild` | `/freebuild` | Toggles building parts without consuming crafting materials (Alias: `/freebuilding`). |
| `destroy` | `/destroy` | Demolishes the player-built structure you are aiming at (Alias: `/demolish`). |
| `airdrop` | `/airdrop [here \| at X Z]` | Calls an emergency supply drop crate (Alias: `/supplydrop`). |
| `purge` | `/purge <now \| warn \| heat N \| end \| state>` | Triggers, configures, or ends the Purge Night zombie horde event. |
| `save` | `/save` | Triggers an immediate world save and backup snapshot to disk. |
| `cleanram` | `/cleanram` | Triggers on-demand garbage collection and trims memory (Aliases: `/trimram`, `/trimmem`). |
| `reloadranks` | `/reloadranks` | Reloads `ranks.json` and `admins.json` live without restarting (Alias: `/ranksreload`). |

---

### 4. Owner & Console Commands (`Owner` Rank or Console Operator)

| Command | Usage | Description |
| :--- | :--- | :--- |
| `restart` | `/restart [minutes \| now \| cancel]` | Schedules a countdown restart, restarts instantly, or cancels pending restarts. |
| `stop` | `/stop` | Gracefully saves world state and shuts down the server (Aliases: `/quit`, `/shutdown`, `/exit`). |
| `wipe` | `/wipe confirm` | Archives current world save to a backup folder and wipes all structures/sleepers for a fresh map wipe. |
| `promote` | `/promote <player\|steamid> <rank>` | Promotes a player to a rank defined in `ranks.json` (e.g. `Owner`, `Admin`, `Moderator`, `VIP`). |
| `demote` | `/demote <player\|steamid>` | Strips all assigned administrative ranks from a player. |
| `time` | `/time <hour \| freeze \| unfreeze \| speed <day> <night>>` | Sets the in-game clock, freezes/unfreezes time, or configures day/night progression speed. |
| `weather` | `/weather <name \| list>` | Changes active weather preset or lists all available weather presets. |
