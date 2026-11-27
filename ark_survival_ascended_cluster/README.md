# ARK: Survival Ascended (Cluster)

The [ARK: Survival Ascended](../ark_survival_ascended) egg with one addition: a **Cluster ID** variable, passed to the server as `-clusterid`. Everything else (install, ports, RCON, mods) is the same as that egg, so its README applies here too.

Use this egg for every server that should be part of one cluster. Players can then upload a character, dinos and items at an obelisk or transmitter on one server and download them on another.

## Setting up a cluster

A cluster needs two things on every server in it:

1. **The same Cluster ID.** Set the `Cluster ID` variable to the same value on each server. Use letters, numbers, dashes and underscores only.
2. **The same cluster folder.** ARK keeps what players upload in `ShooterGame/Saved/clusters`. Every server in the cluster has to read and write the same copy of that folder, so the servers have to run on the same node.

### Sharing the folder on Pterodactyl+

1. Open one of the servers and go to **Shared Folders**.
2. Create a folder with the path `ShooterGame/Saved/clusters`.
3. On each of the other servers, open **Shared Folders**, choose **Add Existing**, pick that folder and give it the same path.
4. Restart every server. A shared folder is mounted when a server starts.

### Sharing the folder on Pterodactyl

Ask an administrator to create a mount (Admin, Mounts) with the target `/home/container/ShooterGame/Saved/clusters` and attach it to every server in the cluster, then restart them.

## Notes

- Each server still needs its own map, ports and session name.
- Leave `-ClusterDirOverride` out of the additional arguments. It moves the cluster folder somewhere the servers do not share.
- Servers with different settings may refuse some transfers. Add `-NoTransferFromFiltering` to the additional arguments on every server to allow them.
- Survival Evolved and Survival Ascended servers cannot be in the same cluster.

## Recommended server settings

### Minimum RAM

Each server in the cluster needs about 11GB of RAM to run with no players on a default map. See the [ARK: Survival Ascended](../ark_survival_ascended) README.

## Server Ports

| Port            | Default |
| --------------- | ------- |
| Game            | 7777    |
| RCON (optional) | 37015   |
