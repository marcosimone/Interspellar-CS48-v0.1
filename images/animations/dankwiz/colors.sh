#!/bin/bash

if [ "$#" -ne 1 ]
then
    echo "USAGE: $0 [hex color code]"
    echo "example: $0 004d00"
   
    exit
fi

rm -rf $1
dir=pwd
color=$1
mkdir $color

for sprite in *.png
do
    convert $sprite -fill "#fffff5" -opaque "#6c6658" __temp.png
    convert __temp.png -fill "#fffff7" -opaque "#6d6656" __temp.png
    convert __temp.png -fuzz 20% -fill "#$color" -opaque "#494949" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#6c6658" -opaque "#fffff5" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#6d6656" -opaque "#fffff7" $color/_wizard_temp_color.png	
    convert $sprite -type Grayscale -brightness-contrast 50x -transparent white $color/_wizard_temp_grayscale.png
    convert $color/_wizard_temp_grayscale.png -fill "#ffffff" -opaque "#e6e6e6" -transparent white $color/_wizard_temp_grayscale.png
    composite -watermark 30% -gravity center $color/_wizard_temp_grayscale.png $color/_wizard_temp_color.png  $color/$sprite
    convert $color/$sprite -transparent white $color/$sprite
    rm __temp.png $color/_wizard_temp_color.png $color/_wizard_temp_grayscale.png 
    
done
