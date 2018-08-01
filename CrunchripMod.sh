#!/bin/bash

Echo "Name of Text file/Series:"
Read FOLDER

Echo "Quality (360, 480, 720,1080)
Read QUALITY

Cat "$FOLDER.txt" | while read URL
do

	mkdir "$FOLDER"

	youtube-dl $URL --write-sub --sub-lang enUS -f 'bestvideo[height<='$QUALITY' +bestaudio/best[height<='$QUALITY']' --cookies cookies.txt

	for MP4 in ./*.mp4
	do
    		NAME=$(basename "$MP4" .mp4)
    		mkvmerge -o "$NAME.mkv" "$NAME.mp4" "$NAME.enUS.ass"
    		rm "$NAME.mp4"
    		rm "$NAME.enUS.ass"
    		mv "$NAME.mkv" "$FOLDER"
	done
done

for AssExt in ./*.ass
do
	rm "$AssExt"
done

for PartExt in ./*.part
do
	rm "$PartExt"
done