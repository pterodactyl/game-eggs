# Windrose
Embark on a PvE survival adventure in the Age of Piracy. Fight on land and sea, solo or with friends. Build, craft and explore vast open world filled with dark secrets. Master soulslite combat and take on challenging bosses, command your ship and plunder unspoken treasures!

## Available eggs
- `egg-windrose.json` installs the Windows dedicated server through SteamCMD and runs it with Wine.
- `egg-windrose-linux.json` runs the native Linux server payload distributed through the publisher's Docker image using `ghcr.io/pterodactyl/games:windrose`.

The Linux egg stores only persistent server data in the Pterodactyl volume. Application updates are delivered through rebuilt container images and do not require a Pterodactyl reinstall.

## Warning
- If running in a VM, set the CPU type to host/passthrough (or equivalent) to expose full CPU features and avoid crashes such as:
Unhandled illegal instruction at address 000000014147C7F8 (thread 0154), starting debugger...
- The Linux runtime is currently available for `linux/amd64` only because the publisher image does not provide an arm64 payload.

## Server Requirements
| Players | RAM  | Storage |
|---------|------|---------|
| 2       | 8GB  | 32GB SSD   |
| 4       | 12GB | 32GB SSD   |
| 10      | 16GB | 32GB  SSD  |

# Connecting to the server
Players can connect by:
- Using the Direct Connect feature, allowing connection through the server's allocated hostname or IP and port. The allocation must be reachable through both TCP and UDP.
- Using Invite Code/P2P mode with the effective invite code and password, if configured. The invite code is not used while Direct Connect is enabled.

For the Linux egg, Invite Code and World Island ID may be left empty. Windrose will generate or preserve them in `R5/ServerDescription.json`. The runtime also prints the effective values and writes them to `R5/GeneratedServerValues.txt`.

## Server Ports
- With the Invite Code, ports are dynamically assigned through NAT punch-through. Ensure the router supports UPnP. Disable proxy/VPN temporarily if connections fail.
- With Direct Connect, the allocated game port is used and must be reachable through both TCP and UDP.

## Persistent files for the Linux egg
The relevant persistent data is:

```text
R5/Saved/
R5/ServerDescription.json
R5/GeneratedServerValues.txt
```

For migration or disaster recovery, restore at least `R5/Saved/` and `R5/ServerDescription.json` before starting the replacement server.

## Updates and backups
The Linux application payload is included in the runtime image. A newly published image is applied when Wings recreates the server container; the saved world and server configuration remain in the server volume.

Create a backup before applying a new Windrose version because game updates may migrate save data. Windrose's internal backup path is redirected into the persistent server volume.
