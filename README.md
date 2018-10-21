# Cabin Status (IoT)

A nodejs project that uses a RaspberryPI with a SenseHat to collect various readings around my family's cabin in the north woods of Wisconsin.

### Motivation

Since the cabin is barely a 2.5 season cabin, there are lots of interesting things that happen during the winter months that we just don't know about. So this project aims to fill in the gaps with some data, specifically:

- What is the inside temperature during the winter and how much does it vary?
- What is the orientation of the foundation as the hill that it's built into errodes away?
- Stretch reading: what's the outside temperature?
- Stretch reading: what's the temperature of the water pipes at the source of the well?
- Stretch reading: what's the temperature of the water pipes in the ground along the way to the cabin?
- Stretch reading: what's the temperature of the water pipes at the connection to the cabin?

With other readings being more for fun:

- What is the humidity during the winter?
- What is the pressure during the winter?
- Are there any seismographic events that occur?
- Does the direction of magnetic north change during different seasons?

### What I hope to learn

Above all just how to work on an Internet of Things project using some low level hardware using a software language that I know really well.

In terms of what questions I hope to use the data to answer:

1. Do we need to be concerned about how the hill errosion is damaging our cabin's foundation?
2. How fast / slow is the foundation changing, if at all?
3. What's the inside temperature of the cabin so that we can plan furniture upkeep better?
4. How much effort and construction must we put into properly insulating the water pipes such that the cabin is usable during the winter months?
5. Can a person survive in the cabin during the coldest winter Wisconsin can throw at them?

### Main sensor hardware

- [x] RaspberryPi Zero W
- [x] RaspberryPI SenseHat
- [ ] External/Renewable power source (PiJuice or SleepyPi)
- [ ] Enclosure that adheres to foundation

### Main sensor software

- [x] RaspianOS
- [x] enable `ssh`: [ssh docs](/docs/ssh.md)
- [x] auto-connect to wifi network via `wpa_supplicant`: [wpa_supplicant docs](/docs/wpa_supplicant.md)
- [ ] Install [SenseHat Lib](https://github.com/RPi-Distro/python-sense-hat) for python
- [ ] Install sqlite3
- [ ] Install nodejs
- [ ] rsync application code to pi (or git clone)

---

### Satellite PoE sensor hardware

- [ ] RaspberryPi (any model compatible with PoE Hat)
- [ ] RaspberryPi PoE Hat
- [ ] Ethernet capable of PoE
- [ ] Any sensor
- [ ] Enclosure

### Satellite PoE sensor software

- [ ] RaspianOS
- [ ] enable `ssh`: [ssh docs](/docs/ssh.md)
- [ ] auto-connect to wifi network via `wpa_supplicant`: [wpa_supplicant docs](/docs/wpa_supplicant.md)
- [ ] Install sqlite3
- [ ] Install nodejs
- [ ] rsync app code to pi (or git clone)

### License

MIT
