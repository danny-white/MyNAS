ls -R .. > temp.out
diff temp.out ref.out > tree_diff
if [ -s tree_diff ]; then
    echo uploading new tree
    # here call drive_native on temp.out to upload new tree
    cat temp.out > ref.out
else
    echo no difference
fi
rm temp.out
rm tree_diff


