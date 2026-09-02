# Brickadia (Omegga)

[Omegga](https://github.com/brickadia-community/omegga) is a server wrapper, automator, and
plugin runner for [Brickadia](https://brickadia.com/). It runs the dedicated server, adds a
plugin API for JavaScript, TypeScript, and anything that speaks JSON-RPC, and serves a
web interface for the console, players, plugins, and saves.

This egg installs Brickadia with SteamCMD, the same as the [Brickadia](..) egg, and installs
Omegga from npm on every start so it stays current without reinstalling the server.

## Server Ports

Omegga needs **two allocations**. Brickadia reports its configured port to the master server,
so the game port has to be the published one and the web UI cannot share it.

| Name    | Default | Notes |
|---------|---------|-------|
| Game    | 7777    | Primary allocation. Brickadia, UDP |
| Web UI  | 8080    | Second allocation. Set `OMEGGA_PORT` to it |
| Metrics | 9000    | Third allocation, only when `METRICS_ENABLED` is true |

## Hosting token

`BRICKADIA_TOKEN` is required. Generate one at <https://brickadia.com/account/tokens> and paste
it into **Brickadia hosting token** on the Startup tab. Omegga reads it from the environment on
every start and passes it to the server, so it stays in the panel and is never written into the
volume.

## Configuration files

|   File    |  Purpose  |   Path  |
|-----------|---------|---------|
| omegga-config.yml | Omegga configuration | /home/container/omegga-config.yml |
| GameUserSettings.ini | General server configuration | /home/container/data/Saved/Config/LinuxServer/GameUserSettings.ini |
| RoleSetup2.json | Server user role permissions | /home/container/data/Saved/Server/RoleSetup2.json |

The egg keeps `server.port` and `omegga.port` in `omegga-config.yml` in sync with the
allocations. Everything else in that file is yours to edit.

Omegga's web UI defaults to `https` with a self-signed certificate, so browsers warn on first
visit. Put a reverse proxy in front of the allocation to use a real certificate.

## Notes

- The server files are the Steam install: updates come from **Steam Auto-Updates**, not from
  Omegga's own updater, which is inactive when `BRICKADIA_DIR` points at a Steam install.
- **Update Omegga on boot** reinstalls the version in `OMEGGA_VERSION` from npm on every start.
  Turn it off to pin the copy in `node_modules`, which also lets the server start while npm is
  unreachable.
- Plugins are installed with `omegga install <url>` from the web UI or the console, into
  `/home/container/plugins`.
- amd64 only: Brickadia has no ARM server build.
