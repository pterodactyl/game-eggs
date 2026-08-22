# Satisfactory

### Authors / Contributors

<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
    <tr>
        <td align="center">
            <a href="https://github.com/lilkingjr1">
                <img src="https://avatars.githubusercontent.com/u/4533989" width="50px;" alt=""/><br /><sub><b>Red-Thirten</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=lilkingjr1" title="Codes">💻</a>
        </td>
        <td align="center">
            <a href="https://github.com/iamkubi">
                <img src="https://avatars.githubusercontent.com/u/6176191" width="50px;" alt=""/><br /><sub><b>Kubi</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=iamkubi" title="Codes">💻</a>
            <a href="https://github.com/parkervcp/eggs/commits?author=iamkubi" title="Contributor">💡</a>
        </td>
        <td align="center">
            <a href="https://github.com/matthewpi">
                <img src="https://avatars.githubusercontent.com/u/26559841" width="50px;" alt=""/><br /><sub><b>matthewpi</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=matthewpi" title="Codes">💻</a>
            <a href="https://github.com/parkervcp/eggs/commits?author=matthewpi" title="Contributor">💡</a>
        </td>
        <td align="center">
            <a href="https://github.com/Software-Noob">
                <img src="https://avatars.githubusercontent.com/u/10975908" width="50px;" alt=""/><br /><sub><b>Software-Noob</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=Software-Noob" title="Codes">💻</a>
            <a href="https://github.com/parkervcp/eggs/commits?author=Software-Noob" title="Contributor">💡</a>
        </td>
        <td align="center">
            <a href="https://github.com/Zarklord">
                <img src="https://avatars.githubusercontent.com/u/1622280" width="50px;" alt=""/><br /><sub><b>Zarklord</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=Zarklord" title="Codes">💻</a>
            <a href="https://github.com/parkervcp/eggs/commits?author=Zarklord" title="Contributor">💡</a>
        </td>
        <td align="center">
            <a href="https://github.com/AlienXAXS">
                <img src="https://avatars.githubusercontent.com/u/1773445" width="50px;" alt=""/><br /><sub><b>AlienXAXS</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=AlienXAXS" title="Contributor">💡</a>
        </td>
        <td align="center">
            <a href="https://github.com/gOOvER">
                <img src="https://avatars.githubusercontent.com/u/116325?v=4" width="50px;" alt=""/><br /><sub><b>gOOvER</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=gOOvER" title="Codes">💻</a>
            <a href="https://github.com/parkervcp/eggs/commits?author=gOOvER" title="Contributor">💡</a>
        </td>
    </tr>
</table>
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

___

### Game Description

From Coffee Stain's [Website](https://www.satisfactorygame.com/):
> Satisfactory is a first-person open-world factory building game with a dash of exploration and combat. Play alone or with friends, explore an alien planet, create multi-story factories, and enter conveyor belt heaven!

___

### Egg Capabilities

- Automatic update check on startup via SteamCMD, with optional file validation for repair.
- Configurable max players, rotating autosave count, and client connection timeouts — values written to Game.ini / Engine.ini that the in-game Server Manager does **not** expose.
- Steam branch + branch password support for switching to experimental or private builds.
- Editable reliable messaging port to avoid collisions between Satisfactory servers running on the same host. The startup command wires the same value to both `-ReliablePort` (bind) and `-ExternalReliablePort` (advertised in the TLS handshake).

> [!NOTE]
> As of Satisfactory 1.0, most gameplay-affecting settings are managed via the **in-game Server Manager**, not the egg.
> See [Settings Worth Changing In-Game](#settings-worth-changing-in-game) for the ones that actually matter, and [Server Initialization](#server-initialization) for how to claim your server.

___

### Server Ports

Satisfactory 1.1 and 1.2 require **two** ports. The old beacon (15000) and query (15777) ports from pre-1.0 are no longer used — if a guide tells you to forward those, the guide is stale.

| Port                   | Default | Protocol  | Required | Notes                                                                                                                                              |
|------------------------|---------|-----------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Primary**            | 7777    | UDP & TCP | **Yes**  | Clients connect using this port. UDP carries game traffic; TCP carries the TLS-encrypted Server Manager / HTTPS API.                               |
| **Reliable Messaging** | 8888    | TCP       | **Yes**  | Reliable messaging port. Required for Satisfactory 1.1 and 1.2.                                                                                    |

> [!TIP]
> Your internal ports **must match** your external ports — Satisfactory does not support port translation (e.g., you can't forward external 7778 → internal 7777). If you run multiple Satisfactory servers on one host, give each its own unique pair and forward both pairs unchanged.

___

### Installation/System Requirements

Per the [official wiki](https://satisfactory.wiki.gg/wiki/Dedicated_servers#Requirements):

|  | Bare Minimum | Recommended |
|---------|---------|---------|
| Processor | x86-64 Intel (i5-3570 or better) or AMD (Ryzen 5 3600 or better). No 32-bit or ARM support. Single-thread rating 2000+ ([cpubenchmark.net](https://www.cpubenchmark.net/singleThread.html)). | Heavily favours single-core performance over multiple cores. **If running Wings under Proxmox VE, the VM CPU type must be `host` — `kvm64` will crash the server on world creation or save load.** |
| RAM | 8 GB | 16 GB (especially for 4+ players or large save files) |
| Storage | 8 GB (game files ~4 GB plus headroom for saves, logs, and crash dumps) | 12-15 GB or more if you autosave frequently or keep many rotating slots |
| Network | Broadband connection. Hosting from home requires port forwarding or a VPN. | 1-5 Mbit/s comfortable. Network *quality* setting in-game has more impact on perceived lag than raw bandwidth ([details below](#settings-worth-changing-in-game)). |
| Host OS | Debian, Ubuntu, or another current major Linux distro. | Latest stable kernel for your distro. |
| Game Ownership | Not required to start the server. | Required to claim and fully initialize the server (see [Server Initialization](#server-initialization)). |

___

### Server Initialization

> [!WARNING]
> Do not use "Join Game → Join game directly..." for the first connection. The server uses a self-signed TLS certificate that your client hasn't trusted yet; a direct join produces a **"Encryption token missing"** network error. Instead: open **Server Manager → Add Server**, enter your server's IP and port (default 7777), and you'll be prompted to trust the certificate and claim the server.

To **claim** the server, a client who owns the game must connect through Server Manager and set an administrator password. A new game can then be created in-game, or an existing save uploaded (see [Save Files](#save-files)).

Once claimed, the **in-game Server Manager** is the only place to configure the following settings — they are *not* set via the Egg:

**Dedicated Server tab:**
- Server Name
- Admin Password
- Player Password Protection
- Auto-Load Session Name
- Auto Pause (when no players are connected)
- Auto-Save on Player Disconnect

**Gameplay tab:**
- Server Restart Interval — *hour of day* for the daily auto-restart (despite the name; e.g. set to `06` to restart at 06:00 daily). Not a rolling interval.
- Autosave Interval (minutes)
- Send Gameplay Data (telemetry/crash reports to Coffee Stain)
- Network Quality

**Weather (1.2+):** Satisfactory 1.2 added weather controls to the Server Manager. The exact menu is still being iterated across 1.2.x hotfixes (one shipped a fix for *"incorrect menus showing up for weather in the Dedicated Server settings"*), so the canonical list is whatever your running server shows — review it once on first launch after updating.

> [!NOTE]
> A few settings are **not** in the in-game Server Manager UI and must be set elsewhere:
> - **Number of Rotating Autosaves** — set via this egg's `NUM_AUTOSAVES` variable (writes to `Engine.ini`).
> - **Max Players** — set via this egg's `MAX_PLAYERS` variable (writes to `Game.ini`). The Server Manager does not expose a player cap control.
> - **Disable Seasonal Events** — CLI launch arg only (`-DisableSeasonalEvents`). Not exposed by this egg; if you need it, append the flag to your server's Startup command.

> [!NOTE]
> **Tier 0 (Onboarding) and Tier 1 are skipped on dedicated servers** — players spawn straight into Tier 2 functionality. This is intentional per Coffee Stain's [1.0 known issues post](https://steamcommunity.com/app/526870/discussions/0/4755326933232852983/). If you want to play the Onboarding tutorial, play a local game until you exit Tier 1, then upload that save to the dedicated server.

> [!CAUTION]
> Some Server Manager settings (Autosave Interval, Server Restart Interval, Send Gameplay Data) have been reported to revert on server restart. This appears to be an upstream game issue ([game-eggs #443](https://github.com/pterodactyl/game-eggs/issues/443)), not an egg bug — the egg does not write to any in-game Server Manager state. After changing settings in-game, verify they persisted after your next restart.

___

### Game Modes (1.2+)

Satisfactory 1.2 added **Game Modes** — per-world toggles for Cost Multipliers (Space Elevator deliverables, recipe parts, power consumption), World Randomization (resource node placement, node purity), and a shareable World Seed. Dedicated servers fully support them.

Two things to know before using them:

- **Set only at new-world creation.** Game Modes are chosen when the *client* creates a new game via Server Manager → New Game. They cannot be enabled on an existing save and cannot be turned off once active — choices are permanent for that world.
- **Not exposed by this egg.** There are no `GAME_MODE_*` variables to set on the panel. If you want a non-default Game Mode, create the world on the server from the in-game UI.

___

### Settings Worth Changing In-Game

Once your server is initialized, open the in-game Server Manager and review these. They're the only Server Manager settings that meaningfully affect performance or play experience:

| Setting                  | Where     | Recommended                                                          | Why                                                                                                                                                                                                                                          |
|--------------------------|-----------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Network Quality**      | Gameplay tab | Ultra (on server **and** every client)                            | Defaults to Low, which is the single biggest cause of perceived "server lag" — belt stuttering, vehicle teleports, build snapping. Each player must set their *own* client to Ultra too; one player on Low still rubber-bands for themselves. |
| **Auto-Pause**           | Dedicated Server tab | Off if you want overnight production                       | Pauses production when no one is connected. Leave on for scheduled-session play; turn off if you want smelters running while everyone's offline.                                                                                             |
| **Autosave Interval**    | Gameplay tab | 5 min default; raise to 10–15 min for large saves                  | The server briefly pauses to write the save. Saves over ~150 MB cause noticeable hitches every interval. Don't go below the 5-minute default — frequent saves don't meaningfully reduce data loss and they amplify the hitch.                  |
| **Server Restart Interval** | Gameplay tab | Set to an off-hour (e.g. `06` for 06:00 daily) on long-running servers | Helps with long-uptime memory creep. Note: the field is *hour of day*, not a rolling interval, despite the name.                                                                                                                          |
| **Number of Rotating Autosaves** | This egg's `NUM_AUTOSAVES` variable | 3–5                                  | How many autosave slots to keep before the oldest is overwritten. *Not in the in-game UI* — change it via the panel.                                                                                                                          |

The other Server Manager settings (admin password, player password, server name, auto-save-on-disconnect, etc.) are about access control and identity, not performance. Set them once on first claim and move on.

___

### Save Files

> [!CAUTION]
> Stopping the server does **not** trigger a fresh save of your game world. Per the [official wiki](https://satisfactory.wiki.gg/wiki/Dedicated_servers), the `SIGINT` shutdown the egg uses lets the server flush its config and log files but does not force a new world save — only the most recent autosave is preserved. If players have built things since the last autosave, ensure the game has saved (via the in-game Server Manager → Save) before stopping.

The world save files for this server are at:

```md
/home/container/.config/Epic/FactoryGame/Saved/SaveGames/server
```

The Server Manager's "Manage Saves" tab (admins only) is the easiest way to download, upload, and load saves — an existing single-player save can be uploaded there and loaded just like a session created on the server.

Blueprints created in-game live alongside saves:

```md
/home/container/.config/Epic/FactoryGame/Saved/SaveGames/blueprints
```

If you forget your administrator password or want to reset the server to an unclaimed state, delete the ServerSettings file (replace `<your_server_port>` with whatever you set `SERVER_PORT` to — `7777` by default):

```md
/home/container/.config/Epic/FactoryGame/Saved/SaveGames/ServerSettings.<your_server_port>.sav
```

Your world saves are not affected by deleting this file.

___

### Updating to 1.2

A 1.1 save will open fine in 1.2, but **a 1.2 save will not open in 1.1** — once your server runs a save on 1.2, you cannot roll the server back to 1.1 with that same save. Back up the `SaveGames/server/` directory above before flipping `AUTO_UPDATE` on for the first time after a major version bump.

Vehicle path automation was rebuilt from the ground up in 1.2. Per Coffee Stain, routes recorded under 1.1 *should* continue to work as-is, but multiple reports from the experimental cycle indicate complex multi-stop routes sometimes need to be re-recorded under the new system. If your players rely on truck/tractor automation, verify routes on a copy of the save first.

___

### Console Commands

The "Console" tab in the in-game Server Manager is the only way to execute commands. Entering commands via the Panel do nothing.

[List of known commands can be found via the Wiki.](https://satisfactory.wiki.gg/wiki/Dedicated_servers#Console_commands)

___

### Known Errors/Warnings

The following errors or warnings you see in the console can safely be ignored:

```log
steamclient.so: cannot open shared object file: No such file or directory
[S_API] SteamAPI_Init(): Loaded '/home/container/.steam/sdk64/steamclient.so' OK.  (First tried local 'steamclient.so')
LogSteamShared: Warning: Steam Dedicated Server API failed to initialize.
```

↑ The local file of 'steamclient.so' was attempted to be loaded, but could not because it is not present, causing the warning message. However, the backup `/home/container/.steam/sdk64/steamclient.so` is loaded successfully (this is the correct behavior according to the [Wiki](https://satisfactory.wiki.gg/wiki/Dedicated_servers#SteamAPI_Init():_Sys_LoadModule_failed_to_load:_/path/to/.steam/sdk64/steamclient.so)).

```log
Warning: failed to init SDL thread priority manager: SDL not found
```

↑ This is a common error with Steam related software on Linux, but can safely be ignored.

```log
Exiting abnormally (error code: 130)
```

↑ This misleading message occurs when stopping the server. It is printed by the Unreal Engine because it doesn't know why it was interrupted (even though it was expected by us). This can be safely ignored if you notice normal engine shutdown logs above.

```log
...Error: Couldn't find file for package...
```

```log
...Error: Navmesh bounds are too large!...
```

```log
...Warning: NiagaraSystem...
```

```log
LogStreaming: Warning: Failed to read file '../../../FactoryGame/Saved/SaveGames/GameAnalytics.sav' error.
```

↑ These seem to be common error messages with the current experimental version of the game.
