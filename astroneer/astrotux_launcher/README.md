# Astroneer AstroTuxLauncher

Astroneer dedicated server managed by [AstroTuxLauncher](https://github.com/JoeJoeTV/AstroTuxLauncher). The launcher runs the native Windows dedicated server under WINE and adds an RCON console, player monitoring, Discord/ntfy notifications and graceful saves.

An alternative to the default Astroneer egg, which runs the server under Proton. This egg is useful if you want the launcher's RCON console, notification support and status reporting.

## Install notes

Two variables are required to prevent the server from crashing on startup:

* Server Owner Name: Steam display name of the server owner. It also sets the given user as owner and administrator of the server.
* Server Owner Guid: Steam id of the server owner. It also sets the given user as owner and administrator of the server. ([Steam FAQ](https://help.steampowered.com/en/faqs/view/2816-BE67-5B69-0FEC))

**Public IP** is optional. The launcher detects it automatically; set it only if detection returns the wrong address, and enable `OVERWRITE_IP` alongside it.

There is no separate installation step. The entrypoint inspects the server directory and runs `install` on the first boot and `start` on every boot after that. The first install downloads a few hundred MiB from Steam and takes roughly a minute on a decent connection.

## Client Configuration

Encryption is disabled on the server, so every player must disable encryption on their own client. To be able to connect to the server you need to edit Engine.ini (located at %LocalAppData%\Astro\Saved\Config\WindowsNoEditor\Engine.ini) on every player's computer by adding the following :

```
[SystemSettings]
net.AllowEncryption=False
```

Clients that skip this cannot connect.

## Minimum RAM warning

Astroneer requires at least 700MiB to run. If more than one player will connect, 1GiB seems to be a minimum.

## Minimum Storage warning

Astroneer requires at least 3GiB. The size may increase with larger save file.

## Server Ports

Astroneer requires a single port to run.

| Port        | default |
|-------------|---------|
| Game        | 8777    |

### Notes

8777 is the default port for this egg, but any port can be used. The egg writes your allocation's port into `Engine.ini` automatically.

## Console commands

The launcher's RCON console accepts the following commands:

| Command     | Subcommands | Description |
|-------------|-------------|-------------|
| `help`      |             | Print the available commands. |
| `shutdown`  |             | Shut the Dedicated Server down gracefully. |
| `restart`   |             | Restart the Dedicated Server. |
| `info`      |             | Information about the running server. |
| `kick`      |             | Kick a player by GUID or name. |
| `whitelist` | `enable`, `disable`, `status` | Manage or query the whitelist. |
| `list`      |             | List players. |
| `savegame`  | `load`, `save`, `new`, `list` | Manage save games. |
| `player`    | `set`, `get` | Set or get a player's category. |

`whitelist`, `savegame` and `player` require a subcommand and do nothing without one.

## Notes

* `LOG_DEBUG` must be enabled for the server's per-line output to appear in the console. Setting it to `0` lowers the level from `DEBUG` to `INFO`; startup, save, shutdown and error lines remain visible either way.
* `SERVER_PWD` is validated with `alpha_dash`, which allows only letters, digits, hyphens and underscores. A password containing punctuation is rejected. Widen the rule to `nullable|string|between:1,100` if you need special characters.
* `SERVER_PWD` appears in cleartext in the server logs. Avoid exporting logs to a shared location if you set a password.
* The first Playfab authentication request commonly returns `HTTP Error 400: Bad Request` before the second succeeds. The launcher retries, so this is expected.

## Troubleshooting

### The server restarts itself after `shutdown`

Wings treats a server that exits without a power action as crashed, and its `detect_clean_exit_as_crash` option defaults to `true`. Because `shutdown` in the console is not a Wings power action, the process exits cleanly with code 0 and is then restarted automatically.

Disable this in `/etc/pterodactyl/config.yml`:

```yaml
crash_detection:
  enabled: true
  detect_clean_exit_as_crash: false
  timeout: 60
```

Restart Wings afterwards. Real crashes and out-of-memory kills will still be restarted; only clean exits will be left alone. The same applies to the Stop button in the panel.

### Importing the egg returns HTTP 500

This egg requires a `config.logs` key. Without it the panel's `EggParserService` reads a null value and the model rule `required_without:config_from` fails, which surfaces as a 500 rather than a 422. If you are importing an older revision, add `"logs": "{}"` to the `config` object.

### The Server Owner Guid variable is rejected

The rule is `digits_between:17,20`, which counts digits. An earlier revision used `min:17|max:20`, which Laravel reads as "value between 17 and 20" and therefore rejected every real SteamID64.

## Links

* [AstroTuxLauncher](https://github.com/JoeJoeTV/AstroTuxLauncher)
* [Docker image](https://github.com/Dxrty369/astroneer-tux)
* [Astroneer on Steam](https://store.steampowered.com/app/804360/Astroneer/)
