# Windrose Dedicated Server (Pterodactyl Egg)

Embark on a PvE survival adventure set in the Age of Piracy. Explore vast procedurally generated worlds, build bases, command ships, and survive alongside other players in a persistent multiplayer environment.

Windrose is a co-op survival game featuring exploration, crafting, naval combat, and progression systems designed for both solo and group play.

---

## Overview

This egg installs and runs the **Windrose Dedicated Server** using SteamCMD and Wine, enabling hosting on Linux-based systems through the Pterodactyl Panel.

---

## Features

* Automated installation via SteamCMD
* Windows server support via Wine
* Configurable server settings (JSON-based)
* Invite code system (default connection method)
* Optional password protection
* Optional direct IP connection support
* Backup optimisation via `.pteroignore`

---

## Important Notes

* Windrose does **not provide a native Linux dedicated server**
* This egg runs the **Windows server build through Wine**
* Configuration file location:

  ```
  /home/container/R5/ServerDescription.json
  ```
* World data location:

  ```
  /home/container/R5/Saved
  ```
* Invite code is the primary connection method
* Direct IP connection is optional and may require additional network configuration

---

## Server Requirements

| Players | RAM   | Storage   |
| ------- | ----- | --------- |
| 2       | 8 GB  | 32 GB SSD |
| 4       | 12 GB | 32 GB SSD |
| 10      | 16 GB | 32 GB SSD |

> SSD storage is strongly recommended for optimal performance.

---

## Connecting to the Server

### Invite Code (Recommended)

* Uses NAT punch-through (no manual port forwarding in most cases)
* Invite code is stored in:

  ```
  /home/container/R5/ServerDescription.json
  ```

### Direct Connect

* Connect using:

  ```
  IP:PORT
  ```
* Requires:

  * Port forwarding
  * Firewall configuration
  * VPN/proxy disabled (recommended)

---

## Ports

### Invite Code Mode

* Uses dynamic NAT punch-through (requires UPnP support)

### Direct Connect Mode

* Uses the assigned **Game Port** (default: `7777`)

---

## Installation Details

This egg will:

* Download and install SteamCMD
* Install Windrose (App ID: `4129620`)
* Force Windows platform installation
* Configure Steam libraries
* Apply backup optimisation rules

---

## File Locations

**Configuration**

```
R5/ServerDescription.json
```

**Logs**

```
R5/Saved/Logs/
```

**World Data**

```
R5/Saved/SaveProfiles/
```

---

## Variables

| Variable                        | Description            |
| ------------------------------- | ---------------------- |
| `SERVER_NAME`                   | Server display name    |
| `INVITE_CODE`                   | Join code (6–32 chars) |
| `MAX_PLAYERS`                   | Maximum players        |
| `IS_PASSWORD_PROTECTED`         | Enable password        |
| `SERVER_PASSWORD`               | Server password        |
| `USE_DIRECT_CONNECTION`         | Enable direct IP       |
| `DIRECT_CONNECTION_SERVER_PORT` | Game port              |
| `WORLD_ISLAND_ID`               | World identifier       |

---

## Known Limitations

* No built-in admin tools currently
* Limited server-side configuration options
* Docker environments may have instability
* Performance may degrade at higher player counts
* Networking reliability depends on ISP and NAT behaviour

---

## Troubleshooting

### Crash: Illegal Instruction

If running in a VM:

* Set CPU type to:

  * `host`
  * `passthrough`

---

### Players Cannot Connect

Check:

* Invite code is correct
* Server is running
* VPN/proxy is disabled
* UPnP is enabled (invite mode)
* Ports are forwarded (direct mode)

---

### Logs Not Appearing

Check:

```
R5/Saved/Logs/R5.log
```

---

## Backup Optimisation

This egg includes a `.pteroignore` file to:

* Exclude unnecessary files
* Retain essential world and configuration data
* Improve backup speed and reduce size

---

## Notes for Maintainers

* Replaces minimal or outdated implementations with a more complete configuration
* Designed for reliability and production-ready deployment
