import webbrowser
import time
# import sleep

# t1 = datetime.datetime.now()

# other stuff here
# t2 = datetime.datetime.now()
# delta = t2 - t1
new = 2
url = "https://www.google.com.au/url?sa=t&rct=j&q=&esrc=s&source=video&cd=7&cad=rja&uact=8&ved=0ahUKEwjM9J3txprOAhWFI5QKHbIVDNQQtwIIMDAG&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DD_ksYVM2cWY&usg=AFQjCNFmoTk2G33l_Ck51-c6h10YZ9bFmg&sig2=amJwdaDoO5_i5yd8otK3uQ&bvm=bv.128617741,d.dGo"
url_direct = "https://www.youtube.com/watch?v=D_ksYVM2cWY"

time.sleep(10)
webbrowser.open(url_direct,new=2)

# if delta.seconds >= 2000:
    # do stuff
    # webbrowser.open(url_direct,new=2)
# else:
    # sleep for a bit