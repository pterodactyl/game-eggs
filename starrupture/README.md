# StarRupture

StarRupture is a first-person open-world base-building game with advanced combat and tons of exploration. Play alone or in a group on this sublime and ever-changing planet, extract and manage resources, create your complex industrial system, and fight off hordes of alien monsters.

> ⚠️ **Note:** Server software is still in an experimental phase. Expect some issues in future updates!
## Contributors

| Name       | GitHub Profile                          |
|------------|-----------------------------------------|
| brainshead | https://github.com/brainshead           |
| SavageCore | https://github.com/SavageCore           |

### Configuration files

|   File    |  Purpose  |   Path  |
|-----------|---------|---------|
| DSSettings.txt | General game configuration | /home/container/StarRupture/DSSettings.txt |
| Password.json | Admin password configuration | /home/container/Password.json |
| PlayerPassword.json | Player password configuration | /home/container/PlayerPassword.json |

You can generate the password files at https://starrupture-utilities.com/passwords.

## Server Ports

| Name    | Default       |
|---------|---------------|
| Game    | 7777 |

## System Requirements

| Type        | Memory | Storage |
|-------------|--------|---------|
| Minimal     | 2 GB   | 25 GB   |
| Recommended | 4+ GB  | 40 GB+  |

---

## Configuration

You must stop the server before making any configuration changes to DSSettings.txt or password files.

Unofficial documentation: https://wiki.starrupture-utilities.com/en/dedicated-server/configuration

### Password Protection

> ⚠️ **Warning:** Anyone who knows your IP and port can join your server if no password is set!

### Option 1: Manual Creation
1. Visit https://starrupture-utilities.com/passwords
2. Generate both an Admin password and a Player Password
3. Create `Password.json` in the root of the container (`/home/container/`) and paste the contents of the site's Password.json field into it
4. Create `PlayerPassword.json` in the root of the container (`/home/container/`) and paste the contents of the site's PlayerPassword.json field into it
5. Start server!

### Option 2: In-Game Server Management
1. Start your server (ensure no `DSSettings.txt` file exists).
2. Open the StarRupture game client.
3. From the main menu, open **Manage Server** and connect to your server.
4. When prompted, configure an **Admin Password**.
5. Click **Change Password** and enter the join password for players.
6. Press **Back** (or ESC). **Do not** create or load a game at this point.
7. Stop your server.
8. Continue with the `DSSettings.txt` configuration below.

## Save Game Management

There are two ways to manage save games:

### Option 1: Manual Configuration (Loading save when server starts.)

Create/Edit the `DSSettings.txt` file in the root directory (`/home/container/`) with the following contents:

```json
{
  "SessionName": "StarRuptureServer",
  "SaveGameInterval": "300",
  "StartNewGame": "false",
  "LoadSavedGame": "true",
  "SaveGameName": "AutoSave0.sav"
}
```

### Configuration Options

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
   "SaveGameName": "AutoSave0.sav",
   "SessionName": "MyExistingSave"
   ```
3. Upload your `.sav` and `.met` files to:
   ```
   /home/container/StarRupture/Saved/SaveGames/MyExistingSave/
   ```

   > You will need to create the `MyExistingSave` folder if it does not exist:

4. Rename the files to `AutoSave0.sav` and `AutoSave0.met`.
5. Start the server and join.

### Option 2: In-Game Server Management

1. Start your server (ensure no `DSSettings.txt` file exists).
2. Open the StarRupture game client.
3. From the main menu, open **Manage Server** and connect to your server.
4. From here, you can create a new world or load an existing save.
