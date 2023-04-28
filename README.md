# 🪙 [CryptoForMe](https://crypto-for.me) Website
Built with:
- Flask
- A self-made CSS framework

## 📦 Getting started  
Requirements:
- Node.js (including `npm` and `npx`)
- Python 3.8+ (including `pip`)

Update your Python dependencies using:
```bash
pip install -r requirements.txt
```

## 🏗️ Development
To make sure everything is up to date, run:
```bash
sh dev.sh 
```

Finally, you can start the web server using:
```bash
sh run.sh
```

## 🧅 Tor Setup
You can find good (but a bit outdated) instructions on how to set up a Tor hidden service for your Flask app here:
https://github.com/satwikkansal/tor-hidden-service-python#instructions

Make sure you have `tor` installed. On Debian/Ubuntu, you can install it using `sudo apt install tor`. 
On most Linux systems, the `tor` config folder is located at `/etc/tor/`.
You can view the hidden service hostname in the `hostname` file located at `/var/lib/tor/hidden_service/`.

To start the Tor service, run `sudo systemctl start tor@default`.

### 🐛 Troubleshooting
To check if `tor` is installed and configured correctly, run `tor` and check the output for any errors.

```bash
sudo chown -R debian-tor /var/lib/tor
130 root@onlixme /etc/tor # sudo chmod -R 700 /var/lib/tor                                                                            :(
```
