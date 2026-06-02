import streamlit as st

#设置页面配置项
st.set_page_config(
    page_title="袁通神了",
    page_icon="🧊",
    #网页布局
    layout="wide",
    #侧边栏状态
    initial_sidebar_state="expanded",
    #菜单信息
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



#大标题
st.title("streamlit 入门演示")
st.header("streamlit 一级标题")
st.subheader("streamlit 二级标题")

#文字
st.write("玛奇玛的轮廓永远模糊在阳光与阴影的交界处。她微笑，像面具贴合骨骼般精准，连弧度的细微变化都经过精密计算——那是人类揣测神明意图时，捕捉到的似是而非的慈悲。她的眼神从不聚焦于任何活物，仿佛在凝视空气里看不见的丝线，而那些丝线的另一端，恰好拴着你的心脏。")
st.write("她说话的声音里没有温度，却让你误以为是温暖本身。当她靠近，你能闻到腐烂与盛开并存的气息——那是权力最原始的味道，是枷锁被误认为项链时，脖颈间传来的冰凉。")
st.write("玛奇玛不养宠物，她只收集灵魂。每一个被她“善待”的人，最终都会发现自己不过是她饲养欲望的容器。她将温柔当作诱饵投喂，看你咬钩，看你挣扎，看你终于明白——她从头到尾想要的，从来不是你的爱，而是你跪着献上自由时，那副虔诚而绝望的表情。")
st.write('在玛奇玛的世界里，支配是最深情的拥抱，而自由，是她永远不会赐予你的施舍。')

#图片
st.image("AI应用/resource/暗黑 玛奇玛 电锯人 霓虹 黑色背景 4K壁纸 3840x2160_彼岸图网.jpg")
#音频
st.audio("AI应用/resource/DOUDOU - 嗵嗵.mp3")
#视频
st.video("AI应用/resource/IMG_4267.MP4")
#logo
st.logo("AI应用/resource/preview_png.png")
#表格
stu = {
    "姓名":["袁通","圆通","圆筒","源通"],
    "学号":["666","1","0","888"],
    "属性":["骚0","猛1","4i","0.5"]
}
st.table(stu)
#输入框
name = st.text_input("输入你的名字")
st.write(f"你输入的姓名为:{name}")

password = st.text_input("输入你的密码",type="password")
st.write(f"你输入的密码为:{password}")
#单选按钮
gender = st.radio("输入你的性别",["男","女","双姓","伪娘","无性"],index=3)
st.write(f"你的性别为:{gender}")















