# Conan Exiles

## From their [Site](https://conanexiles.com/)

Conan Exiles is online multiplayer survival game set in the lands of Conan the Barbarian

## Minimum RAM warning

This server requires about 6GB to run properly.

## Server Ports

Ports required to run the server in a table format.

| Port    | default |
|---------|---------|
| Game    | 7777    |
| Game +1 | 7778    |
| UDP Server query| 27015  |
| RCON| 25575 |


## Mods

If you want mods download you have to allocated 1 extra port and manualy set Engine.ini.

See: [Here](https://www.conanexiles.com/dedicated-servers/)


## More information can be found [here](https://forums.funcom.com/t/conan-exiles-dedicated-server-app-latest-version-1-0-21/21699)

---

# Conan Exiles Enhanced (UE5)

Conan Exiles Enhanced is the May 5, 2026 Unreal Engine 5 rebuild of Conan Exiles, developed by Funcom with Inflexion Games. The egg `egg-conan-exiles-enhanced.json` in this folder runs the native Linux dedicated server binary that Funcom shipped with Enhanced — no Wine required, unlike the original egg above.

**Use the Enhanced egg** if you want the current UE5 build (the default Steam download for App ID `443030`).

**Use the original egg** if you specifically need the UE4 build, accessible via the `conan-exiles-legacy` Steam beta branch.

## Minimum RAM warning

UE5's Lumen and Nanite increase baseline memory usage 15–25% over UE4. Plan for at least 12 GB; 16 GB recommended if running mods.

## Server Ports

| Port            | default |
|-----------------|---------|
| Game            | 7777    |
| Game +1         | 7778    |
| UDP Server query| 27015   |
| RCON            | 25575   |

## Steam Workshop mods

Set the `MOD_LIST` egg variable to a comma-separated list of Steam Workshop IDs (e.g. `1369743238,2287499941`). The install script downloads each anonymously via SteamCMD, copies the `.pak` files into `ConanSandbox/Mods/` without renaming them (renaming breaks loading per Inflexion), and writes `modlist.txt`.

UE4 mods are silently ignored by Enhanced — only UE5-rebuilt mods will load. Most popular mods (Pippi, Fashionist, Hosav's UI) had Enhanced-compatible re-uploads available within hours of launch.

## Known issues since Enhanced launch

- **Legacy/UE4 mods cause OOM at boot** on builds before the May 6, 2026 hotfix. Fixed by Funcom.
- **Stale `bUseBuildIdOverride` lines** in migrated `Engine.ini` files from UE4 servers block client connections. Remove the `[OnlineSubsystem] bUseBuildIdOverride=` and `BuildIdOverride=` lines.
- **`-MULTIHOME=<ip>` server browser registration** required also passing `-MULTIHOMEHTTP=<ip>` on builds before the May 13, 2026 hotfix.
- **`game.db` → `game_0.db` rename** happens automatically on first boot if migrating a UE4 save. Update any backup scripts to use the new filename.
- **First boot is slow** — UE5 asset preload plus potential save migration. Don't kill the process during first start; it can corrupt the save.

## More information can be found [here](https://exiles-enhanced.inflexion.io/servers/)
