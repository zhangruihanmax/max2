'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页',['我的旅行','我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区','我的快捷网站'])

def page_1():
    st.write('我的旅行')
    st.write('我在各种假期中可没闲着，而是在各地留下自己的足迹，如果你也喜欢游览名胜古迹、到网红点打卡、亲近大自然……那么就来看看我的丰富流程，参考一下吧！')
    st.write('')
    
    st.image('北京环球影城.jpg')
    st.write('去北京环球影城')
    st.write('这是在环球影城(一个项目排队两个小时的游乐园)里面项目玩起来都可以,等待的时间太长。我玩了霸天虎过山车,太好玩了，这辈子也不想玩了……')
    st.write('---------------------------------------------------------------')
    
    st.image('大同应县木塔.jpg')
    st.write('去大同应县木塔')
    st.write('应县木塔与意大利比萨斜塔、巴黎埃菲尔铁塔并称“世界三大奇塔，挺壮观的，就是只能干看着，有点无聊~')
    st.write('---------------------------------------------------------------')
    
    st.image('北京科技馆.jpg')
    st.write('去中国科学技术馆')
    st.write('中国科技馆，外形就像一个巨型魔方，位于北京的国家奥林匹克公园中心区内。里面特别科技，知识很多，但是我啥也没记住！')
    st.write('---------------------------------------------------------------')
    
    st.image('天津之眼.jpg')
    st.write('去天津之眼')
    st.write('是世界上唯一建在桥上的摩天轮，是天津的地标之一。到达最高处时，周边景色一览无余，甚至能看到方圆40公里以内的景致，被誉为"天津之眼"')

def page_2():
    '''我的兴趣推荐'''
    with open('西部风情.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time = 0)
    st.image('马里喵1.gif')
    st.write('我的游戏推荐')
    st.image('火影忍者.png')
    st.write('《火影忍者》，《王者荣耀》.....')
    st.write('-----------------------')
    st.write('我的书籍推荐')
    st.write('《水浒传》，《三国演义》.....')
    st.write('-----------------------')
    st.image('马里喵2.gif')
    
def page_3():
    '''我的图片处理工具'''
    st.write(':sunglasses:图片处理小程序:sunglasses:')
    uploaded_file = st.file_uploader('上传图片', type=['png','jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        #st.image(img)
        #st.image(img_change(img,0,2,1))

        tab1,tab2,tab3,tab4=st.tabs(["原色","改色1","改色2","改色3",])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))    
def page_4():
    '''我的智能词典'''
    st.write('智能词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
        
    with open('check_out_times.txt','r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
        
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8')as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数:', times_dict[n]) 
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
        if word == 'snow' or word == 'winter':
            st.snow()
        if word == 'birthday':
            st.balloons()
            
def page_5():
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r', encoding='utf-8') as f:
        message_list = f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i] = message_list[i].split('#')
    for i in message_list:
        if i[1] == '阿短':
            with st.chat_message('👽'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('😼'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是......',['阿短','编程猫'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in message_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page_6():
    '''我的快捷网站'''
    st.write('我的快捷网站')
    st.link_button('百度首页', 'https://www.baidu.com/')
    st.write('-----------------------')
    st.link_button('知乎', 'https://www.zhihu.com/')
    st.write('-----------------------')
    st.link_button('微博', 'https://weibo.com/')
    st.write('-----------------------')
    st.link_button('bilibili', 'https://www.bilibili.com/')
    st.write('-----------------------')
    st.link_button('爱奇艺', 'https://www.iqiyi.com/')
    st.write('-----------------------')
    st.link_button('网易云音乐', 'https://music.163.com/')
    st.write('-----------------------')

def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGP值
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img   

if page == '我的旅行':
    page_1()
elif page == '我的兴趣推荐':
    page_2()
elif page == '我的图片处理工具':
    page_3()
elif page == '我的智慧词典':
    page_4()
elif page == '我的留言区':
    page_5()
elif page == '我的快捷网站':
    page_6()