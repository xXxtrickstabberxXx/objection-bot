import requests
import json
import time
class Lawyer:
    def __init__(self,group_id,my_token):
        self.name=None
        self.group_id=group_id
        self.my_token=my_token
        self.sayings={}
    def SetSaying(self,num):
        p = requests.get("https://api.vk.com/method/docs.getUploadServer?access_token="+self.my_token+"&group_id="+self.group_id+"&type=audio_message&v=5.103").json()
        print(p)
        time.sleep(1)
        upload_url=p['response']['upload_url']
        name_file="sounds/"+self.name+"_"+str(num)+".mp3"
        upload_files = {'file': (name_file, open(name_file, 'rb'))}
        response = requests.post(upload_url, files=upload_files)
        time.sleep(1)
        file=response.json()["file"]
        p = requests.get("https://api.vk.com/method/docs.save?file="+file+"&access_token="+self.my_token+"&v=5.103").json()
        print(p)
        time.sleep(1)
        try:
            p=p['response']['audio_message']
        except KeyError:
            captcha_sid=p['error']['captcha_sid']
            captcha_img=p['error']['captcha_img']
            print(captcha_img)
            captcha_key=str(input())
            p = requests.get("https://api.vk.com/method/docs.save?file="+file+"&access_token="+self.my_token+"&captcha_sid="+str(captcha_sid)+"&captcha_key="+captcha_key+"&v=5.103").json()
            p=p['response']['audio_message'] 
        media_id=str(p["id"])
        self.sayings[num]=media_id
class PhoenixWright(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='pw'
        for i in range(4):
            Lawyer.SetSaying(self,i)
class MilesEdgeworth(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='me'
        for i in range(4):
            Lawyer.SetSaying(self,i)
class WinstonPayne(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='wp'
        Lawyer.SetSaying(self,0)
class ManfredVonKarma(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='mk'
        Lawyer.SetSaying(self,0)
class FranziskaVonKarma(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='fk'
        Lawyer.SetSaying(self,0)
class MiaFey(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='mf'
        for i in range(3):
            Lawyer.SetSaying(self,i)
class Godot(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='da'
        Lawyer.SetSaying(self,0)
class ApolloJustice(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='aj'
        for i in range(4):
            Lawyer.SetSaying(self,i)
class KristophGavin(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='kr'
        Lawyer.SetSaying(self,0)
class KlavierGavin(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='kl'
        Lawyer.SetSaying(self,0)
class JacquesPortsman(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='jp'
        Lawyer.SetSaying(self,0)
class ShiLongLang(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='sl'
        Lawyer.SetSaying(self,0)
class CalistoYew(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='cy'
        Lawyer.SetSaying(self,0)
class QuercusAlba(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='qa'
        Lawyer.SetSaying(self,0)
class HershelLayton(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='hl'
        for i in range(2):
            Lawyer.SetSaying(self,i)
class AthenaCykes(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='ac'
        for i in range(3):
            Lawyer.SetSaying(self,i)
class ZachariasBarnham(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='zb'
        Lawyer.SetSaying(self,0)
class Darklaw(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='dk'
        Lawyer.SetSaying(self,0)
class GaspenPayne(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='gp'
        Lawyer.SetSaying(self,0)
class SimonBlackquill(Lawyer):
    def __init__(self,group_id,my_token):
        Lawyer.__init__(self,group_id,my_token)
        self.name='sb'
        Lawyer.SetSaying(self,0)
