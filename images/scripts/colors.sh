#!/bin/bash

dir=pwd
color=$1
mkdir $color

for sprite in *.png
do
    convert $sprite -fuzz 20% -fill "#$color" -opaque "#494949" $color/_wizard_temp_color.png
    convert $sprite -type Grayscale -brightness-contrast 50x -transparent white $color/_wizard_temp_grayscale.png
    composite -blend 75 $color/_wizard_temp_color.png $color/_wizard_temp_grayscale.png $color/$sprite
done
