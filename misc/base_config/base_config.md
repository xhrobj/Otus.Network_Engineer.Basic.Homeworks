**Базовая настройка коммутатора**

```

enable
configure terminal

! При наборе неверных команд, не пытаться их интерпретировать
! как имя хоста с последующим походом в DNS
no ip domain-lookup

```

***Имя хоста и баннер***

Пользователь сначала увидит banner motd, а затем, когда будет готов ввести свои учетные данные, увидит banner login

```

hostname Switch-2960C
banner motd = 
        .__       .__           ____ 
  _____ |__| _____|  |__   ____/_   |
 /     \|  |/  ___/  |  \_/ __ \|   |
|  Y Y  \  |\___ \|   Y  \  ___/|   |
|__|_|  /__/____  >___|  /\___  >___|
      \/        \/     \/     \/     
=

banner login " Hello, Switch "

```

***Настройка паролей***

Команда `line console 0` с подкомандами `password` и `login` включают аутентификацию на входе в систему и устанавливают пароль на консольном терминальном порту

```

! Пароль на CONSOLE
line console 0
logging synchronous
password cisco
login
exit

```

Порты Telnet на коммутаторе известны как линии VTY (Virtual TeletYpe). На коммутаторе может работать до 16 виртуальных портов, обеспечивающих до 16 одновременных сеансов Telnet. Виртуальные порты пронумерованы от 0 до 15.

Команда `line vty 0 4` с подкомандами `password` и `login` включают аутентификацию на входе в систему и устанавливают пароль для сеансов Telnet

```

! Пароль на VTY
line vty 0 4
logging synchronous
password cisco
login

! ... и разрешить подключение по telnet
transport input telnet

exit

```

Пароль на доступ к привилегированному режиму EXEC

```

! Пароль на enable
enable password class
! или
enable secret class

```

Скрываем пароли

```

! Скрываем пароли
service password-encryption

! Чтобы отключить шифрование паролей
! no service password-encryption

```

другое ...

```

! ip-адрес для коммутатора
interface vlan 1
ip address 192.168.1.11 255.255.255.0
no shutdown
exit

end

```

Копируем текущую конфигурацию в NVRAM

```

! Сохраняем конфигурацию
! write memory
copy running-config startup-config

```