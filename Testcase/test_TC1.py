from Generic.Pat_Informed import *
from datetime import datetime,date

def test_TC1(launch):
     driver = launch
     pat = Pat_informed(driver)
     pat.search_textfield('SIL')
     pat.alert()
     pat.patents()
     pat.jurisdiction()
     p_date = pat.publication_date()
     f_date = pat.filing_date()
     a = datetime.strptime(str(p_date[0]), "%Y-%m-%d")
     b = datetime.strptime(str(f_date[0]), "%Y-%m-%d")
     
     if a>b:
          print(f"Filing Date {f_date[0]} is earlier than Publication Date {p_date[0]}")
     else:
          print(f"Filing Date {f_date[0]} is later than Publication Date {p_date[0]}")