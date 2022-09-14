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

https://www.instructables.com/Fingerprint-and-RFID-Based-Attendance-System-Using/

https://tutorials-raspberrypi.com/how-to-use-raspberry-pi-fingerprint-sensor-authentication/

https://learn.adafruit.com/adafruit-optical-fingerprint-sensor/circuitpython

https://www.codespeedy.com/fingerprint-detection-in-python/

https://github.com/kjanko/python-fingerprint-recognition/blob/master/app.py
