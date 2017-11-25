# this checks the mail, and if a signal has come in
# then upload the specified file
# signal out is a unix file path and nothing more
SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/Danny/apache-ant-1.10.1/bin:/Library/TeX/texbin:/opt/X11/bin
cd /Users/Danny/Documents/CS/NAS
echo $PATH > ~/cronpath.txt
python3 mail.py
if [ -f signal_out ]; then
    a=$(cat signal_out)
    python3 drive.py --source $a
    rm signal_out
fi
