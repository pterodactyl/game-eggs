# RBY MMO Hub (Gen1Recomp)

Pterodactyl egg for the standalone **RBY MMO Hub** server used by Gen1Recomp and RBYMMOMod.

## Upstream Projects

- **Gen1Recomp:** https://github.com/pret/pokered
- **RBYMMOMod:** https://github.com/alamops/RBYMMOMod
- **RBY MMO Hub documentation:** https://github.com/alamops/RBYMMOMod/blob/main/server/README.md

See the upstream RBYMMOMod server documentation for complete information about the hub, configuration, networking, join codes, and available commands.

## Server Configuration

The egg exposes the hub's primary environment variables:

| Variable | Default | Description |
|---|---:|---|
| `RBY_MMO_MAX` | `4` | Maximum players, 2–64 |
| `RBY_MMO_PORT` | `7788` | Hub port |
| `RBY_MMO_LOG_LEVEL` | `info` | Hub log level |
| `RBY_MMO_GENERATION` | `1` | `1` = RBY, `2` = GSC |
| `RBY_MMO_GENERATION` | `1` | `1` = RBY, `2` = GSC |
| `SERVER_JOIN_CODE` | `(blank)` | Optional 6-character alphanumeric join code. Leave blank to generate a code automatically |

The generation variable is editable so the same egg can be used for either generation.

On first startup, the egg initializes the hub configuration automatically and generates a join code if SERVER_JOIN_CODE is blank.

## Join Code

Set SERVER_JOIN_CODE to a 6-character alphanumeric code to require players to use that code when connecting to the hub. Leave it blank to have the hub generate a code automatically.

To view the configured code:

    node server/bin/rby-mmo-hub.js invite list --reveal

See the upstream server documentation for additional hub commands and configuration options.

## Server Ports

The hub uses a single TCP port.

| Port | Default | Protocol | Required |
|---|---:|---|---|
| Game / Hub | 7788 | TCP | Yes |