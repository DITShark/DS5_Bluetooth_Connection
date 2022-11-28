# DS5_Bluetooth_Connection
This is for Connection between Ubuntu (PI4 &amp; NUC) and Dualsense 5 through Bluetooth.
<br><br>

## Bluetooth Connection with Ubuntu Terminal
Refer to this website : https://www.baeldung.com/linux/bluetooth-via-terminal
<br>
You can use this as a reference.
<br>

### 1. Open your terminal and use bluetoothctl command. And then use show command.
```
$ bluetoothctl

$ show
Controller 24:EE:9A:9D:33:D8 (public)
	Name: shark-ubuntu20
	Alias: shark-ubuntu20
	Class: 0x000c0000
	Powered: yes
	Discoverable: no
	DiscoverableTimeout: 0x000000b4
	Pairable: yes
	UUID: Headset AG                (00001112-0000-1000-8000-00805f9b34fb)
	UUID: Audio Source              (0000110a-0000-1000-8000-00805f9b34fb)
	UUID: Headset                   (00001108-0000-1000-8000-00805f9b34fb)
	UUID: PnP Information           (00001200-0000-1000-8000-00805f9b34fb)
	UUID: A/V Remote Control Target (0000110c-0000-1000-8000-00805f9b34fb)
	UUID: A/V Remote Control        (0000110e-0000-1000-8000-00805f9b34fb)
	UUID: Audio Sink                (0000110b-0000-1000-8000-00805f9b34fb)
	Modalias: usb:v1D6Bp0246d0535
	Discovering: no

```
<br>
You can check your status at here, and the most important part is to check the power, discoverable and pairable status.<br><br>

### 2. Change Your Power, Discoverable and Pairable Status. 
###### (If all status are on you can skip this part !)
Use power on, discoverable on, pairable on 3 commands to open needed status.
```
$ bluetoothctl power on
[CHG] Controller 00:1A:7D:DA:71:15 Class: 0x006c0104
Changing power on succeeded

$ bluetoothctl discoverable on
Changing discoverable on succeeded

$ bluetoothctl pairable on
Changing pairable on succeeded
```

### 3. Connect to your DS5 joystick.
