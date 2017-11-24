python3 mail.py
if [ -f signal_out ]; then
    python3 drive.py
    rm signal_out
fi