# SocialMap
My graduation project！
#地理社交Demo

-   前端单页面响应式设计，BackBone MVC
-   后端使用Django + Django ReST Framework 提供Api供前端调用

现在完成的功能有：
-   用户注册，登陆，完善身份信息等
-   查看修改用户信息
-   用户在前端提交一个GPS（WGS-84），服务器记录起来，作为用户的行动记录
-   前端初始化界面，从服务器上取得用户位置附近7000米圆形区域内的MarkPost（类似微博一样的东西），显示在地图上，服务器用PostgreSQl GIS引擎支持地理查询
-   用户拖动地图，自动判断这里没有从服务器get过数据，没有就查询，显示到为地图上
-   点击信息气泡，显示Post的信息
-   点击用户，显示用户信息，可以点击关注，不看他
-   用户间Message互发

#Introduction
……

#Requirement
- Nginx
- uWSGI
- Python
- Npm

#How to Start
-   cd FRONT && bower install && npm install
-   cd Server && (With virtualenv and pip install requirement.txt)

#Demo
-   you can see the DemoPic directory

#Todo
-   Security
-   Web Socket
