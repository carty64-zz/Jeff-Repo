#!/usr/bin/python

import os
import random

def wildcard(member_names):
  x = random.randint(0,len(member_names)-1)
  name = member_names[x]
  print name
  return name

if __name__ == "__wildcard__":
  wildcard()
