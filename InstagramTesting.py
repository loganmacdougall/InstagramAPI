import InstagramAPI
from time import sleep
from Info import InstagramPW as pw
from Info import InstagramUsername as usr


Insta = InstagramAPI.Instagram(usr,pw) #logs in
Insta.openMyPost(1) #opens the second (index of 1) post on my profile
Insta.loadComments() #loads all the comments in on that post

comment = Insta.getCommentEqualTo(11) #gets me the first comment which has the number n as an index and string in an array
#comment = [index of comment, text of comment]

if comment == None: #If no comments were found, print no match found
    print("No match was found")
else: # If a comment was found...
    print(comment[1]) #print the comment which was found
    Insta.clickReplyButton(comment[0]+2) #click the reply button of the index the comment was found
    Insta.textToPost("You sent me the number "+comment[1]+" and that's very cool.") #post this comment to to the person you'd like to reply to

sleep(20) #Don't close browser until 20s

