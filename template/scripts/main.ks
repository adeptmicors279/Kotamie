//注释的定义为双斜杠

//*
*start
//标识，标记为可跳转路径
//每个跳转标识不可重名且只能定义一次

//@
@YukuNya: hello!
//@后面加角色名，冒号（半角）后跟语句

//sound
sound xxxx.mp3
//播放音频


//:
: 没有角色的旁白
//以冒号开头则自动忽略角色

//bg
bg classroom.png
//bg后面跟想要切换到的图片


//show
show YukuNya Nya.png left
show YukuNya happy.png
show YukuNya happy.png at 100 100
show YukuNya happy.png center offset -30 0
//show+角色名称+状态+位置+动作
//顺序不能乱
//assets文件目录格式应该如下
//assets
//  - YukuNya
//    - Nya_xxx.png
//    - sad_xxxx.png
//调用时则写成show YukuNya sad_xxxx.png left  例如
show YukuNya sad_1.png left
@YukuNya: 呜呜呜T_T
//同时，你也可以将assets文件夹建立成这样
//assets
//  - sad
//    - sad_xxxx1.png
//    - sad_xxxx2.png
//  -happy
//    - happy_xxxx.png
//这种写法要求子文件夹内部的文件开头需要以父文件夹名称开头并在_后加入文件名
show YukuNya sad_xxxx1.ong center
//引擎会自动读取_之前的内容作为父文件夹的路径，并且以此文件名来寻找文件
//两种储存结构不可混用
//关于定位，引擎提供三个锚点供选择，你可以写偏移量或者直接改坐标
show YukuNya happy_1.png center action shake
//默认只有shake这个动画
//可以去action.py修改与添加


//jump
@YukuNya: 好想睡觉

jump home

*home
@YukuNya: Zzzzzzzzz~

*school
@YukuNya: ????????

//jump实现跳转
//例如YukuNya想睡觉了，jump到对应的板块



//choice
? 你要做什么
- 去教室 -> class
- 回家 -> home

*class
bg classroom_scene
@YukuNya: 上课了？
//以?开头进行选择
//选项对应的文字会出现在选择框
//?后的文字会在对话框显示
//执行的是跳转功能
//选项要以-打头
//中间不可插入其他语句


//变量
//MP = 100
//定义MP为100
//new_MP = MP - 10
//可以进行运算
//支持Python支持的运算符号
//可以进行简单的判断操作
//仍未支持
jump happy_end
*happy_end
@YukuNya: 假装这是好结局
END
*bad_end
@YukuNya: 假装这是坏结局
END
//END是游戏终止的标识
//必须在选择的分支后面写上，否则会导致游戏读取接下来的分支从而无法结束游戏
