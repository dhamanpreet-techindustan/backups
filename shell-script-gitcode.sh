#!/bin/bash

src_dir=/home/dhaman/web
# which directory we have to backup
tgt_dir=/home/dhaman/backups
# where copy the backups
curr_timestamp=$(date "+%Y-%m-%d-%H-%M-%S")
# script of backup time with folder
backup_file=$tgt_dir/$curr_timestamp.tgz
# show dir-name and date in backup folder
echo "Taking backup"
#echo "$backup_file"

tar czf $backup_file --absolute-names $src_dir
# making zip file of src_dir
declare -A map
# declare map for repo
map["back"]="backups"

#git init
#git checkout -b master
git add .
# add file add <file name> to add all file add .
git commit -m "committed"
# commit file with change we change in file
git push origin master
# push file in  branch master
#for i in "$(!map[@])"
#do
#       git remote add $i git@github.com:dhamanpreet-techindustan/${map[$i]}.git
#       git push -u $i master
#done
echo "backup complete"
