
def autherName(BookName):
    return "//table[@name='BookTable']/tbody/tr/td[text()='"+BookName+"']/../td[2]"

def SubjectName(BookName):
    return "//table[@name='BookTable']/tbody/tr/td[text()='"+BookName+"']/../td[3]"


def Pricing(BookName):
    return "//table[@name='BookTable']/tbody/tr/td[text()='"+BookName+"']/../td[4]"


def intellipathfootersection(para , sublinks):
    return "//p[text()='"+para+"']/../div/ul/li/a[contains(.,'"+sublinks+"')]"