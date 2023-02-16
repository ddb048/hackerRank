# NOTE - Spam Detection

# implement a prototype of an email spam detection algorithm.


def getSpamEmails(subjects, spam_words):

    returnList = []

    spam_words = [i.lower() for i in spam_words]

    for email in subjects:

        emailList = email.lower().split()

        s1 = 0

        for word in emailList:
            if word in spam_words:
                s1 += 1

        if s1 >= 2:
            returnList.append('spam')
        else:
            returnList.append('not_spam')

    return returnList
