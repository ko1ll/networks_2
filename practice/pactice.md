University: [ITMO University](https://itmo.ru/ru/)  
Faculty: [FICT](https://fict.itmo.ru)  
Year: 2023/2024  
Group: K33212  
Author: Kirpichenko Daniil Aleksandrovich

## Упражнение



# Упражнение 1 - Установки mininet

![](https://github.com/ko1ll/networks_2/blob/main/photos/1.jpg)

### Скачиваем образ, устанавливаем и заходим 

![](https://github.com/ko1ll/networks_2/blob/main/photos/2.jpg)

### Открываем консольку, заходим с правами админа и качаем пакет mininet

![](https://github.com/ko1ll/networks_2/blob/main/photos/3.jpg)

### Тестируем, что пакет работает и все ок

# Упражнение 2 - Работа с топологиями

![](https://github.com/ko1ll/networks_2/blob/main/photos/4.jpg)

### Пытаемся запустить линейную топологиую и получаем ошибочку. Качаем openvswitch-testcontroller

![](https://github.com/ko1ll/networks_2/blob/main/photos/5.jpg)

### Пытаемся запустить линейную топологиую еще раз и получаем ошибочку снова. Чистим порт и пытаемся еще раз
Там еще минут 30 пришлось повозиться, потому что я забыл удалить какие-то строчки, которые не давали мне запустить и выдавали рандомные ошибки :(

![](https://github.com/ko1ll/networks_2/blob/main/photos/6.jpg)

### Вот так выглядит рабочая топология

![](https://github.com/ko1ll/networks_2/blob/main/photos/7.jpg)

### Проверяем, что все запускается

![](https://github.com/ko1ll/networks_2/blob/main/photos/8.jpg)

### Проверяем, кастомную топологиую

# Упражнение 3 - Работа с POX

![](https://github.com/ko1ll/networks_2/blob/main/photos/9.jpg)

### Убеждаемся, что ничего не работает в фоном режиме и перезапускает mininet

![](https://github.com/ko1ll/networks_2/blob/main/photos/10.jpg)

### Качаем POX с гита и заходим в папочку

![](https://github.com/ko1ll/networks_2/blob/main/photos/11.jpg)

### Моделируем сеть и запускаем контроллер

![](https://github.com/ko1ll/networks_2/blob/main/photos/12.jpg)

### Запускаем компонент HUB

![](https://github.com/ko1ll/networks_2/blob/main/photos/13.jpg)

### Подключаемся, предварительно установив xterm, потому что его не было и видим консольки

![](https://github.com/ko1ll/networks_2/blob/main/photos/14.jpg)

### Запускаем утилиту tcpdump и пингуем в существующий айпишник

![](https://github.com/ko1ll/networks_2/blob/main/photos/15.jpg)

### Запускаем утилиту tcpdump и пингуем в несуществующий айпишник






