# RuneScape: Dragonwilds

A Pterodactyl egg for the RuneScape: Dragonwilds dedicated server.

## Server Requirements

| Resource | Recommended |
|----------|-------------|
| RAM | 2GB base + 1GB per player |
| CPU | Modern x86-64 CPU. Some virtualised CPU models without SSE4.2/AVX have been reported to fail; if the server crashes on boot, set your VM CPU type to `host`. |
| Players | Up to 6 |

## Configuration

### Required

**Owner ID**: Your in-game RuneScape: Dragonwilds Player ID. This is a 32-character code found at the bottom of the in-game Settings menu. It is **not** your Steam ID; a Steam ID is accepted by the game but leaves the world without an owner.

The server does not create a world until an Owner ID is set. Until then it stays on "Starting" in the panel; this is expected, not a hang.

**Server Name**: The name of your server. The in-game server browser only shows the first 16 characters.

**Default World Name**: The name of the world the server creates on first startup.

### Optional

**Admin Password**: Lets players other than the owner manage the server. Do not reuse the World Password here, or every player who joins gets admin rights.

> **World management needs the Beacon Port.** The game manages world settings over a separate UDP beacon port, not the game port. Without an allocation for it, the owner and admins cannot manage the world. See [Server Ports](#server-ports).

Values passed by the egg are applied at every startup. The game does not write them back to `RSDragonwilds/Saved/Config/LinuxServer/DedicatedServer.ini`, so don't expect to see them there.

**World Password**: The password required to join the world. Leave empty for public access.

**Extra Arguments**: Additional startup flags. The logging flags the panel needs are already part of the startup command.

Only use `-multihome` if you specifically need to bind to a specific IP and your networking environment supports it. Pterodactyl already binds the server to its allocation.

## Find your world

In game, go to the Public tab of the Worlds screen and search for your exact world name (case sensitive).

## Server Ports

The **Game** port is set automatically from your server's primary allocation. The **Beacon** port needs its own allocation on the same IP; set the **Beacon Port** variable to match it. Jagex's official server image ([runescape/rsdw-dedicated](https://github.com/runescape/rsdw-dedicated)) publishes both ports.

| Port | Default | Protocol | Purpose |
|------|---------|----------|---------|
| Game | 7777 | UDP | Main game traffic |
| Beacon | 8888 | UDP | World settings beacon (Jagex default: game port + 1111) |
