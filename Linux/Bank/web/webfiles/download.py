import wget

my_file  = open("filenames_to_download.txt", "r")

data = my_file.read()

data_into_list = data.split("\n")

# print(data_into_list)
my_file.close()


for i in data_into_list:
	url = 'http://bank.htb/balance-transfer/'+ i
	wget.download(url)

