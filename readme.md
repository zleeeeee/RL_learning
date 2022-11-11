mkdir demo
cd demo
echo "# demo" >> README.md
git init //把这个目录变成Git可以管理的仓库
git add README.md //文件添加到仓库
git add . //不但可以跟单一文件，还可以跟通配符，更可以跟目录。一个点就把当前目录下所有未追踪的文件全部add了（空目录不会被添加）
git status //查看当前工作区的状态（需提交的变更）
git commit -m "first commit" //把文件提交到仓库
git remote add origin https://github.com/zleeeeee/RL_learning.git//关联远程仓库
git push -u origin master //将本地主分支推到远程(如无远程主分支则创建，用于初始化远程仓库)
git push origin master //将本地主分支推到远程主分支
————————————————
版权声明：本文为CSDN博主「疯跑蜗牛」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/hxf0663/article/details/79527453
