from utils import *
import time

countries = get_country_codes('countrycode.txt')
# print(countries)

# url1 = 'https://www.google.com/search?q=filetype:pdf+site:%s&start='
# url = url1 %countries[0] + str(0)
# get_html(url,0)

#get html part------------------------
filenum = 2176
url1 = 'https://www.google.com/search?q=filetype:pdf+site:%s&start='
start = filenum//10
for i in range(start,len(countries)):
    for page_num in range(10):
        url = url1 %countries[i] + str(page_num*10)
        get_html(url,filenum)
        filenum += 1


#get pdf url part------------------------------
# htmlname = 'pages/page%d.html'

# start_num = 1800
# for i in range(start_num,2175):
#     html_path = htmlname%i
#     try:
#         res = fetch_pdfurl(html_path)
#         generate_txt(res,'pdfurlfinal.txt')
#     except:
#         pass

# caculate throughput------------------------------
# with open('pdfurlfinal.txt','r') as f:
#     pdfurl = f.readlines()
# pdfurl_total_len = len(pdfurl)
# for i in range(pdfurl_total_len):
#     pdfurl[i] = pdfurl[i].strip()

# #start to end#####################
# index = 12243
# end = 16380
# for i in range(index,end):
#     print(round((i-index)*100/(end-index),3),'%')
#     try:
#         t = download_pdf(pdfurl[i],i)
#         t = round(t,2)
#         if t:
#             print('tp:',t)
#             with open('tp.txt','a+') as f:
#                 f.write(str(i)+','+pdfurl[i]+','+str(t)+'\n')
#     except:
#         pass


# generate ip,tp file---------------------------
# with open('tp.txt','r') as f:
#     data = f.readlines()

# start_index = 10000
# end_index = 12838
# ip = []
# tp = []
# for row_num in range(start_index,end_index):
#     print('now row_num:',row_num)
#     try:
#         e = data[row_num].split(',')
#         i = url_to_ip(e[1])
#         t = float(e[2].strip())
#     except:
#         continue
#     if i not in ip:
#         ip.append(i)
#         tp.append(t)
#     else:
#         ip_index = ip.index(i)
        
#         tp[ip_index] = max(tp[ip_index],t)
#     # print(t)
# for j in range(len(ip)):
#     with open('iptp.txt','a+') as f:
#         try:
#             f.write(str(ip[j])+','+str(tp[j])+'\n')
#         except:
#             pass




