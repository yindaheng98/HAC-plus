#!/bin/bash
mkdir -p HAC-plus
for video in `ls outputs`; do
  folder="outputs/$video/frame1/0.004"
  echo "Processing $folder"
  cp $folder/outputs.log HAC-plus/$video.outputs.log
  cp $folder/results.json HAC-plus/$video.results.json
done
