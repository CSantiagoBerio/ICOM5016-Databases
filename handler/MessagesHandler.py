from flask import *
from dao.MessagesDAO import *


class MessagesHandler:
    def arrange(self, row):
        messages = {}
        messages['Message ID'] = row[0]
        messages['Group ID'] = row[1]
        messages['User ID'] = row[2]
        messages['Date sent'] = row[3]
        messages['Message Content'] = row[4]
        return messages

    def arrangeJoin(self, row):
        messages = {}
        messages['First Name'] = row[0]
        messages['Last Name'] = row[1]
        messages['Text'] = row[2]
        return messages

    def arrangebeta(self, row):
        contents={}
        #contents['Group ID'] = row[0]
        #contents['User ID'] = row[1]
        contents['First Name'] = row[2]
        contents['Last Name'] = row[3]
        contents['Phone'] = row[4]
        contents['E-mail'] = row[5]
        #contents['Username'] = row[6]
        #contents['Message ID'] = row[8]
        contents['Likes'] = row[9]
        contents['Group Name'] = row[10]
        #contents['Date Created'] = row[12]
        return contents

    def arrangelike(self, row):
        likes = {}
        likes['#ofLikes'] = row[0]
        return likes

    def arrangedislike(self, row):
        likes = {}
        likes['#ofDislikes'] = row[0]
        return likes

    def arrangelikesbeta(self, row):
        contents={}
        contents['Message'] = row[0]
        contents['likes'] = row[1]
        contents['dislikes'] = row[2]
        return contents

    def arrangereactions(self, row):
        reactions = {}
        reactions['Likes'] = row[0][0]
        reactions['Dislikes'] = row[0][1]
        return reactions

    # def arrangeMessageID(self, row):
    #     message = {}
    #     message['message_id'] = row[0]
    #     return message
    #
    # def arrangeMessageSenderID(self, row):
    #     message = {}
    #     message['sender_id'] = row[1]
    #     return message
    #
    # def arrangeMessageGroupID(self, row):
    #     message = {}
    #     message['group_id'] = row[2]
    #     return message
    #
    # def arrangeMessageDateSent(self, row):
    #     message = {}
    #     message['date_sent'] = row[3]
    #     return message
    #
    # def arrangeMessageSenderID(self, row):
    #     message = {}
    #     message['message_content'] = row[4]
    #     return message

    def getMessages(self):
        dao = MessagesDAO()
        result = dao.getMessages()
        message = []
        for i in result:
            message.append(self.arrange(i))
        return jsonify(Messages=message)

    def getUserMessagesById(self, usrid):
        dao = MessagesDAO()
        result = dao.getUserMessagebyId(usrid)
        message = []
        if result:
            for m in result:
                message.append(self.arrangeJoin(m))
            return jsonify(Messages=message)
        return jsonify(ERROR='No messages from that User')

    def getMessageLikes(self,name, mid):
        dao = MessagesDAO()
        result = dao.getMessageLikes(name, mid)
        res = []
        if result:
            for r in result:
                res.append(self.arrangebeta(r))
            return jsonify(Message=res)
        return jsonify(ERROR='No one has liked this message')

    def getMessageDislikes(self, gid, mid):
        dao = MessagesDAO()
        result = dao.getMessageDislikes(gid, mid)
        res = []
        if result:
            for r in result:
                res.append(self.arrangebeta(r))
            return jsonify(Message=res)
        return jsonify(ERROR='No one has disliked this message')

    def getMessageReplies(self, gid, mid):
        dao = MessagesDAO()
        result = dao.getMessageReplies(gid, mid)
        res = []
        if result:
            for r in result:
                res.append(self.arrangebeta(r))
            return jsonify(Replies=res)
        return jsonify(ERROR='No replies for that message')

    def getNumberOfLikes(self, mid):
        dao = MessagesDAO()
        result = dao.getNumberOfLikes(mid)
        if result:
            res = self.arrangelike(result)
            return jsonify(Message_Likes=res)
        return jsonify(ERROR='0 Likes')

    def getNumberOfDislikes(self, mid):
        dao = MessagesDAO()
        result = dao.getNumberOfDislikes(mid)
        if result:
            res = self.arrangedislike(result)
            return jsonify(Message_Disikes=res)
        return jsonify(ERROR='0 Likes')

    def getReactions(self, mid):
        dao = MessagesDAO()
        result = dao.getReactions(mid)
        if result:
            res = self.arrangereactions(result)
            return jsonify(Reactions=res)
        return jsonify(ERROR='0 Reactions')


    def getHashtags(self):
        dao = MessagesDAO()
        result = dao.getHashtags()
        return jsonify(Hashtags=result)
