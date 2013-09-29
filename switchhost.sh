hostpath="$HOME/bin/host"
var=`date "+%F_%T"`
if [ -f "$hostpath/hosts.bak" ]; then
    bakname=$hostpath/hosts.bak.$var
    cp /etc/hosts $bakname
    echo "backup /etc/hosts to $bakname"
else
    cp /etc/hosts $hostpath/hosts.bak
    echo "backup /etc/hosts to $hostpath/hosts.bak"
fi
if [ "$1" = "qing" ]; then
    sudo cp $hostpath/hosts.qing /etc/hosts
elif [ "$1" = "vip" ]; then
    sudo cp $hostpath/hosts.vip /etc/hosts
else
    sudo cp $hostpath/hosts.pub /etc/hosts
fi

