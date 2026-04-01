# Runescape: Dragonwilds

> [!IMPORTANT]
> ***Migrating from your private game?***
> - Ensure you have set Owner ID! See below for instructions.
> - You can import your world from `C:\Users\<your_username>\AppData\Local\RSDragonwilds\Saved\SaveGames\<your_world_name>.sav`
> - See below for location to store your save file.
___

### Authors / Contributors

<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
    <tr>
		<td align="center">
            <a href="https://github.com/euno-sbs">
                <img src="https://avatars.githubusercontent.com/u/272661925" width="50px;" alt=""/><br /><sub><b>euno-sbs</b></sub>
            </a>
            <br />
            <a href="https://github.com/pterodactyl/game-eggs/commits?author=euno-sbs" title="Codes">💻</a>
        </td>
        <td align="center">
            <a href="https://github.com/lilkingjr1">
                <img src="https://avatars.githubusercontent.com/u/4533989" width="50px;" alt=""/><br /><sub><b>Red-Thirten</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=lilkingjr1" title="Codes">💻</a>
        </td>
        <td align="center">
            <a href="https://github.com/iamkubi">
                <img src="https://avatars.githubusercontent.com/u/6176191" width="50px;" alt=""/><br /><sub><b>Kubi</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=iamkubi" title="Codes">💻</a>
            <a href="https://github.com/parkervcp/eggs/commits?author=iamkubi" title="Contributor">💡</a>
        </td>
        <td align="center">
            <a href="https://github.com/matthewpi">
                <img src="https://avatars.githubusercontent.com/u/26559841" width="50px;" alt=""/><br /><sub><b>matthewpi</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=matthewpi" title="Codes">💻</a>
            <a href="https://github.com/parkervcp/eggs/commits?author=matthewpi" title="Contributor">💡</a>
        </td>
        <td align="center">
            <a href="https://github.com/Software-Noob">
                <img src="https://avatars.githubusercontent.com/u/10975908" width="50px;" alt=""/><br /><sub><b>Software-Noob</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=Software-Noob" title="Codes">💻</a>
            <a href="https://github.com/parkervcp/eggs/commits?author=Software-Noob" title="Contributor">💡</a>
        </td>
        <td align="center">
            <a href="https://github.com/Zarklord">
                <img src="https://avatars.githubusercontent.com/u/1622280" width="50px;" alt=""/><br /><sub><b>Zarklord</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=Zarklord" title="Codes">💻</a>
            <a href="https://github.com/parkervcp/eggs/commits?author=Zarklord" title="Contributor">💡</a>
        </td>
        <td align="center">
            <a href="https://github.com/AlienXAXS">
                <img src="https://avatars.githubusercontent.com/u/1773445" width="50px;" alt=""/><br /><sub><b>AlienXAXS</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=AlienXAXS" title="Contributor">💡</a>
        </td>
        <td align="center">
            <a href="https://github.com/gOOvER">
                <img src="https://avatars.githubusercontent.com/u/116325?v=4" width="50px;" alt=""/><br /><sub><b>gOOvER</b></sub>
            </a>
            <br />
            <a href="https://github.com/parkervcp/eggs/commits?author=gOOvER" title="Codes">💻</a>
            <a href="https://github.com/parkervcp/eggs/commits?author=gOOvER" title="Contributor">💡</a>
        </td>
    </tr>
</table>
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

___

### Game Description

From Jagex's [Website](https://dragonwilds.runescape.com/):
> On RuneScape’s forgotten continent of Ashenfall, dragons have awoken. Gather, build, skill and craft to survive in this co-operative (1-6) survival crafting game. Only by mastering survival and uncovering ancient secrets can they hope to slay the Dragon Queen—alone or with allies.

___

### Egg Capabilities

- Configurable to automatically check for server updates on start via SteamCMD. Forcing validation is also configurable.
- [*Experimental*] Configurable server branch settings.

___

### Server Ports

| Port          | Default | Protocol  | Required | Notes                                                                                                                                                  |
|---------------|---------|-----------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Primary**   | 7777    | UDP & TCP | **Yes** | Clients connect using this port. UDP is un-encrypted game traffic. |                                                                  
___

### Installation/System Requirements

|  | Bare Minimum | Recommended |
|---------|---------|---------|
| Processor | Recent x86/64 (AMD/Intel) processor that supports modern instructions (ie. AVX, AES, etc.). No 32 bit or ARM support. | Favours higher single-core performance over multiple cores. If you are running Wings via Proxmox, you may need to set the VM's CPU Type to "host" to avoid session save/load crashes. |
| RAM | 3072 MiB | 4096-8192 MiB 2GB + 1GB per additonal player. |
| Storage | 5120 MiB | 7168-10240 MiB (or more, depending on save size or frequency). |
| Host OS | Most stable Linux OS branches should work. | Using the latest kernel version for your installed OS can prevent some edge-case installation/boot issues. |
| Game Ownership | Owner ID required to start. | Required to fully "initialize" (see [Server Initialization](#server-initialization) below). |

___

### Server Initialization

> [!WARNING]
> Owner ID: this is your RuneScape: Dragonwilds Player ID. It can be found in game at the bottom of the Settings Menu. Don't hesitate to use the copy button to add it to your clipboard. The server will not start without your owner ID.

The below settings can be modified in the egg.

- Server Name
- Admin Password
- Server Password
- World Name
- Owner ID

> [!NOTE]
> The admin password seems to reset on each start of the server. You can find the password here: `home/container/RSDragonwilds/Saved/Config/LinuxServer/DedicatedServer.ini`
___

### Save Files

Save files are located in the following directory, an existing save file (including single-player saves) can be uploaded to the server but the world name must match.

```md
home/container/RSDragonwilds/Saved/SaveGames/<your_world_name>.sav
```

___

### Known Errors/Warnings

The following errors or warnings you see in the console can safely be ignored:

```log
Exiting abnormally (error code: 130)
```
↑ This misleading message occurs when stopping the server. It is printed by the Unreal Engine because it doesn't know why it was interrupted (even though it was expected by us). This can be safely ignored if you notice normal engine shutdown logs above.

```log
[  5]DominionLog: Error: TryToFindPlayerCharacter() : Local Player Character not found because World does not exist.
```
```log
[ 30]LogNetworkMatchmaker: Warning: Entitlement query failed
```
```log
[120]LogOnline: Warning: LoadSubsystemModule attempting to load module "OnlineSubsystemJpp"
```
```log
[120]LogRedpointEOS: Warning: EOS_SessionModification_AddAttribute called for string attribute '', but the string value has a length of 0 - this will probably fail!
```
```log
[120]LogNetworkMatchmaker: Warning: Entitlement query failed
```
```log
[120]LogDomMatcherSession: Warning: CREATE SESSION - Previous request still underway
```
```log
[134]LogRedpointEOS: Warning: EOS_SessionModification_AddAttribute called for string attribute '', but the string value has a length of 0 - this will probably fail!
```
```log
[361]LogRedpointEOSNetworkAuth: Warning: The dedicated server had no public/private signing keypair set, so the connection will not be automatically encrypted.
```
```log
[362]LogRedpointEOSNetworkAuth: Warning: Skipping verification of connecting user...
```
```log
[662]LogAISpawnVolume: Warning: [DedicatedServer] UpdateSpawnRowToChildVolumesMap() : Child spawn volume doesn't reference row from parent volume: Parent[AISpawnVolume_UAID_AC1A3DB43E39568202_1350897394], Child[AISpawnVolumeChildVolume], Row[Zogre_Single]
```
```log
[724]DominionLog: Warning: [DedicatedServer] FillDataArrayFromJson() : Unknown id in SpellsNew entry, skipping:
```
```log
[724]DominionLog: Warning: [DedicatedServer] LoadStateFromJson() : Unknown Actor Class in ActorsInteractedWith entry, skipping:
```
```log
[729]LogNetPackageMap: Warning: FNetGUIDCache::SupportsObject: SkillPerk...
```
↑ These seem to be common error messages with the current experimental version of the game.
