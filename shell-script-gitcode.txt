#!/bin/bash

src_dir=/home/dhaman/web
tgt_dir=/home/dhaman/backups

curr_timestamp=$(date "+%Y-%m-%d-%H-%M-%S")
backup_file=$tgt_dir/$curr_timestamp.tgz
echo "Taking backup"
#echo "$backup_file"

tar czf $backup_file --absolute-names $src_dir

declare -A map

map["back"]="backups"

#git init
#git checkout -b master
git add .
git commit -m "committed"
git push origin master
#for i in "$(!map[@])"
#do
#       git remote add $i git@github.com:dhamanpreet-techindustan/${map[$i]}.git
#       git push -u $i master
#done
echo "backup complete"
