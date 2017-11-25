# cron this to run every hour or something 

ls -R .. > file_hierarchy.txt
diff file_hierarchy.txt ref.out > tree_diff
if [ -s tree_diff ]; then
    echo uploading new tree
    python3 drive.py --source file_hierarchy.txt
    cat file_hierarchy.txt > ref.out
else
    echo no difference
fi
rm file_hierarchy.txt
rm tree_diff


