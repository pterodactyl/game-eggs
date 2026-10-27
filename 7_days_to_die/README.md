# 7 Days to Die

### Game Description

Set in a brutally unforgiving post-apocalyptic world overrun by the undead, 7 Days to Die is an open-world game that is a unique combination of first person shooter, survival horror, tower defense, and role-playing games. It presents combat, crafting, looting, mining, exploration, and character growth, in a way that has seen a rapturous response from fans worldwide. Play the definitive zombie survival sandbox RPG that came first. Navezgane awaits!

___

### Egg Capabilities

- Updated for **V3.1.0 "Henpocalypse"** (stable since 27 July 2026), which sits on top of V3.0's config format.
- **60 `serverconfig.xml` settings on the panel** — identity, slots, networking, crossplay, world selection, land claims, dynamic mesh, Telnet, the web dashboard and Twitch integration, each with a plain description. No file editing needed for anything most people change.
- Every setting is written straight into `serverconfig.xml` on each boot, so nothing needs a restart-then-restart-again to take effect.
- Automatic updates on start, with a Beta Branch setting for opting into experimental builds.
- Anonymous or authenticated Steam installs, same as before.

___

### Server Ports

7 Days to Die needs up to three ports open.

| Port | Default | Protocol | Required | Notes |
|---|---|---|---|---|
| **Game** | 26900 - 26902 | UDP | **Yes** | Main port, plus the two ports right after it that the game uses internally for its networking transports. |
| Telnet | 8081 | TCP | No | The panel console talks to the server over this. Only needs a separate allocation if you want an external tool (a Discord bot, for example) to connect too. |
| Web Dashboard | 8080 | TCP | No | Only needed if you turn on **Web Dashboard** below. Map rendering (**Web Map Rendering**) is served from this same port, not a separate one. |

> [!TIP]
> Running more than one 7 Days to Die server on the same machine? Give each one its own set of ports — two servers sharing a port range will fight over it.

___

### The V3.0 SandboxCode Change — Read This First

V3.0 "Dead Hot Summer" (stable 29 June 2026) made the biggest change to `serverconfig.xml` in the game's history: **30 gameplay properties were removed** — `GameDifficulty`, `XPMultiplier`, `BloodMoonFrequency`, `LootAbundance`, zombie speed and sense settings, and two dozen others — and replaced with a single new property, **Sandbox Code**, that encodes all 150 sandbox options at once.

> [!IMPORTANT]
> **Setting one of the removed properties does nothing, and the server won't tell you.** It boots cleanly, logs no error, and just uses whatever the Sandbox Code says instead. This is exactly what the old version of this egg was doing with its Game Difficulty setting — it looked like it worked, and it hadn't done anything since V3.0 shipped.

The Sandbox Code is **not something you type by hand**. To get one:

1. Start 7 Days to Die on your own PC and open the **Sandbox Options** menu (from the main menu, or the preset editor when starting a new game).
2. Set every option the way you want your server to play, or start from one of the built-in presets (Undead Matinee, Bite Club, Legacy Survival, and others) and adjust from there.
3. Copy the code the menu generates.
4. Paste it into this egg's **Sandbox Code** setting.

The default, `AAAJABJACJADJARFBNC`, is the official equivalent of the old `GameDifficulty` "Adventurer" setting.

> [!WARNING]
> **V3.1.0 changed the shape of the code.** It split enemy and animal density/respawn into separate day and night values and added new options (chicken coops, infection chance, hunger/thirst multipliers, stack size). A code generated before V3.1.0 may not apply cleanly — regenerate it in-game rather than reusing an old one, and run `getsandboxoptions true` in the console after starting to confirm what actually loaded.

___

### Where Each Setting Lives

| Where | What it covers | Notes |
|---|---|---|
| **This panel** | 60 `serverconfig.xml` properties | Written into the file every time the server starts. |
| **Sandbox Code** setting | All 150 gameplay/sandbox options | One opaque code, generated in-game — see above. |
| `serverconfig.xml` (File Manager) | Anything not on the panel | Edit directly, then restart. The panel will not touch a property it doesn't manage. |

> [!IMPORTANT]
> **Any setting shown on the panel is owned by the panel.** It's rewritten from the panel value every time the server starts, so hand-editing one of those lines in `serverconfig.xml` will not stick. Everything else in the file is left completely alone.

___

### First Start

1. If you want anything other than the default Adventurer-equivalent ruleset, generate a **Sandbox Code** first (see above) — it's much easier to set before your world exists than to fix after.
2. Start the server. `World` defaults to `Navezgane`, the hand-built map; set it to `RWG` with a **World Seed** if you want a randomly generated one instead.
3. The console prints `Connected with 7DTD server` once Telnet is up, which is what the panel waits on to consider the server started. World generation (if you chose RWG) happens after that and can take a few minutes on a large **World Size**.
4. In game, use **Connect to IP** with your server's address and the Game port (26900 by default).

___

### Crossplay

To let PC, PlayStation and Xbox players join the same server, all of the following need to be true:

- **Allow Crossplay** set to `true`
- **Easy Anti-Cheat** set to `true`
- **Max Players** at 8 or below
- No mods installed

> [!CAUTION]
> Easy Anti-Cheat and most gameplay-overhaul mods (DLL/Harmony mods) are mutually exclusive. If you're running a mod that needs EAC off, crossplay isn't available to you regardless of the setting above.

___

### Remote Console

7 Days to Die uses **Telnet, not Source RCON** — a standard RCON client will not connect. The panel's built-in console already speaks Telnet, so most people never need anything else. If you want an external tool (a Discord bot, for example) to connect, add the Telnet port as a separate allocation on this server and set a **Telnet Password** — with no password set, Telnet only accepts connections from the server itself.

___

### Sample Ignore File For Backups

By default the backup includes a lot of files that can be reacquired by pulling the image. Using the following file limits backups to the files that are unique to your server: your config files, logs, saves and generated worlds.

```
# Ignore all
*
# Except server config file
!serverconfig.xml
# Except server data dir
!.local/
# Except logs
!logs/
```

___

### Upgrading From The Old Version Of This Egg

This update replaces the old 9-variable egg with the 60-variable set described above, and a few names changed along the way:

- **Game Difficulty** is gone — it stopped doing anything the moment your server updated to V3.0, whether or not you'd noticed. Set a **Sandbox Code** instead (see above).
- **Telnet Password** now has the env var name `TELNET_PASSWORD` (was `PASSWORD`), and **Network Protocols** is now `DISABLED_NETWORK_PROTOCOLS` (was `SERVER_DISABLED_NETWORK_PROTOCOLS`). If you'd changed either from its default, re-set it after updating — the old values aren't carried across automatically.
- The server port is no longer a separate panel setting — it's taken from this server's main allocation, same as most other eggs.

Your existing `serverconfig.xml` and world save are untouched by the update; only the panel's list of settings changed.
