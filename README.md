# NeteaseCloudMusicPlaylistCreator
这个项目主要是在Windows上创建网易云音乐的播放列表(格式m3u)，方便导入MP3

## 使用方法：
1. 安装网易云音乐客户端
2. 登录账户，下载播放列表中所有音乐
3. 双击运行脚本
4. 将音乐文件和生成的m3u文件拷贝到你的播放器目录（前提是要你的播放器支持 m3u

## Tips：
如果你只需要在电脑中其他播放器使用 M3U 文件，可以使用绝对路径生成模式  
将参数 `-a` 设置为真，然后直接在下载目录运行脚本  
例如 -> `create_playlist.py -a True`  
也可以使用 `-p` 参数手动传递网易云音乐的歌曲下载目录位置  
例如 -> `create_playlist.py -a True -p "D:\NeteaseCloudMusicDownload"`

## 注意：
本 fork 为 Python3+ only，Python2 麻烦绕道原 repo