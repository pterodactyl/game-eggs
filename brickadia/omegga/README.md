# Brickadia (Omegga)

[Omegga](https://github.com/brickadia-community/omegga) is a server wrapper, automator, and
plugin runner for [Brickadia](https://brickadia.com/). It runs the dedicated server, adds a
plugin API for JavaScript, TypeScript, and anything that speaks JSON-RPC, and serves a web
interface for the console, players, plugins, and saves.

Omegga is a node application that runs and updates Brickadia itself, so the install script
installs node, Omegga, SteamCMD, and the game into the paths Omegga owns. Omegga takes over
updates from there: it saves the server, stops it, updates, starts it, and restores the world,
without the container restarting.

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
allocations. Everything else in that file is yours to edit, including `server.steambeta` for a
Steam beta branch.

Omegga's web UI defaults to `https` with a self-signed certificate, so browsers warn on first
visit. Put a reverse proxy in front of the allocation to use a real certificate.

## Notes

- **Update Omegga on boot** reinstalls the version in `OMEGGA_VERSION` from npm on every start.
  Turn it off to pin the copy in `node_modules`, which also lets the server start while npm is
  unreachable. Brickadia updates are Omegga's own either way.
- **Node version** takes effect on the next reinstall, since node is installed into the volume.
- Plugins are installed with `omegga install <url>`, or `/plugin install <url>` from the
  console, into `/home/container/plugins`. `/plugin update` updates them. Neither needs a
  `git` binary in the image, as of Omegga 1.17.0.
- amd64 only: Brickadia has no ARM server build.
