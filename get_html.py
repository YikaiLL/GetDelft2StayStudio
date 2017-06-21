import urllib
from lxml import html
from urllib.request import urlopen
from lxml import etree
import time
import json
from collections import defaultdict
from send_email import send_email
# from open_html import fill_input

def rec_dd():
    return defaultdict(rec_dd)
def split_space(s):
    return "".join(s.split())
def is_two_dict_different(dict1,dict2):
    if len(dict1)==len(dict2):
        for key in dict1:
            if key not in dict2:
                return True
            elif dict2[key]['house_available_date'] != dict1[key]['house_available_date']:
                return True
        return False

    return True

url = "https://delft2stay.nl/book-apartment.html"


time_sleep_second=15

while(True):
    try:
        with open('house_list.json') as data_file:
            house_list_from_file= json.load(data_file)
        print('Dict Length: ',len(house_list_from_file))
        first_dict_length=len(house_list_from_file)
    except:
        house_list_from_file={}
        pass

    

    current_time_string=time.ctime()
    print(current_time_string)
    try:
        html_page =urlopen(url).read()
        page = html.fromstring(html_page)
    except urllib.error.URLError as e:
        print(e)
        pass
        time.sleep(time_sleep_second)  
        continue
    
    # doc=urlopen(url).read()
    # ul_product_grid=page[2][0][1][2][0][0][0][2][3][1]

    try:
        ul_product_grid=page[2][0][1][2][0][0][0][2][3][1]
    except:
        print('No House Available')
        # time.sleep(3)  
        ul_product_grid=[]
        

    for count in range(0,len(ul_product_grid)):
        print('Housing list length:\t',len(ul_product_grid))
    if(len(ul_product_grid)>=1):
        print('We got house!!!!!!!')






    house_dict_result=rec_dd()
    for house_id in range(0,len(ul_product_grid)):
        house_name=ul_product_grid[house_id][1][0].text
        house_detail=ul_product_grid[house_id][3]
        house_price=split_space(house_detail[1].text).split(':')[1]
        house_available_date=split_space(house_detail[1].tail).split(':')[1]
        house_area=split_space(house_detail[2].tail).split(':')[1]
        house_floor=split_space(house_detail[4].tail).split('|')[1]
        house_type=split_space(house_detail[3].tail)
        url_link=ul_product_grid[house_id][4][0].get('onclick').split('\'')[1]
        house_dict_result[house_name]['house_name']=house_name
        house_dict_result[house_name]['house_price']=house_price
        house_dict_result[house_name]['house_available_date']=house_available_date
        house_dict_result[house_name]['house_area']=house_area
        house_dict_result[house_name]['house_floor']=house_floor
        house_dict_result[house_name]['url_link']=url_link
        
        print('Room:\t',house_name,'\nPrice:\t',house_price)
        print('Available:',house_available_date)
        print('Area:\t',house_area)
        print('Floor:\t',house_floor)
        print('Link:\t',url_link)

        if house_available_date.split('-')[1]=='06':
            print('June!!!')
        elif house_available_date.split('-')[1]=='07':
            print('July!!!')
        elif house_available_date.split('-')[1]=='08':
            print('August!!!!!')
        else:
            print('Wonderful, Even later!!!!!!')
        print('*****')
        # End of For
    # break
    if len(house_list_from_file)!=len(house_dict_result) or is_two_dict_different(house_list_from_file,house_dict_result):
        send_email(house_dict_result,current_time_string)
        with open('house_list.json', 'w') as fp:
            fp.write(json.dumps(house_dict_result,indent=4)) 
        print('Rewrite json file')
        # Call function
        # fill_input('')

    time.sleep(time_sleep_second)  
    print('------------------------')






# For test


 # print(ul_product_grid[house_id])
        # print(ul_product_grid[house_id].text,ul_product_grid[house_id].tail)
        # index=0
        # for child in ul_product_grid[house_id][4]:
        #     print(index)
        #     print(child.text,child.get('class'),len(child))
        #     print(child.tail,child.get('onclick'),child.text_content)
        #     index+=1
