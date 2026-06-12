# Subnautica: Nitrox Mod

Subnautica is an open world survival action-adventure video game developed and published by Unknown Worlds Entertainment.
In it, players are free to explore the ocean on an alien planet, known as planet 4546B, after their spaceship, the Aurora, crashes on the planet's surface.
The multiplayer function is provided by the mod "Nitrox". This mod is still in alpha version and therefore not yet fully stable.

## Requirements

- **Nitrox 1.8+** — older versions are not supported by this egg.
- A Steam account that owns Subnautica. The account must use **email-based** Steam Guard; the authenticator app is not supported by SteamCMD's `+set_steam_guard_code` flow.

## Steam Guard install flow

Steam Guard codes are single-use and expire quickly.

1. Trigger the first install with `STEAM_GUARDCODE` blank. SteamCMD's login will fail and Steam will email a fresh code to the account owner.
2. Paste that code into the `Steam Guard Code` variable on the server's Startup page.
3. **Reinstall** the server — the install script consumes the code and downloads Subnautica.
4. Clear the `Steam Guard Code` field after the install succeeds; it's not needed on subsequent boots.

## Server Ports

Nitrox uses a single UDP port. Pterodactyl's default allocation is assigned automatically.

| Port   | Default | Protocol |
|--------|---------|----------|
| Server | any     | UDP      |

Make sure the allocation includes UDP. Nitrox 1.8 removed the old "must be ≥1024" port restriction, so any free port the node allows is fine.

## Save folder

The save folder is hardcoded to `nitrox_world` (visible in the `Save Name` variable as read-only). Files live under `NitroxData/saves/nitrox_world/`. The `Save Name` variable is locked because Pterodactyl's config-file parser does not template variables inside file paths — changing it would break the panel's ability to manage `server.cfg`.

## Configuration

The egg manages these `server.cfg` keys from variables (no need to hand-edit unless you want options the egg doesn't expose):

- `ServerPort` (from the panel's allocation)
- `SaveInterval`, `DisableAutoSave`
- `ServerPassword`, `AdminPassword`
- `GameMode`, `SerializerMode`
- `MaxConnections`, `DefaultPlayerPerm`, `DisableConsole`
- `AutoPortForward`

The full `server.cfg` lives at `NitroxData/saves/nitrox_world/server.cfg`. Editable through the panel file manager when the server is stopped. Other Nitrox config keys not exposed as variables can be edited directly there.

## Known limitations

- **In-game console is not interactive from the panel console.** Typing `/op`, `/kick`, etc. into Pterodactyl's web console will not reach Nitrox. This is upstream — Nitrox's `ConsoleInputService` requires raw-mode terminal behaviour that Pterodactyl Wings' TTY doesn't currently provide. A yolks-level wrapper is being tracked in the Pterodactyl community. The server itself works fine; admin commands must currently be issued in-game by a player with admin permissions.
- **Graceful stop uses SIGINT, not the `stop` console command.** Consequence of the above. Pterodactyl's Stop button still works — the egg's stop configuration is set to `^C`, which .NET Generic Host catches and converts into a clean save + shutdown.

## Updating Nitrox

Set the `Nitrox Version` variable to `latest` (default) and reinstall to pull the newest release. Pin to a specific tag (e.g. `1.8.1.0`) if you need to lock the version — see [Nitrox releases](https://github.com/SubnauticaNitrox/Nitrox/releases) for tags.
