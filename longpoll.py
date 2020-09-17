import json
import requests
import random
from characters import PhoenixWright
from characters import MilesEdgeworth
from characters import WinstonPayne
from characters import ManfredVonKarma
from characters import FranziskaVonKarma
from characters import MiaFey
from characters import Godot
from characters import ApolloJustice
from characters import KristophGavin
from characters import KlavierGavin
from characters import JacquesPortsman
from characters import ShiLongLang
from characters import CalistoYew
from characters import QuercusAlba
from characters import HershelLayton
from characters import AthenaCykes
from characters import ZachariasBarnham
from characters import Darklaw
from characters import GaspenPayne
from characters import SimonBlackquill

class LongPollApi:
    def __init__(self, access_token, group_id, my_token):
        self.access_token = access_token
        self.group_id = group_id
        self.server = None
        self.key = None
        self.ts = None
        self.my_token=my_token
        self.set()
        self.pw=PhoenixWright(group_id,my_token)
        self.me=MilesEdgeworth(group_id,my_token)
        self.wp=WinstonPayne(group_id,my_token)
        self.mk=ManfredVonKarma(group_id,my_token)
        self.fk=FranziskaVonKarma(group_id,my_token)
        self.mf=MiaFey(group_id,my_token)
        self.da=Godot(group_id,my_token)
        self.aj=ApolloJustice(group_id,my_token)
        self.kr=KristophGavin(group_id,my_token)
        self.kl=KlavierGavin(group_id,my_token)
        self.jp=JacquesPortsman(group_id,my_token)
        self.sl=ShiLongLang(group_id,my_token)
        self.cy=CalistoYew(group_id,my_token)
        self.qa=QuercusAlba(group_id,my_token)
        self.hl=HershelLayton(group_id,my_token)
        self.ac=AthenaCykes(group_id,my_token)
        self.zb=ZachariasBarnham(group_id,my_token)
        self.dk=Darklaw(group_id,my_token)
        self.gp=GaspenPayne(group_id,my_token)
        self.sb=SimonBlackquill(group_id,my_token)
        self.count={'pw':3,'me':3,'wp':0,'mk':0,'fk':0,'mf':2,'da':0,'aj':3,'kr':0,'kl':0,'jp':0,'sl':0,'cy':0,'qa':0,'hl':1,'ac':3,'zb':0,'dk':0,'gp':0,'sb':0}
        self.func={'pw':self.pw.sayings,'me':self.me.sayings,'wp':self.wp.sayings,'mk':self.mk.sayings,'fk':self.fk.sayings,'mf':self.mf.sayings,'da':self.da.sayings,'aj':self.aj.sayings,'kr':self.kr.sayings,'kl':self.kl.sayings,'jp':self.jp.sayings,'sl':self.sl.sayings,'cy':self.cy.sayings,'qa':self.qa.sayings,'hl':self.hl.sayings,'ac':self.ac.sayings,'zb':self.zb.sayings,'dk':self.dk.sayings,'gp':self.gp.sayings,'sb':self.sb.sayings}
        print("init complete!")
    def set(self):
        print(self.access_token)
        r = requests.get("https://api.vk.com/method/groups.getLongPollServer?group_id="+self.group_id+"&access_token="+self.access_token+"&v=5.103").json()['response']
        print(r)
        self.server=r['server']
        self.key=r['key']
        self.ts=r['ts']
    def events(self):
            r = requests.get(self.server+"?act=a_check&key="+self.key+"&ts="+self.ts+"&wait=5").json()
            updates=r['updates']
            if updates:
                for i in updates:
                    if i['type']=='message_new':
                        obj=i['object']['message']
                        print(obj)
                        user_id=str(obj['from_id'])
                        peer_id=str(obj['peer_id'])
                        text=obj['text']
                        if (text[0]=='/') :
                            text=text[1:]
                        if len(text)==4:
                            name=text[0:2]
                            num=int(text[3])
                            if name in self.count:
                                if num<=self.count[name]:
                                    random_id=str(random.randint(-9223372036854775808,9223372036854775807))
                                    response=requests.post("https://api.vk.com/method/messages.send?peer_id="+peer_id+"&random_id="+random_id+"&attachment=doc-"+self.group_id+"_"+str(self.func[name][num])+"&access_token="+self.access_token+"&v=5.103")

                                    print(response.json())
                self.ts=r['ts']
