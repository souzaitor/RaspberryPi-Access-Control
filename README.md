# RaspberryPi-Access-Control

## Materiais

- 1 x [Raspberry Pi 3](https://components101.com/sites/default/files/component_datasheet/Raspberry%20Pi%203%20Datasheet.pdf)
- 1 x [FPM10A (50 DY) Optical Fingerprint sensor](https://cdn.awsli.com.br/945/945993/arquivos/FPM10A-DY50.pdf) 
- 1 x [Relay](https://s3-sa-east-1.amazonaws.com/robocore-lojavirtual/258/Relay_AX.pdf)
- 1 x Buzzer
- 1 x USB / Serial - UART converter
- 4 x button
- 1 x LCD 16x2 5V - GDM1602K

## Requisitos/funcionalidades obrigatórias
- [ ] Identificar o usuário por biometria ou cartão de acesso RFID (Carteirinha da UFSCar)
- [ ] Consultar um servidor HTTP, via método GET, verificando se aquele usuário está autorizado a acessar o local
- [ ] Caso ocorra falha de conexão ao consultar o servidor, verificar em uma memória local (SD Card) se aquele usuário está autorizado
- [ ] Acionar um rele, que será responsável por abrir a porta

## Requisitos opcionais / desejáveis
- [ ] Registrar log de acesso em um arquivo no cartão de memória
- [ ] Sincronizar data e hora com a Internet
- [ ] Exibir data e hora em um display e mensagem "Acesso Liberado" ou "Acesso Negado"
- [ ] Emitir um sinal sonoro ao liberar acesso (BEEP)


## Referências
[Adafruit Optical Fingerprint Sensor](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor/circuitpython)

https://github.com/moka1309/Biometric-Attendance-System-using-Python-and-Raspberry-pi-3-/blob/master/attendance/enroll.py

[Python library for ZFM fingerprint sensors](https://github.com/bastianraschke/pyfingerprint)

https://github.com/bastianraschke/pyfingerprint/issues/40
