## wpa_supplicant.conf

Create a file named `wpa_supplicant.conf` in the root of the `boot` directory so that when RaspianOS boots the pi, it will automatically connect to a network defined in the conf.

Use this setup in conjunction with the [ssh setup](/docs/ssh.md) for easy headless raspberrypi setup.

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=«your_ISO-3166-1_two-letter_country_code»

network={
    ssid="«your_SSID»"
    psk="«your_PSK»"
    key_mgmt=WPA-PSK
}
```

### More info

The entire [wpa_supplicant](https://w1.fi/cgit/hostap/plain/wpa_supplicant/wpa_supplicant.conf) specification doc.
