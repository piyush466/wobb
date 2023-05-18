import time

from Page_Object.Loginpage import Login
from Utilities.log_generation import LogGen


class Test_001:
     email = "piyushdravyakar46@gmail.com"
     password = 'Piyush@123'
     campion = 'piyush'

     logger = LogGen.logger()

     def test_firstlogin(self,setup):
          self.driver = setup
          self.logger.info("*******Test Started*******")
          self.driver.get("https://stage.wobb.ai/auth/login")
          self.lp = Login(self.driver)
          self.lp.setemail(self.email)
          self.logger.info(f"Your email :- {self.email}")
          self.lp.clickNext()
          time.sleep(2)
          self.lp.setpassword(self.password)
          self.logger.info(f"Your password :- {self.password}")
          self.lp.clicksign_up()
          self.page_title = self.driver.title
          time.sleep(2)
          assert self.page_title == "Wobb.ai - Reach influencers easily", "Title is not match"
          self.logger.info("******Login succesfully******")

     def test_postCamption(self, setup):
          self.test_firstlogin(setup)
          self.lp.hover()
          time.sleep(2)
          self.lp.Set_Campaign_Name(self.campion)
          self.lp.dropdown_platfrom()
          time.sleep(2)
          self.lp.all_drop_down()
          self.lp.select_2nd_droplist()











