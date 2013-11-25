# file:
#    locate xkb|grep base
#    file /usr/share/X11/xkb/rules/base.lst
#    config /etc/default/keyboard
if [ "$1" = "-r" ]; then
    setxkbmap -option ctrl:nocaps
elif [ "$1" = "-s" ]; then
    setxkbmap -option ctrl:swapcaps
else
    echo "-r   reset | -s  set"
fi

# remove Lock = Caps_Lock
# remove Control = Control_L
# keysym Control_L = Caps_Lock
# keysym Caps_Lock = Control_L
# add Lock = Caps_Lock
# add Control = Control_L
