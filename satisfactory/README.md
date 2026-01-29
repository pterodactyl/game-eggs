# Satisfactory

> [!IMPORTANT]
> ***Updating for v1.0?***
> - Ensure any existing servers have the updated Startup Command applied!
> - TCP is now required! (See [Server Ports](#server-ports) for details)
> - While not required, it's recommended existing servers delete the `LinuxServer` directory under `~/FactoryGame/Saved/Config/` to remove depreciated settings, and reconfigure the settings via the in-game Server Manager.
___

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

- Configurable to automatically check for server updates on start via SteamCMD. Forcing validation is also configurable.
- Configurable number of rotating autosaves.
- [*Experimental*] Configurable maximum number of players.
- [*Advanced*] Configurable networking and server branch settings.

> [!NOTE]
> As of Satisfactory v1.0, most server settings have moved from being configured in the Egg to being configured via the in-game Server Manager.\
> Please see [Server Initialization](#server-initialization) for what settings can be configured in-game.

___

### Server Ports

| Port          | Default | Protocol  | Required | Notes                                                                                                                                                  |
|---------------|---------|-----------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Primary**   | 7777    | UDP & TCP | **Yes** | Clients connect using this port. UDP is un-encrypted game traffic. TCP is also required for the in-game Server Manager & API, and it is TLS encrypted. |
| **Reliable Messaging** | 8888    | TCP       | **Yes** | Reliable messaging port. Required for Satisfactory version 1.1 and above.                                                                    |

> [!TIP]
> \*Your internal ports **must match** your external ports on your network (ie. you can't have an external port of 7778 forwarded to your 7777 internal port; they must match).

___

### Installation/System Requirements

|  | Bare Minimum | Recommended |
|---------|---------|---------|
| Processor | Recent x86/64 (AMD/Intel) processor that supports modern instructions (ie. AVX, AES, etc.). No 32 bit or ARM support. | Favours higher single-core performance over multiple cores. If you are running Wings via Proxmox, you may need to set the VM's CPU Type to "host" to avoid session save/load crashes. |
| RAM | 4608 MiB | 8192-12288 MiB (especially for 4 players or large save files) |
| Storage | 5120 MiB | 7168-10240 MiB (or more, depending on save size or frequency) |
| Network | 1 Mbit/s | 1-5 Mbit/s ([may require server *and* client config tweaks](https://satisfactory.wiki.gg/wiki/Multiplayer#Temporary_lag_solution)) |
| Host OS | Most stable Linux OS branches should work | Using the latest kernel version for your installed OS can prevent some edge-case installation/boot issues. |
| Game Ownership | Not required to start. | Required to fully "initialize" (see [Server Initialization](#server-initialization) below) |

___

### Server Initialization

> [!WARNING]
> The server cannot be joined for the first time via "Join Game -> Join game directly..." on the main menu due to the TLS certificate not being trusted yet. Instead, join via "Server Manager -> Add Server" and you will be prompted to trust the certificate and initialize the server.

For a server to be fully "initialized", a client who owns the game must log into the server to "claim" it and create an administrator password. Then, a new session can be created via the "Create Game" tab in-game, or an existing save file can be uploaded (see [Save Files](#save-files) below).

Misc. settings listed below can be configured by an admin client via the Server Manager's "Server Settings" tab, and are currently **not** set via the Egg:

- Server Name
- Admin Password
- Player Password Protection
- Auto-Load Session Name
- Auto Pause (when no players are online)
- Auto-Save on Player Disconnect
- Disable Seasonal Events
- Autosave Interval
- Server Restart Interval
- Send Gameplay Data (Crash Reports)
- Network Quality

> [!NOTE]
> Currently, Tier 0 (Onboarding) is not possible to play on a dedicated server and it will be automatically unlocked, even if you upload a save in Tier 0. If you would like to play the beginning of the game with Onboarding, it is recommended you play local multiplayer first, and then upload your save after completing Tier 0.

___

### Save Files

> [!CAUTION]
> Stopping the server **does not** currently save your game! Ensure it is saved before stopping the server!

Save files are located in the following directory, but can be more easily downloaded to your local computer in-game via the Server Manager under the "Manage Saves" tab (admins only).

```md
/home/container/.config/Epic/FactoryGame/Saved/SaveGames/server
```

An existing save file (including single-player saves) can be uploaded to the server via the Server Manager as well and loaded under the same tab.

If you have forgotten your administrator password or would generally like to reset your server as if it were new, you can delete the following file:

```md
/home/container/.config/Epic/FactoryGame/Saved/SaveGames/ServerSettings.<your_server_query_port>.sav
```

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
