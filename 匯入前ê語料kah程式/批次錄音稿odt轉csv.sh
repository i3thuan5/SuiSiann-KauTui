#!/bin/bash

find $1 -type f -name '*.odt' | while read inputName ; do
  #echo $inputName
  outputName=`basename "$inputName"` 
  echo $outputName
  python 錄音稿的odt轉csv.py "$inputName" "$outputName"
done
