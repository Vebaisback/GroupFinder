import os 
import threading
import requests, random
from dhooks import Webhook
from dhooks import Embed
from replit import db
import sys
import time 
i = 1
while i < 2:
  
  def progressbar(it, prefix="", size=60, file=sys.stdout):
      count = len(it)
      def show(j):
          x = int(size*j/count)
          file.write("%s[%s%s] %i/%i\r" % (prefix, "█"*x, "▒"*(size-x), j, count))
          file.flush()        
      show(0)
      for i, item in enumerate(it):
          yield item
          show(i+1)
      file.write("\n")
      file.flush()
  
  while len(db["webhook"]) != 120 :
    db["webhook"] = input("webhook ? :")
    if len(db["webhook"]) == 120 :
     db["login"] = "nothing"
     break
  
  #---------------------
  hook2 = db["webhook"]
  hook = Webhook(f'{hook2}')
  threads = int("900") 
  #---------------------
  
  #---------------------
  # Aleks group finder fan edititon
  #---------------------
  
  if input("send tick? 1 or 0 :") == "1":
   embed = Embed(
   description=(f'**Linked ✓ **\n\n[**Replit**](https://replit.com/@yunusbayrak/Aleks-group-finder-fan-edition?v=1)'),
   color=0x5CDBF0,
   timestamp='now'  # sets the timestamp to current time
   )
   hook.send(embed=embed)
  
  
  for i in progressbar(range(25), "getting ready: ",10):
      time.sleep(0.225) # any calculation you need
  print("✓")
  
  def groupfinder():
      id = random.randint(1000, 10000) #Change this to the range you want to scan
      r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={id}") 
      if 'owned' not in r.text:
          re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
          if 'isLocked' not in re.text and 'owner' in re.text:
              if re.json()['publicEntryAllowed'] == True:
               embed = Embed(
  
                description=(f'**Group find !!!**\n\n__id: **{id}**\n claimable: **true**__\n\n[**Group**](https://www.roblox.com/groups/group.aspx?gid={id})\n**-----------------------**\n***AleksGroupFinder***\n[**Discord**](https://discord.gg/2QzSGz8G8u)'),
                color=0x5CDBF0,
                timestamp='now'  # sets the timestamp to current time
                )
  
               hook.send(embed=embed)
               print(f"[+]Hit {id}")
              else:
               print(f"[-]wrong {id}")
          else:
           print(f"[-]wrong {id}")
      else:
        print(f"[-]wrong {id}")
  
  while True:
      if threading.active_count() <= threads:
          threading.Thread(target=groupfinder).start()
