ps aux | grep uwsgi
killall -s INT /usr/local/bin/uwsgi
sleep 2
ps aux | grep uwsgi
setsid uwsgi ryansreader-uwsgi.ini &
#uwsgi ryansreader-uwsgi.ini
sleep 1
ps aux | grep uwsgi
