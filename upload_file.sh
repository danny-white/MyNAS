# this checks the mail, and if a signal has come in
# then upload the specified file
# signal out is a unix file path and nothing more
python3 mail.py
if [ -f signal_out ]; then
    a=$(cat signal_out)
    python3 drive.py --source $a
fi
