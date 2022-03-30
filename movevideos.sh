#!/bin/bash

FLAG=1
while [ $FLAG ]
do
  echo "Would you like to create a new directory to save this video in? [Y/n]"

  read -r NEWDIRECTORY

  if [ $NEWDIRECTORY == "Y" ] ; then
  NEWDIRECTORY=1
  FLAG=0

  elif [ $NEWDIRECTORY == "n" ] ; then
  NEWDIRECTORY=0
  FLAG=0
  fi
done

echo "$NEWDIRECTORY"
