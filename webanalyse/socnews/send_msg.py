import itchat


def send_msg(f):

	itchat.auto_login()
	itchat.send("@fil@%s"%f)
	itchat.logout()

if __name__=="__main__":
	f = "index.html"
	send_msg(f)
