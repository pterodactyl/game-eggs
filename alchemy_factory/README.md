# Alchemy Factory

Start small, team up with friends, and automate production with conveyor belts, pipes, and magical devices. Stock your shop with potions, jewelry, and relics, complete commissions, and build an alchemy empire!

> Note: Server software is still in an experimental phase. Expect some issues in future updates!

---

## Recommended Server Settings

| Setting | Recommended Value | Notes |
|---------|-------------------|-------|
| Max Clients | 4 | Adjust based on server resources |
| Autosave Mode | 1 | Save every 5 minutes |
| Pause When Empty | 1 | Pause when no players connected |
| Session Retry Seconds | 10 | Retry Steam session creation |

---

## Server Ports

| Name | Default |
|------|---------|
| Game | 9877    |
| Query | 9878    |

Both ports are UDP and must be open in your firewall.

---

## System Requirements

| Type        | Memory | Storage |
|-------------|--------|---------|
| Minimal     | 1 GB   | 10 GB   |
| Recommended | 2+ GB  | 20 GB+  |

---

## Configuration

Server configuration is managed via `ServerConfig.ini`, which is generated automatically on first launch. Settings take effect after a server restart.

The following settings can be configured through the Panel:

| Panel Option | Config Key | Description |
|--------------|------------|-------------|
| Server Name | `server_name` | Name shown in the server browser |
| Query Port | `query_port` | Steam query port |
| Server Public | `server_public` | Make the server publicly visible in the server browser |
| Steam Relay | `server_relay` | Routes server traffic through Steam, allowing hosting without a public IP |
| LAN Mode | `server_lan` | Make the server visible only to players on the same local network |
| Server Password | `server_password` | Password required to join the server (leave empty for none) |
| Admin Password | `admin_password` | Enter /admin <password> in game chat to become an admin (leave empty for none) |
| Max Clients | `max_clients` | Maximum number of simultaneous players |
| Max Admins | `max_admins` | Maximum number of simultaneous admins |
| Autosave Mode | `autosave_mode` | 0=Save when Sleep, 1=Save every 5 Min, 2=Save every 10 Min, 3=Never Save |
| Pause When Empty | `pause_when_empty` | Pause the game while no player is connected |
| Session Retry Seconds | `session_retry_seconds` | Seconds to wait after a failed Steam session creation before retrying |

Command line `-Port=` / `-QueryPort=` override the ini settings when specified.

---

## How to Join

- **Public server**: If `server_public` is enabled, anyone can find and join the server through the server list.
- **Direct IP**: If the server has a public IP address and `server_relay` is set to `0`, players can connect using `IP:Port`.
- **Join Code**: Once a Join Code has been generated, share it with other players to let them join.

---

## How to Become an Admin

1. Join the server and enter the server password if required
2. Press Enter to open the chat
3. Enter `/admin <admin password>`
4. Press Enter to confirm

Enter `/help` in the chat to view available commands.

---

## Backup Configuration

The following files and folders are backed up by default:

- `ServerConfig.ini` - Server configuration
- `AlchemyFactory/Saved/SaveGames/` - All save game folders

---

## Official Documentation

Dedicated Server guide: https://steamcommunity.com/sharedfiles/filedetails/?id=3797831446
