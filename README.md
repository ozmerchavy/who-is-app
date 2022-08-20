# Who's App

See who's connected to your Wi-Fi network easily on your phone, even **when you're away from home**.
Also, logs are saved every couple of mintutes on your computer for you to view later.

<img src="[drawing.jpg](https://raw.githubusercontent.com/ozmerchavy2/who-is-app/master/assets-for-github/RPReplay-Final1661005208.gif)" alt="screen capture" width="200"/>

Built for windows, dependent on ngrok, nmap and insomnia to keep your computer on.

## How to Run

1. `pip3 install python-nmap uvicorn fastapi`

66. optionally, edit `names.json` to map from local ip's to meaningful names

2. create an *ngrok* account, and [config your *ngrok* token](https://dashboard.ngrok.com/get-started/your-authtoken)

3. `run-me.bat` (you can also create a shortcut to this file)

The link will appear in *ngrok*'s terminal; browse it on your phone from anywhere.

---

If chrome warns you against ngrok, don't worry;
Some people use ngrok to create fishing servers.

credits for
- ngrok
- nmap-python
- insomnia
- hacker.css
