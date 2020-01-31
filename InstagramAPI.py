#openMyPost(post)
#openUsersPost(account,post)
#Refresh()
#loadComments()
#getFullComments()
#getTextComments()
#getTextCommentOfIndex(index)
#clickReplyButton(index)
#commentHasReply(index)
#getCommentsWithoutReply()
#getCommentsWithReply()
#getCommentsWithoutReply()
#textToPost(text)
#getCommentOfNumber(num)
#getCommentEqualTo(comment)

#/\ List of possible commands /\

from selenium import webdriver
from time import sleep

class Instagram:
    def __init__(self, usr, pw): #opens insta and logs you in
        self.driver = webdriver.Chrome("C:\Program Files\ExternalPATH\chromedriver.exe")
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(usr)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(2)
    def openMyPost(self,post): #opens a specific post which you have posted
        mainPageSVGs = self.driver.find_elements_by_class_name("_8-yf5")
        mainPageSVGs[len(mainPageSVGs)-1].click()
        sleep(2)
        self.driver.find_elements_by_class_name("_9AhH0")[post].click()
        sleep(6)
    def openUsersPost(self,account,post): #opens a specific post which another user has posted
        self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]").send_keys(account)
        sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div").click()
        sleep(2)
        self.driver.find_elements_by_class_name("_9AhH0")[post].click()
        sleep(6)
    def Refresh(self): #refreshes the page
        self.driver.refresh()
    def loadComments(self): #loads in all the comments (take a long time depending on the number of comments)
        try:
            self.driver.find_element_by_class_name("glyphsSpriteCircle_add__outline__24__grey_9").click()
        except:
            return
        sleep(4)
        self.loadComments()
    def getFullComments(self): #returns the html of all the comments
        return self.driver.find_elements_by_class_name("Mr508")
    def getTextComments(self): #returns the text of all the comments
        comments = self.getFullComments()
        comText = []
        for i in range(0,len(comments)):
            comText.insert(-1, comments[i].get_attribute("innerText").split("\n")[1])
        return comText
    def getTextCommentOfIndex(self,index):
        return self.getFullComments()[index].get_attribute("innerText").split("\n")[1]
    def clickReplyButton(self,index): #clicks the reply button of whatever comment index specified
        self.driver.execute_script("var b = document.getElementsByClassName(\"_7UhW9\")["+str(index+1)+"].querySelectorAll(\"button\");\nb[b.length-1].click()")
    def commentHasReply(self,index): #checks if a comment has been repiled by anybody or not
        comments = self.getFullComments()
        commentsWithReplies = self.driver.find_elements_by_class_name("EizgU")
        for i in range(0,len(commentsWithReplies)):
            commentsWithReplies[i] = commentsWithReplies[i].find_element_by_xpath('../../../../../..')
        if comments[index] in commentsWithReplies:
            return True
        else:
            return False
    def getCommentsWithoutReply(self):
        max = len(self.getFullComments())
        NoReply = []
        for i in range(0,max):
            if self.commentHasReply(i) == False:
                NoReply.append(i)
        return NoReply
    def getCommentsWithReply(self):
        max = len(self.getFullComments())
        NoReply = []
        for i in range(0,max):
            if self.commentHasReply(i) == True:
                NoReply.append(i)
        return NoReply
    def textToPost(self,text): #takes a string as input and posts it as a comment
        self.driver.find_element_by_class_name("Ypffh").send_keys(text)
        index = len(self.driver.find_elements_by_class_name("y3zKF")) - 1
        self.driver.find_elements_by_class_name("y3zKF")[index].click()
    def getCommentEqualTo(self,comment): #returns me the first comment that posted the number 'num'
        comments = self.getTextComments()
        i = 0
        while(i < len(comments)):
            if comments[i] == str(comment):
                return [i,comments[i]]
            i+=1
        return None
    def getCommentOfNumber(self,num): #returns me the first comment that posted the number 'num'
        comments = self.getTextComments()
        i = 0
        while(True):
            try:
                numInt = int(comments[i])
            except:
                if i >= len(comments):
                    return None
                i+=1
                continue
            if numInt == num:
                return [i,comments[i]]
            i+=1