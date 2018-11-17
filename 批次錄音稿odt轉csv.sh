#!/bin/bash

find ../ -type f -name '*.odt' | while read inputName ; do
  outputName=${inputName%.odt}
  echo $outputName
  #python 錄音稿的odt轉csv.py $inputName
done
