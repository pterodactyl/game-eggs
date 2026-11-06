# Alchemy Factory

## From their [Steam page](https://store.steampowered.com/app/3669570/Alchemy_Factory/)

Alchemy Factory is a factory-building automation game by D5 Copperhead. This egg runs the **experimental** Windows dedicated server (Steam App ID `4550060`, anonymous download) on Linux through Wine.

- Dedicated Server on Steam: <https://steamdb.info/app/4550060/>
- Players can join via IP:Port, join code or the in-game server list.

## How it works

- The server is installed with SteamCMD (`+@sSteamCmdForcePlatformType windows`).
- Wine runs the Windows executable. A hidden dummy X display (Xvfb) is started automatically, because Wine and the game need a display. Nothing is rendered or streamed.
- `ServerConfig.ini` is generated from the panel variables on every start.
- If `Auto Update` is `1`, SteamCMD checks for updates on every start/restart.
- The game log is mirrored into the panel console. If the server exits within 60 seconds, diagnostics (Xvfb log and game log) are printed.

## Install notes

- The first start creates the Wine prefix and takes about a minute.
- The actual server binary is `AlchemyFactory/Binaries/Win64/AlchemyFactoryServer-Win64-Shipping.exe`. The `AlchemyFactoryServer.exe` in the root folder is only a launcher and exits right away under Wine. Do not change `Server EXE` unless the game layout changes.
- Set a strong `Admin Password`. In game you become admin with `/admin <password>`.
- Join codes always work. `Steam Relay` = `0` additionally allows direct IP:Port joins.
- Stop the server only after an autosave (or when everyone has left), the server does not save on shutdown.
- If the console is empty, set `Wine Debug` to `err+all,fixme-all` and check `xvfb.log` in the file manager.

## Variables

| Variable | Default | Description |
| -------- | ------- | ----------- |
| `AF_APPID` | `4550060` | Steam App ID of the dedicated server |
| `AF_AUTO_UPDATE` | `0` | `1` = update check via SteamCMD on every start |
| `STEAM_BETA_ARGS` | empty | e.g. `-beta experimental` |
| `SERVER_NAME` | `Alchemy Factory` | Name in the server list |
| `MAX_CLIENTS` | `4` | Max players (1-6) |
| `SERVER_PUBLIC` | `1` | Show in server list |
| `SERVER_PASSWORD` | empty | Join password, empty = open |
| `ADMIN_PASSWORD` | `ChangeMe123` | Password for `/admin` |
| `MAX_ADMINS` | `1` | Max simultaneous admins |
| `AUTOSAVE_MODE` | `1` | 0 = sleep, 1 = 5 min, 2 = 10 min, 3 = never |
| `PAUSE_WHEN_EMPTY` | `1` | Pause the world when nobody is online |
| `SERVER_RELAY` | `0` | `1` = join code only |
| `SERVER_EXE` | `AlchemyFactory/Binaries/Win64/AlchemyFactoryServer-Win64-Shipping.exe` | Path relative to `/home/container/server` |
| `EXTRA_ARGS` | `-log -stdout -unattended` | Extra arguments for the executable |
| `WINEDEBUG` | `err+all,fixme-all` | Wine debug channels, `-all` silences Wine |

## Manual start (shell)

`af-wine.sh` starts the dummy display and then Wine:

```bash
./af-wine.sh server/AlchemyFactory/Binaries/Win64/AlchemyFactoryServer-Win64-Shipping.exe -log
```

## Server Ports

Ports required to run the server in a table format. The query port is always the game port + 1, so the server needs two consecutive allocations.

| Port  | default | Protocol |
| ----- | ------- | -------- |
| Game  | 9877    | UDP      |
| Query | 9878    | UDP      |
