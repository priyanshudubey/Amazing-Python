#Priyanshu Dubey
#8/10/2020
#Internet speed checker: It will result you your internet speed

#install the important library first
# pip install speedtest-cli

import speedtest as sp

test = sp.Speedtest()
downloading = test.download()
uploading = test.upload()

print("Downloading speed is: ")
print(downloading)
print("Uploading speed is: ")
(uploading)
