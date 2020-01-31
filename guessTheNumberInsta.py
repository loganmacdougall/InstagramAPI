import InstagramAPI
from time import sleep
from Info import InstagramPW as pw
from Info import InstagramUsername as usr

num = 12

Insta = InstagramAPI.Instagram(usr,pw)
Insta.openMyPost(1)

while(True):
    Insta.Refresh()
    sleep(4)
    Insta.loadComments()
    unrepliedComments = Insta.getCommentsWithoutReply()
    if bool(unrepliedComments) == False:
        print("No unreplied comments")
        continue
    i = unrepliedComments[0]
    print("i:",i,"& comment:",Insta.getTextCommentOfIndex(i))
    Insta.clickReplyButton(i)
    try:
        guess = int(Insta.getTextCommentOfIndex(i))
    except:
        Insta.textToPost("I'm sorry, this comment wasn't reconized as a whole number")
        sleep(30)
        continue
    if guess > num:
        Insta.textToPost("Guess lower (in a new comment, don't reply to this one)")
    elif guess < num:
        Insta.textToPost("Guess higher (in a new comment, don't reply to this one)")
    else:
        Insta.textToPost("That's it! You got the correct number!")
    sleep(30)

