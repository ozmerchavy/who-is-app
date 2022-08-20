start "scan" python "src\scanner.py"
start "serve" python "src\server.py"
start "tunnel" "lib\ngrok" http 5001
start "awake" "lib\insomnia"
