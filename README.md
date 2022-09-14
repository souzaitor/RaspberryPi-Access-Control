# RaspberryPi-Access-Control

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
