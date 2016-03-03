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
    convert $sprite -fuzz 10% -fill "#$color" -opaque "#47354a" $color/_wizard_temp_color.png
    #convert $color/_wizard_temp_color.png -fuzz 10% -fill "#$color" -opaque "#896475" $color/_wizard_temp_color.png
    convert $sprite -type Grayscale -brightness-contrast 50x -transparent white $color/_wizard_temp_grayscale.png
    convert $color/_wizard_temp_grayscale.png -fill "#ffffff" -opaque "#e6e6e6" -transparent white $color/_wizard_temp_grayscale.png
    composite -watermark 30% -gravity center $color/_wizard_temp_grayscale.png $color/_wizard_temp_color.png  $color/$sprite
    convert $color/$sprite -transparent white $color/$sprite
    rm $color/_wizard_temp_color.png $color/_wizard_temp_grayscale.png

done
