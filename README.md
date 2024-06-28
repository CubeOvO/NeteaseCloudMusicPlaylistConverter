# NeteaseCloudMusicPlaylistCreator
将网易云音乐 PC 端的歌单转换成 M3U 格式，方便其他程序使用

## 本repo的区别：
- 优化了在遇到需要处理的歌单名的情况（处理了？，|，/，！）
- 解决了某些歌单里的歌曲为加密的.ncm格式的情况

注意，**如果歌单里有.ncm的加密后的文件，用户在下载歌单后需要先自行解密这些文件**。同时，据 [这个issue](https://github.com/charlotte-xiao/NCM2MP3/issues/22) 网易的.ncm加密方法在2023做了修改。
为了配合上述repo，请使用老一点版本的网易云下载歌单(tested with 2.5.2)，或者也可以搜素解密新加密方法的软件

## 使用方法：
1. 安装网易云音乐客户端
2. 登录账户，下载播放列表中所有音乐
3. 解密.ncm文件，并且放在原网易云音乐的下载目录中(程序需要读取解密后的后缀为flac还是mp3)
4. 双击运行脚本
5. 将解密后的音乐文件和生成的m3u文件拷贝到你的播放器目录(前提是要你的播放器支持 m3u)

## Tips：
如果你只需要在电脑中其他播放器使用 M3U 文件，可以使用绝对路径生成模式  
将参数 `-a` 设置为真，然后直接在下载目录运行脚本  
例如 -> `save_all_play_list.py -a True`  
也可以使用 `-p` 参数手动传递网易云音乐的歌曲下载目录位置  
例如 -> `save_all_play_list.py -a True -p "D:\NeteaseCloudMusicDownload"`

## Sg4Dylan repo 与原 repo 的区别：
 - Sg4Dylan的 fork 为 Python3+ only，与 Python2 不兼容
 - 增加了历史播放列表保存及当前播放列表保存
