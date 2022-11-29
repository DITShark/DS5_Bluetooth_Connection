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
[CHG] Controller 24:EE:9A:9D:33:D8 Class: 0x006c0104
Changing power on succeeded


$ bluetoothctl discoverable on
Changing discoverable on succeeded


$ bluetoothctl pairable on
Changing pairable on succeeded
```

### 3. Connect to your DS5 joystick.
Open your DS5 Pairing Mode (Press Create & PS Button)
<br>
Check your DS5 joystick MAC address first, Device name will be Wireless Controler, it will be uesd in the next step !<br>
```
[bluetooth]# devices
Device 48:18:8D:F5:11:EF Wireless Controller
Device 56:3F:42:C3:B9:8B 56-3F-42-C3-B9-8B
Device 7B:B4:CD:88:70:47 7B-B4-CD-88-70-47
Device 46:7D:13:7D:17:72 46-7D-13-7D-17-72
Device 61:38:62:53:E4:20 61-38-62-53-E4-20
Device 44:F9:CF:F2:9A:57 44-F9-CF-F2-9A-57
Device 67:9A:BC:DD:6B:66 67-9A-BC-DD-6B-66
Device 7E:60:67:98:00:40 7E-60-67-98-00-40
Device 4D:84:EF:96:AA:C2 4D-84-EF-96-AA-C2
Device 7D:14:5A:F9:3F:5F 7D-14-5A-F9-3F-5F
Device 47:57:8C:F9:A7:C1 47-57-8C-F9-A7-C1
Device 44:09:40:09:F5:5C 44-09-40-09-F5-5C
Device 5F:40:02:DD:E2:15 5F-40-02-DD-E2-15
Device 24:EE:9A:E4:20:81 LAPTOP-4F2N8QDB
Device 52:65:F3:B6:52:6E 52-65-F3-B6-52-6E
Device 6D:E6:40:3C:1D:BC 6D-E6-40-3C-1D-BC
Device A4:6B:B6:26:FF:51 DIT-NUC11PAHi7
Device 57:10:59:14:F6:7A 57-10-59-14-F6-7A
Device 53:8A:09:61:08:4B 53-8A-09-61-08-4B
Device 48:E7:DA:FC:62:8A RTK_BT_4.1
Device 70:58:96:04:91:7E Mi_Watch
Device 64:D6:C6:62:D1:12 64-D6-C6-62-D1-12
[bluetooth]# pair 48:18:8D:F5:11:EF

```
And then use pair and connect command.
###### (If pair command failed means you have connected this joystick before, just use connect one command only)
```
$ bluetoothctl pair 48:18:8D:F5:11:EF
Attempting to pair with 48:18:8D:F5:11:EF
[CHG] Device 48:18:8D:F5:11:EF Connected: yes
...
[CHG] Device 48:18:8D:F5:11:EF Paired: yes
Pairing successful


$ bluetoothctl connect 48:18:8D:F5:11:EF
Attempting to connect to 48:18:8D:F5:11:EF
...
Connection successful
```
