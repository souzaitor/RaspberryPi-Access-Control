<h1 align="center"> RaspberryPi Fingerprint Access Control </h1>

![WhatsApp-Video-2022-09-19-at-10 25 05](https://user-images.githubusercontent.com/39158108/191032555-744235cd-15d2-42db-b0dd-2c2b959f6726.gif) 

![WhatsApp-Video-2022-09-19-at-10 25 20](https://user-images.githubusercontent.com/39158108/191032673-4c773d0f-ce95-4d4a-b516-c426bf8f665f.gif)

## 🔵 Introduction

Project proposed during the course of Embedded Computer Systems Project (1001538), offered by the Department of Computing at UFSCar in semester 2022/1.


With fingerprint access control, you use a fingerprint scanner to create a template for each person you want to authorise for access. Then when they present their finger at a fingerprint reader, for example by a door, it’s compared with the stored template in your database. If it’s a match, they’re given access.

## 🔵 Components

- 1 x [Raspberry Pi 3](https://components101.com/sites/default/files/component_datasheet/Raspberry%20Pi%203%20Datasheet.pdf)
- 1 x [FPM10A (50 DY) Optical Fingerprint sensor](https://cdn.awsli.com.br/945/945993/arquivos/FPM10A-DY50.pdf) 
- 1 x [Relay](https://s3-sa-east-1.amazonaws.com/robocore-lojavirtual/258/Relay_AX.pdf)
- 1 x [Buzzer](https://datasheetspdf.com/datasheet/KY-006.html)
- 1 x [USB / Serial - UART converter](https://www.mouser.com/datasheet/2/117/usb232r-ds-v10-14032.pdf)
- 1 x [Potentiometers 10k](https://components101.com/resistors/potentiometer)
- 1 x [LCD 16x2 5V - GDM1602K](https://www.sparkfun.com/datasheets/LCD/GDM1602K.pdf)

## 🔵 Schematic
![Capturar](https://user-images.githubusercontent.com/39158108/190927242-fd24282c-425d-45e4-a3ac-49613fc4d011.JPG)

## 🔵 Roadmap
- [x] Identify the user by biometrics 
- [X] Query an HTTP server, via GET method, checking if that user is authorized to access the site
- [x] Trigger a relay, which will be responsible for opening the door
- [x] Log access to a file in the server
- [x] Display "Access Allowed" or "Access Denied"
- [x] Beep when releasing access 

## 🔵 Authors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/souzaitor">
        <img src="https://avatars.githubusercontent.com/souzaitor" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Heitor Souza</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/hugo-souza">
        <img src="https://avatars.githubusercontent.com/hugo-souza" width="100px;" alt="Foto do Mark Zuckerberg"/><br>
        <sub>
          <b>Hugo Souza</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<!-- LICENSE -->
## 🔵 License

Distributed under the MIT License. See [LICENSE.txt](https://github.com/souzaitor/RaspberryPi-Access-Control/blob/main/LICENSE) for more information.


## 🔵 Acknowledgments
* [**Adafruit Optical Fingerprint Sensor**](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor/circuitpython)
* [**Python library for ZFM fingerprint sensors**](https://github.com/bastianraschke/pyfingerprint)
* [**Raspberry Pi GPIO pinout guide**](https://pinout.xyz/#)
* [**RPLCD Documentation**](https://rplcd.readthedocs.io/en/stable/)
