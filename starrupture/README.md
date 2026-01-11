# StarRupture

StarRupture is a first-person open-world base-building game with advanced combat and tons of exploration. Play alone or in a group on this sublime and ever-changing planet, extract and manage resources, create your complex industrial system, and fight off hordes of alien monsters.

> ⚠️ **Note:** Server software is still in an experimental phase. Expect some issues in future updates!

## Contributors

| Name       | GitHub Profile                          |
|------------|-----------------------------------------|
| brainshead | https://github.com/brainshead           |
| SavageCore | https://github.com/SavageCore           |

## Server Ports

| Name | Default |
|------|---------|
| Game | 7777    |

> ⚠️ **Important:** You must connect to the server using the **WAN IP** and port, even if running locally.

## System Requirements

| Type        | Memory | Storage |
|-------------|--------|---------|
| Minimal     | 2 GB   | 25 GB   |
| Recommended | 4+ GB  | 40 GB+  |

## Configuration Files

| File                | Purpose                      | Path                                       |
|---------------------|------------------------------|--------------------------------------------|
| DSSettings.txt      | Server configuration for save management   | /home/container/DSSettings.txt |
| Password.json       | Admin password configuration | /home/container/Password.json              |
| PlayerPassword.json | Server join password configuration | /home/container/PlayerPassword.json        |
| .pteroignore        | Files/folders to ignore during backups | /home/container/.pteroignore               |

Unofficial documentation: https://wiki.starrupture-utilities.com/en/dedicated-server/configuration

---

# Setup Methods

There are two ways to configure your server: via the **Panel** (recommended) or **In-Game**. Choose one method and follow it consistently.

---

## Method 1: Panel Configuration (Recommended)

This method uses the Pterodactyl Panel and `DSSettings.txt` for all configuration. This is the recommended approach as settings persist across server restarts.

> ⚠️ **Important:** Always stop the server before making configuration changes.

### Password Setup

> ⚠️ **Warning:** Anyone who knows your IP and port can join your server if no password is set!

#### Automatic Setup (Recommended)

If you set the `[SERVER] Admin Password` and `[SERVER] Player Password` variables in the **Startup** tab before installing the server, the password files will be created automatically during installation.

#### Manual Setup

If you didn't set passwords during installation, you can create them manually:

1. Visit https://starrupture-utilities.com/passwords
2. Generate both an Admin password and a Player password
3. Create `Password.json` in the root of the container (`/home/container/`) and paste the generated content
4. Create `PlayerPassword.json` in the root of the container (`/home/container/`) and paste the generated content
5. Start the server

### Save Game Settings

The egg manages `DSSettings.txt` automatically via the Panel's **Startup** tab.

| Panel Option               | DSSettings.txt Key | Description                                                    |
|----------------------------|--------------------|----------------------------------------------------------------|
| `[SERVER] Session Name`    | `SessionName`      | Name of the save game session (max 20 characters)              |
| `[SERVER] Save Interval`   | `SaveGameInterval` | Time between automatic saves in seconds (e.g., `300` = 5 mins) |
| `[SERVER] Start new Savegame` | `StartNewGame`  | `true` to create a new world (use only once!)                  |
| `[SERVER] Load saved Game` | `LoadSavedGame`    | `true` to load an existing save on startup                     |
| `[SERVER] Savegame Name`   | `SaveGameName`     | Filename of the save to load (e.g., `AutoSave0.sav`)           |

### Creating a New World

> ⚠️ **Important:** Only enable `Start new Savegame` for initial world creation - disable it immediately after!

1. Stop the server
2. Go to the **Startup** tab in the Panel
3. Set `[SERVER] Load saved Game` to `false`
4. Set `[SERVER] Start new Savegame` to `true`
5. Start the server and wait for it to finish loading
    1. Join using the server's WAN IP and port
    2. Press ESC to open the menu and then select Save. This will instruct the server to save the file to `StarRupture\Saved\SaveGames\SessionName`
    3. Disconnect from the server
6. Stop the server
7. Set `[SERVER] Load saved Game` to `true`
8. Set `[SERVER] Start new Savegame` to `false`
9. Start the server - your world will now load automatically on every startup

### Loading an Existing Save

1. Stop the server
2. Go to the **Startup** tab in the Panel
3. Set `[SERVER] Load saved Game` to `true`
4. Set `[SERVER] Start new Savegame` to `false`
5. Set `[SERVER] Savegame Name` to match your save file (e.g., `AutoSave0.sav`)
6. Set `[SERVER] Session Name` to match your session folder name (e.g., `StarRuptureServer`)
7. Start the server

---

## Method 2: In-Game Configuration

This method uses the game's built-in **Manage Server** feature. Only use this method if you have issues with DSSettings.txt.

> ⚠️ **Important:** For this method to work, `DSSettings.txt` must **not** exist. Shutdown the server and delete it if present. You'll be stuck on a loading spinner when trying to connect if it exists.

### Password Setup

1. Start your server
2. Open the StarRupture game client
3. From the main menu, select **Manage Server** and connect to your server
4. When prompted, configure an **Admin Password**
5. Click **Change Password** to set the player join password

### Save Game Management

1. Start your server
2. Open the StarRupture game client
3. From the main menu, select **Manage Server** and connect to your server
4. Use the in-game interface to create a new world or load an existing save

> ⚠️ **Note:** With this method, you will need to load your save via the in-game interface each time the server restarts.
