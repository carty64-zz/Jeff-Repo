import time
import slack
import os
import random

token = os.environ["LEBOWS_KEY"]
sc = slack.WebClient(token)

quotes={1:"Well that's just, like, your opinion, man."
        ,2:"Shut the fuck up, Donny!"
        ,3:"No, you're not wrong Walter, you're just an asshole."
        ,4:"Donny, you're out of your element!"
        ,5:"Smokey, this is not 'Nam. This is bowling. There are rules."
        ,6:"Nobody fucks with the Jesus."
        ,7:"Sometimes you eat the bear, and sometimes, well, he eats you."
        ,8:"I'm the Dude. So that's what you call me. You know, that or, uh, His Dudeness, or uh, Duder, or El Duderino if you're not into the whole brevity thing."
        ,9:"You want a toe? I can get you a toe, believe me."
        ,10:"That rug really tied the room together."
        ,11:"Say what you will about the tenants of National Socialism, Dude, at least its an ethos."
        ,12:"The Dude abides."
        ,13:"Hey, this is a private residence man."
        ,14:"Obviously you're not a golfer."
        ,15:"Am I the only one who gives a shit about the rules?!"
        ,16:"The Chinaman is not the issue here... also Dude, 'Asian-American' please."
        ,17:"This will not stand, ya know, this aggression will not stand, man."
        ,18:"Walter, I love you, but sooner or later you're going to have to face the fact you're a goddamn moron."
        ,19:"Lady, I got buddies who died face down in the muck so that you and I could enjoy this family restaurant!"
        ,20:"This is a very complicated case, Maude. You know, a lotta ins, a lotta outs, a lotta what-have-yous. And, uh, a lotta strands to keep in my head, man. Lotta strands in old Duder's head."
        }

while 1:
  s = random.randint(1620,2880)
  def quote():
    x = random.randint(1,len(quotes))
    m = quotes[x]
    return m

  sc.chat_postMessage(
    channel="#lower_bowl", text=quote(), username='bot lebowski', icon_emoji=':sunglasses:'
    )
  time.sleep(s)
