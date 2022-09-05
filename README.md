# WPAgen<span style="font-size: 12px; color: rgba(100, 150, 255)">BETA</span> 1.2.0

## Welcome to WPAgen

<br>

> WPAgen is a tool that helps with finding default WPA/WPA2 wireless keys.<br><br> Many wireless network providers use a certain algorithm for setting up default passwords for their routers. However, this algorithm can be exploited.<br><br>In the case were you know your target well, this tool can be helpful. Many people don't care about setting up more secure passwords for their routers which could be dangerous.
<br>
---

## About & Use cases:
<br>

*Disclaimer: This python tool is for ethical use only \*\*\**
> This tool is mainly used to generate default WPA/WPA2 wireless passkey word lists. Wireless companies usually have two passkey sequences.<br><br> Mainly in the form of:<br><br> - L N N N L N N N L L<br> - N N N N L N N N L L<br><br>Were `L` represents an uppercase letter and `N` represents a number.<br><br>Now, of course you will need to generate a very long word list in order to crack a handshake ; however, this tool can be very useful in the case of a weak target.
<br>
---

### Usage
<br>

```ps
~$ git clone https://github.com/flakkakun/WPAgen.git

~$ cd WPAgen

~$ python ./wpagen.py
```

> Now WPAgen will ask you some questions about the word list you are about to generate. And these questions are something like this:<br>

```ps
Select a valid sequence mode:    

letter-number sequence [type: LN]

number-number sequence [type: NN]

>>> {chosen mode}

---------------------------------------

Choose a name for your wordlist >>> {file name}

---------------------------------------

Choose a range for {file name}.txt >>> {range in numbers. eg: 100}
```

> After that a file with the name you chose will appear.<br>

<br>

---

#### \*\*\* This tool is for ethical and public use only. No one can copy or claim this code other than the creators and maintainers of this tool. \*\*\*
