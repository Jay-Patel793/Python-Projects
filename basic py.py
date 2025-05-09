# Python-Projects


print('Welcome to the Jukebox !')
print('Please enter one of the folling options')
print('    1. Rock')
print('    2. Pop')
print('    3. Jazz')
song1 = int(input('What do you like: '))

if song1 == 1:
  print('    1. Stairway to Heaven')
  print('    2. Hey Jude')
  print('    3. All Along the Watchtower')
  song2 = int(input('What would you like to listen: '))
  if song2 == 1:
    print('Now playing Stairway to Heaven')
  if song2 == 2:
    print('Now playing Hey Jude')
  if song2 == 3:
    print('Now playing All Along the Watchtower')
  else:
    print('')

if song1 == 2:
  print('    1. Despacito')
  print('    2. Shape of You')
  print('    3. See You Again')
  song3 = int(input('What would you like to listen: '))
  if song3 == 1:
    print('Now playing Despacito')
  if song3 == 2:
    print('Now playing Shape of you')
  if song3 == 3:
    print('Now playing See You Again')
  else:
    print('')

if song1 == 3:
  print('    1. My Funny Valentine')
  print('    2. Somewhere Over The Rainbow')
  print('    3. Summertime')
  song4 = int(input('What would you like to listen: '))
  if song4 == 1:
    print('Now playing My Funny Valentine')
  if song4 == 2:
    print('Now playing Somewhere Over The Rainbow')
  if song4 == 3:
    print('Now playing Summertime')
  else:
    print('')
