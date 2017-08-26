● NetworkManager.service - Network Manager
   Loaded: loaded (/lib/systemd/system/NetworkManager.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since mar 2017-08-22 15:04:59 CLST; 26min ago
  Process: 738 ExecStart=/usr/sbin/NetworkManager --no-daemon (code=exited, status=0/SUCCESS)
 Main PID: 738 (code=exited, status=0/SUCCESS)

ago 22 15:04:22 tectronix-desktop NetworkManager[738]: <info>  [1503425062.9064] dhcp4 (usb0): state changed timeout -> done
ago 22 15:04:22 tectronix-desktop NetworkManager[738]: <info>  [1503425062.9084] device (usb0): state change: ip-config -> failed (reason 'ip-config-unavailable') [70 120 5]
ago 22 15:04:22 tectronix-desktop NetworkManager[738]: <info>  [1503425062.9097] manager: NetworkManager state is now DISCONNECTED
ago 22 15:04:22 tectronix-desktop NetworkManager[738]: <info>  [1503425062.9109] policy: disabling autoconnect for connection 'Wired connection 2'.
ago 22 15:04:22 tectronix-desktop NetworkManager[738]: [0;1;39m<warn>  [1503425062.9122] device (usb0): Activation: failed for connection 'Wired connection 2'[0m
ago 22 15:04:22 tectronix-desktop NetworkManager[738]: <info>  [1503425062.9164] device (usb0): state change: failed -> disconnected (reason 'none') [120 30 0]
ago 22 15:04:58 tectronix-desktop NetworkManager[738]: <info>  [1503425098.9364] caught SIGTERM, shutting down normally.
ago 22 15:04:58 tectronix-desktop NetworkManager[738]: <info>  [1503425098.9444] device (enxb827eb041c0f): state change: unavailable -> unmanaged (reason 'unmanaged') [20 10 3]
ago 22 15:04:58 tectronix-desktop NetworkManager[738]: <info>  [1503425098.9524] device (usb0): state change: disconnected -> unmanaged (reason 'unmanaged') [30 10 3]
ago 22 15:04:58 tectronix-desktop NetworkManager[738]: <info>  [1503425098.9614] exiting (success)
