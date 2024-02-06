from selenium.webdriver import Chrome

class Pat_informed:
     def __init__(self, driver):
          self.driver = driver
          
     def search_textfield(self,data):
          self.driver.find_element("xpath","//input[@class='searchField']").send_keys(data)
          
     def alert(self):
          self.driver.find_element("xpath","//button[@class='green']").click()
          
     def patents(self):
          self.driver.find_element("xpath","(//div[contains(.,'MACROCYCLIC ANALOGS')])[3]").click()
          
     def jurisdiction(self):
          jurisdiction = self.driver.find_element("xpath","(//td[@_ngcontent-ng-c4035860033])[2]")
          print(jurisdiction.text)
          
     def publication_date(self):
          publication_date = self.driver.find_element("xpath","(//td[@_ngcontent-ng-c4035860033])[6]")
          a = publication_date.text
          return a.split()
     
     def filing_date(self):
          filing_date = self.driver.find_element("xpath","(//span[@_ngcontent-ng-c4035860033])[9]")
          b = filing_date.text
          return b.split()
