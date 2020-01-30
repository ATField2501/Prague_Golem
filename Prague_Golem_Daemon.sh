#!/bin/sh -e

#
### BEGIN INIT INFO
# Provides:          ATField2501
# Required-Start:    $all
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Bot irc
### END INIT INFO

## author: cagliostro <atfield2501@gmail.com>

DAEMON="/home/cagliostro/Documents/Prague_Golem/Prague_Golem.py" #ligne de commande du programme.
daemon_OPT="-d -p -f /home/cagliostro/Prague_Golem/Prague_Golem_Daemon.ini"  #argument à utiliser par le programme 
DAEMONUSER="cagliostro" #utilisateur du programme
daemon_NAME="Prague_Golem_Daemon.sh" #Nom du programme (doit être identique à l'exécutable).

 
PATH="/sbin:/bin:/usr/sbin:/usr/bin" #Ne pas toucher
 
test -x $DAEMON || exit 0
 
. /lib/lsb/init-functions
 
d_start () {
        log_daemon_msg "Starting system $daemon_NAME Daemon"
    start-stop-daemon --background --name $daemon_NAME --start --quiet --chuid $DAEMONUSER --exec $DAEMON -- $daemon_OPT
        log_end_msg $?
}
 
d_stop () {
        log_daemon_msg "Stopping system $daemon_NAME Daemon"
        start-stop-daemon --name $daemon_NAME --stop --retry 5 --quiet --name $daemon_NAME
    log_end_msg $?
        killall -q $daemon_NAME || true
        sleep 2
        killall -q -9 $daemon_NAME || true

}
 
case "$1" in
 
        start|stop)
                d_${1}
                ;;
 
        restart|reload|force-reload)
                        d_stop
                        d_start
                ;;
 
        force-stop)
               d_stop
                killall -q $daemon_NAME || true
                sleep 2
                killall -q -9 $daemon_NAME || true
                ;;
 
        status)
                status_of_proc "$daemon_NAME" "$DAEMON" "system-wide $daemon_NAME" && exit 0 || exit $?
                ;;
        *)
                echo "Usage: /etc/init.d/$daemon_NAME {start|stop|force-stop|restart|reload|force-reload|status}"
                exit 1
                ;;
esac
exit 0


