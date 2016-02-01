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
    convert __temp.png -fill "#fffff0" -opaque "#69604E" __temp.png
    convert __temp.png -fill "#fffff1" -opaque "#4C4638" __temp.png
    convert __temp.png -fill "#fffff2" -opaque "#6B634E" __temp.png
    convert __temp.png -fill "#fffff3" -opaque "#4B4239" __temp.png
    convert __temp.png -fill "#fffff4" -opaque "#6E6351" __temp.png
    convert __temp.png -fill "#fffff6" -opaque "#4E4735" __temp.png
    convert __temp.png -fill "#fffff8" -opaque "#3F3128" __temp.png
    convert __temp.png -fill "#fffff9" -opaque "#333527" __temp.png
    convert __temp.png -fill "#fffffa" -opaque "#4F4539" __temp.png
    convert __temp.png -fuzz 20% -fill "#$color" -opaque "#494949" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#6c6658" -opaque "#fffff5" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#6d6656" -opaque "#fffff7" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#69604E" -opaque "#fffff0" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#4C4638" -opaque "#fffff1" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#6B634E" -opaque "#fffff2" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#4B4239" -opaque "#fffff3" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#6E6351" -opaque "#fffff4" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#4E4735" -opaque "#fffff6" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#3F3128" -opaque "#fffff8" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#333527" -opaque "#fffff9" $color/_wizard_temp_color.png
    convert $color/_wizard_temp_color.png -fill "#4F4539" -opaque "#fffffa" $color/_wizard_temp_color.png
    convert $sprite -type Grayscale -brightness-contrast 50x -transparent white $color/_wizard_temp_grayscale.png
    convert $color/_wizard_temp_grayscale.png -fill "#ffffff" -opaque "#e6e6e6" -transparent white $color/_wizard_temp_grayscale.png
    composite -watermark 30% -gravity center $color/_wizard_temp_grayscale.png $color/_wizard_temp_color.png  $color/$sprite
    convert $color/$sprite -transparent white $color/$sprite
    rm __temp.png $color/_wizard_temp_color.png $color/_wizard_temp_grayscale.png 
    
done
