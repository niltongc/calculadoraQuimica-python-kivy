from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Pressao(Screen):
    pass

    #1Pam3 = 1J
    #5/9 * K
    def pcalc(self):
        try:
            ptin = float(self.ids.ptin.text)
            ptit = float(self.ids.ptit.text)
            ptiv = float(self.ids.ptiv.text)

            ptbm = (self.ids.ptbm.state == 'down')
            ptbmm = (self.ids.ptbmm.state == 'down')
            ptbk = (self.ids.ptbk.state == 'down')
            ptbc = (self.ids.ptbc.state == 'down')
            ptbf = (self.ids.ptbf.state == 'down')
            ptbl = (self.ids.ptbl.state == 'down')
            ptbm3 = (self.ids.ptbm3.state == 'down')        
            
            if ptbm and ptbk and ptbl:
                self.ids.plr.text = ( str((ptin*8.314*ptit)/(ptiv*0.001))+str(' Pa = ')+str(((ptin*8.314*ptit)/(ptiv*0.001)/100000))+
                                      str(' bar = ')+str(((ptin*8.314*ptit)/(ptiv*0.001))/101325)+str(' atm = ')+
                                      str(((ptin*8.314*ptit)/(ptiv*0.001))/(101325/760))+str(' torr') ) 
            elif ptbm and ptbk and ptbm3:
                self.ids.plr.text = ( str((ptin*8.314*ptit)/ptiv)+str(' Pa = ')+str(((ptin*8.314*ptit)/ptiv)/100000)+
                str(' bar = ')+str(((ptin*8.314*ptit)/ptiv)/101325)+str(' atm = ')+str(((ptin*8.314*ptit)/ptiv)/(101325/760))+
                str(' torr') )
            elif ptbm and ptbc and ptbl:
                self.ids.plr.text = ( str((ptin*8.314*(ptit+273.16))/(ptiv*0.001))+str(' Pa = ')+str(((ptin*8.314*(ptit+273.16))/(ptiv*0.001))/100000)+
                                      str(' bar = ')+str(((ptin*8.314*(ptit+273.16))/(ptiv*0.001))/101325)+str(' atm =')+
                                      str(((ptin*8.314*(ptit+273.16))/(ptiv*0.001))/(101325/760))+str(' torr')  )
            elif ptbm and ptbc and ptbm3:
                self.ids.plr.text = str((ptin*8.314*(ptit+273.16))/ptiv)+str(' Pa')
            elif ptbm and ptbf and ptbl:
                self.ids.plr.text = str((ptin*8.314*((ptit+459.688)*5/9) )/(ptiv*(0.001)))+str(' Pa')
            elif ptbm and ptbf and ptbm3:
                self.ids.plr.text = str((ptin*8.314*((ptit+459.688)*5/9) )/ptiv)+str(' Pa')
                
            elif ptbmm and ptbk and ptbl:
                self.ids.plr.text = str((ptin*0.001*8.314*ptit)/(ptiv*(0.001)))+str(' Pa')
            elif ptbmm and ptbk and ptbm3:
                self.ids.plr.text = str((ptin*0.001*8.314*ptit)/ptiv)+str('Pa')
            elif ptbmm and ptbc and ptbl:
                self.ids.plr.text = str((ptin*0.001*8.314*(ptit+273.16))/(ptiv*(0.001)))+str(' Pa')
            elif ptbmm and ptbc and ptbm3:
                self.ids.plr.text = str((ptin*0.001*8.314*(ptit+273.16))/ptiv)+str(' Pa')
            elif ptbmm and ptbf and ptbl:
                self.ids.plr.text = str((ptin*0.001*8.314*((ptit+459.688)*5/9) )/(ptiv*(0.001)))+str(' Pa')
            elif ptbmm and ptbf and ptbm3:
                self.ids.plr.text = str((ptin*0.001*8.314*((ptit+459.688)*5/9) )/ptiv)+str(' Pa')
        except:
            self.ids.plr.text = 'error'
        
        
class Calculadora(App):
    def build(self):
        return Gerenciador()

Calculadora().run()
