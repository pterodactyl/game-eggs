# StarRupture

StarRupture is a first-person open-world base-building game with advanced combat and tons of exploration. Play alone or in a group on this sublime and ever-changing planet, extract and manage resources, create your complex industrial system, and fight off hordes of alien monsters.

> ⚠️ **Note:** Server software is still in an experimental phase. Expect some issues in future updates!

## Contributors

| Name       | GitHub Profile                          |
|------------|-----------------------------------------|
| brainshead | https://github.com/brainshead           |
| SavageCore | https://github.com/SavageCore           |

## Server Ports

StarRupture requires 1 port:

| Port | Default |
|------|---------|
| Game | 7777    |

This can be changed to any port.

## System Requirements

| Type        | Memory | Storage |
|-------------|--------|---------|
| Minimal     | 2 GB   | 25 GB   |
| Recommended | 4+ GB  | 40 GB+  |

---

## Configuration

### Password Protection

> ⚠️ **Warning:** Anyone who knows your IP and port can join your server if no password is set!

There is currently no way to configure a password via command-line parameters or `DSSettings.txt`. You must set the password through the game client:

1. Start your server (ensure no `DSSettings.txt` file exists).
2. Open the StarRupture game client.
3. From the main menu, open **Manage Server** and connect to your server.
4. When prompted, configure an **Admin Password**.
5. Click **Change Password** and enter the join password for players.
6. Press **Back** (or ESC). **Do not** create or load a game at this point.
7. Stop your server.
8. Continue with the `DSSettings.txt` configuration below.

---

## Save Game Management

There are two ways to manage save games:

### Option 1: In-Game Server Management

1. From the main menu, click **Manage Server**.
2. Enter your server IP and port to connect.
3. From here, you can create a new world or load an existing save.

### Option 2: Manual Configuration (No Password Protection)

Create a `DSSettings.txt` file in the root directory (`/home/container/`) with the following content:

```json
{
  "SessionName": "MySaveGame",
  "SaveGameInterval": "300",
  "StartNewGame": "false",
  "LoadSavedGame": "true",
  "SaveGameName": "AutoSave0.sav"
}
```

---

## Configuration Options

| Option           | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `SessionName`    | Name of the save game session. Maximum 20 characters.                       |
| `SaveGameInterval` | Time between automatic saves in seconds (e.g., `300` = 5 minutes).        |
| `StartNewGame`   | `true` to create a new world, `false` to prevent new save creation.         |
| `LoadSavedGame`  | `true` to load an existing save, `false` to skip loading saved data.        |
| `SaveGameName`   | Filename of the save to load (e.g., `AutoSave0.sav`).                       |

---

## Creating a New World

> ⚠️ **Important:** Only set `StartNewGame` to `true` once when creating a new world!

1. Stop the server.
2. Update `DSSettings.txt`:
   ```json
   "StartNewGame": "true",
   "LoadSavedGame": "false"
   ```
3. Start the server and wait for it to finish loading.
4. Stop the server.
5. Revert `DSSettings.txt`:
   ```json
   "StartNewGame": "false",
   "LoadSavedGame": "true"
   ```
6. Start the server and join.

---

## Loading an Existing Save

1. Stop the server.
2. Ensure `DSSettings.txt` contains:
   ```json
   "StartNewGame": "false",
   "LoadSavedGame": "true",
   "SaveGameName": "AutoSave0.sav"
   ```
3. Upload your `.sav` and `.met` files to:
   ```
   /home/container/StarRupture/Saved/SaveGames
   ```
4. Rename the files to `AutoSave0.sav` and `AutoSave0.met`.
5. Start the server and join.
