# BilibiliConcat
Concat videos downloaded by BiliBili for UWP

## 要求
需要ffmepg的支持，自行去ffmpeg官网下载安装并添加环境变量
## 功能
输入BiliBili for UWP下载的视频路径和输出路径可以自动合并各分集下的flv，并根据分集名称重命名输出。
## 目前问题
ffmpeg使用filelist的方式输入待合并视频的话，路径中需要转义反斜杠，目前用的是先把反斜杠替换成@再替换成双反斜杠的方式实现，文件名及路径中不能有冒号等奇怪字符，感觉linux下这个问题不是问题，但是win下有点麻烦。
