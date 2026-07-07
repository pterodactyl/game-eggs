# Carrier Command 2

### Steam Description
Carrier Command 2 is a real-time strategy game in which you command an
aircraft carrier and its squadrons of land, sea, and air units across an
archipelago. Conquer islands, manage logistics, and battle enemy carriers
in solo or multiplayer.

### Authors / Contributors
<table>
    <tr>
        <td align="center">
            <a href="https://github.com/norto22">
                <img src="https://avatars.githubusercontent.com/u/88603725" width="50px;" alt=""/><br /><sub><b>norto22</b></sub>
            </a>
            <br />
            <a href="https://github.com/pterodactyl/game-eggs/issues/299" title="Egg Author">💻</a>
        </td>
        <td align="center">
            <a href="https://github.com/Medx-a99">
                <img src="https://avatars.githubusercontent.com/u/13230838" width="50px;" alt=""/><br /><sub><b>Medx-a99</b></sub>
            </a>
            <br />
            <a href="https://github.com/pterodactyl/game-eggs/issues/299" title="Egg Request">🤔</a>
        </td>
        <td align="center">
            <a href="https://github.com/ActiumDev">
                <img src="https://avatars.githubusercontent.com/u/178988117" width="50px;" alt=""/><br /><sub><b>ActiumDev</b></sub>
            </a>
            <br />
            <a href="https://github.com/ActiumDev/cc2-server-wine" title="Linux/Wine Research">🔬</a>
        </td>
    </tr>
</table>

## Steam Ownership Required
The Carrier Command 2 dedicated server is not available for anonymous SteamCMD
download. You must provide Steam credentials (`STEAM_USER` / `STEAM_PASS`) for
a Steam account that owns the game.

**Steam Guard 2FA:** if your account has Steam Guard enabled, you must enter
the current code in `STEAM_AUTH` when first creating the server. Steam Guard
codes rotate every 30 seconds; grab a fresh one immediately before clicking
install or the SteamCMD login will time out.

**Throwaway account recommended:** because the password field is stored in
panel variables (encrypted at rest but visible to anyone with edit access on
the server), consider using a dedicated alt Steam account that owns only
CC2, rather than your main account.

## Recommended Server Settings

### RAM
Minimum 4 GB. CC2's dedicated server has been observed using 2-3 GB at idle
on small worlds; larger worlds and active battles use more.

### CPU
Minimum 2 vCPU cores. CC2's server is sensitive to thread synchronization
under Wine; VM-virtualized cores may underperform compared to bare metal.

### Storage
Minimum 5 GB. The game install is ~1.3 GB, plus SteamCMD, Wine prefix, and
the Steamworks SDK redistributable files.

## Server Ports
Carrier Command 2 requires **4 consecutive UDP ports** starting at the
primary allocation. The server listens on the base port and the next three
for Steam communications.

| Port | Purpose |
|------|---------|
| `<base>` (default 25565) | Main game traffic |
| `<base+1>` | Steam extended server info |
| `<base+2>` | Reserved |
| `<base+3>` | Steam server query |

Allocate all four consecutive UDP ports to the server in Pterodactyl
before creating it. The server will fail to register with Steam Master
Server if any of the four are not open.

## Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SERVER_NAME` | Display name in the server browser | A Pterodactyl Hosted Server |
| `SERVER_PASSWORD` | Optional join password | (none) |
| `MAX_PLAYERS` | Max simultaneous players (1-16) | 4 |
| `SAVE_NAME` | Folder under `saved_games/` to load on start | (none) |
| `ISLAND_COUNT` | Number of islands (4-32) | 16 |
| `TEAM_COUNT_AI` | AI-controlled enemy teams (0-4) | 1 |
| `TEAM_COUNT_HUMAN` | Human-controlled teams (1-4) | 1 |
| `CARRIER_COUNT_PER_TEAM` | Carriers per team (1-4) | 1 |
| `ISLAND_COUNT_PER_TEAM` | Starting islands per team (1-8) | 1 |
| `BASE_DIFFICULTY` | Base capture difficulty (0=easy, 1=normal, 2=hard) | 1 |
| `LOADOUT_TYPE` | Starting carrier loadout (0=standard, 1=light, 2=heavy) | 0 |
| `BLUEPRINTS` | Blueprint unlocks (0=research required, 1=all unlocked) | 0 |
| `STEAM_USER` | Steam username (account owning CC2) | |
| `STEAM_PASS` | Steam password | |
| `STEAM_AUTH` | Steam Guard code (first install only) | |
| `SRCDS_APPID` | Steam App ID (read-only) | 1489630 |
| `AUTO_UPDATE` | Re-run SteamCMD on every server start | 0 |

## Known Limitations

### The CC2 dedicated server can LOAD save games but cannot WRITE them
This is a **CC2 server bug**, not an egg bug. All in-game progress is lost
when the server stops. The server can boot from an existing save by setting
`SAVE_NAME`, but ongoing state is never persisted back to disk.

References:
- [Geometa Support #2227](https://geometa.co.uk/support/carriercommand/2227)
- [Geometa Support #13520](https://geometa.co.uk/support/carriercommand/13520)
- [Geometa Support #26425](https://geometa.co.uk/support/carriercommand/26425)

### In-game LAN/local server browser may not find the server
When connecting from the same host or LAN, the in-game browser sometimes
fails to discover the server. Use `carrier_command.exe +connect <ip>:<port>`
from a Windows shortcut, or join via the Public Servers list. Public
discovery via Steam Master Server works correctly.

### `AUTO_UPDATE=1` adds ~50 MB of Linux Steam Runtime files per start
When `AUTO_UPDATE` is enabled, the runtime container logs into Steam on
every server start. Steam's backend then pushes the Linux variant of the
Steamworks SDK Redistributable (app 1007) into the install directory,
adding `steam-runtime/`, `libsteamwebrtc.so`, and other files alongside
the Windows DLLs we need.

This **does not break the server** — the Windows DLLs we placed during
install survive, and CC2 still starts correctly. But it adds a ~330 MB
download and several seconds to every restart, plus burns a Steam Guard
challenge if your session has expired.

The default is `AUTO_UPDATE=0` and we recommend keeping it there. If you
need automatic patch updates, the trade-off is yours to make per-server.

## Implementation Notes

### Wine, not Proton
This egg uses the standard Pterodactyl Wine yolk
(`ghcr.io/ptero-eggs/yolks:wine_latest`) rather than Proton. Two reasons:

1. **Steam DLL availability.** CC2's `dedicated_server.exe` requires
   `steamclient.dll`, `tier0_s.dll`, and `vstdlib_s.dll` — Windows DLLs
   Geometa did not ship with the dedicated server. These are obtained
   anonymously from Steamworks SDK Redistributables (app `1007`) at install
   time and placed next to `dedicated_server.exe`.
2. **CC2 stdout reaches the panel.** Under Proton, CC2's console messages
   never reach Pterodactyl's stdout. Under Wine they do, enabling accurate
   "done" detection via the `connected to Steam` message and proper
   "running" status in the panel.

This approach matches the same recipe used by the AMP CC2 module (see
`CubeCoders/AMPTemplates/carrier-command2.kvp` for reference).

### App 1007 is installed to a temporary directory
The install script installs Steamworks SDK Redistributables to
`/tmp/sdk_redist`, copies out the three required DLLs, then deletes the
temp directory. This ensures **no** `appmanifest_1007.acf` exists in
`/home/container/steamapps/`, which prevents the runtime image's
auto-update from re-pulling app 1007 in a way that could relocate or
overwrite the DLLs.

### Server config is templated by inline `sed`
On every server start, the startup command runs 13 `sed` substitutions
against `server_config.xml` to inject the current values of `SERVER_PORT`,
`SERVER_NAME`, `MAX_PLAYERS`, and the gameplay tuning variables.

**Caveat:** the substitutions use `%` as the sed delimiter. Server names
containing a literal `%` character will break the substitution. This is a
known limitation; pick a delimiter-safe name.
