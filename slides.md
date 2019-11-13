---
customTheme : "custom_night"
transition: "slide"
highlightTheme: "monokai"
slideNumber: false
title: "Hacking with Python"
enableTitleFooter: false
logoImg: false

---

## Hacking networks

# with

![Python](/img/python.logo.png =250x)

---

<!-- .slide: style="text-align: left;" -->

### What's Scapy 

![Scapy](img/scapy.logo.png =200x)

_"Is a **Python program** that enables the user to **send**, **sniff**, **dissect**  and **forge network packets**"_

_"In other words, is a **powerful** interactive packet manipulation program"_

---

## Let's forge some packets

--

### Do you Remember OSI?

![wireshark osi](img/wireshark_layers_icmp.png)

--

### Show me the code

```python
pkg = IP(dst="8.8.8.8")/ICMP(type=8)/"Payload Data"
pkg.show()
```

```python
###[ IP ]### 
    version= 4
    ihl= None
    tos= 0x0
    len= None
    id= 1
    flags= 
    frag= 0
    ttl= 64
    proto= icmp
    chksum= None
    src= 192.168.177.131
    dst= 8.8.8.8
    \options\
    ###[ ICMP ]### 
        type= echo-request
        code= 0
        chksum= None
        id= 0x0
        seq= 0x0
        ###[ Raw ]### 
            load= 'Payload Data'
```

---

## Let's send some packets

--

<!-- .slide: style="text-align: left;" -->

### Some types of send

#### **By layer**

* **Send in layer 3:** send, sr, sr1, srloop...
* **Send**p **in layer 2:** sendp, srp, srp1, srploop...

--

<!-- .slide: style="text-align: left;" -->

### Some types of send

#### **By behavior**

* **Just send some packages:** send, sendp...
* **Send some receive some:** sr srp, srloop, srploop...
* **Send some receive first:** sr1, srp1...

--

### Now, show the code

```python
pkg = IP(dst="8.8.8.8")/ICMP(type=8)/"Payload Data"
rec = sr1(pkg)
rec.show()
```

```python
###[ IP ]###
    version= 4
    ihl= 5
    tos= 0x0
    len= 40
    id= 25657
    flags= 
    frag= 0
    ttl= 128
    proto= icmp
    chksum= 0x5460
    src= 8.8.8.8
    dst= 192.168.177.131
    \options\
    ###[ ICMP ]###
        type= echo-reply
        code= 0
        chksum= 0xa9ed
        id= 0x0
        seq= 0x0
    ###[ Raw ]###
            load= 'Payload Data'
    ###[ Padding ]###
                load= '\x00\x00\x00\x00\x00\x00'
```

---

## What about sniff and dissect

--

```python
def arp_monitor_callback(pkt):
    # Dissect
    if ARP in pkt and pkt[ARP].op in (1,2): #who-has or is-at
        return print(f"{pkt[ARP].hwsrc} {pkt[ARP].psrc}")

# And sniff
sniff(prn=arp_monitor_callback, filter="arp", store=0)
```

```python
00:0c:29:ff:ff:ff 192.168.177.131
00:50:56:ff:ff:ff 192.168.177.2
```

--

#### Little break for some code reading

* [sendp - write packages at layer 2](https://github.com/secdev/scapy/blob/master/scapy/sendrecv.py#L338)
* [sniff and AsyncSniffer - for package reading from interface](https://github.com/secdev/scapy/blob/43fda76e560e3c94ab64fc23f8ee29c582b459be/scapy/sendrecv.py#L1021)

---

#### Did you said powerful???

![sounds good to me](/img/gif/sounds_good_to_me.gif =x500)

--

`ping -c1 8.8.8.8`

`tcpdump arp`

---

## DEMO 1

--

![cat board](/img/gif/cat_board.gif =x800)

---

## DEMO 2

[Pinecone - deauth module](https://github.com/pinecone-wifi/pinecone/blob/master/modules/attack/deauth/deauth.py#L72)

--

![elmo](img/gif/elmo.webp)

---

## DEMO 3

[Pinecone - recon module](https://github.com/pinecone-wifi/pinecone/blob/master/modules/discovery/recon/recon.py#L91)

---

<!-- .slide: style="text-align: left;" -->

### Other things

#### Talk Evaluation!!
https://bit.ly/2CFJP4S

### We are hiring
https://tarlogic.talentclue.com/co/tarlogic

#### I have some merchandising stuff 😀 🖊🗒

---

## That's all, thanks!
### **Any questions?**