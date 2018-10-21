## ssh

To enable ssh daemon on startup of a fresh install of Raspian:

1. create a file named `ssh` with any contents in the boot directory
2. boot up the raspberryPi.
3. if your pi is connected to a network: `ssh pi@<the-pi-ip-address>` or `ssh pi@raspberrypi.local`
4. default password is: `raspberry`

To connect your pi to a network in headless mode see the [wpa_supplicant configuration docs](/docs/wpa_supplicant.md).
