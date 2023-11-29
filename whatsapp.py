class version1():
    def chatting(self):
        print("text message")
class version2(version1):
    def chatting(self):
        super().chatting()
        print("voice message")
        print("images")
        print("videos")
    def call(self):
        print("audio call")
class version3(version2):
    def call(self):
        super().chatting()
        super().call()
        print("video call")
