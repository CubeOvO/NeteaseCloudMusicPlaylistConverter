import os
import json
import codecs
import argparse
import lib_save_playlist as cp


def get_play_tid(type=0):
    playlist_path = os.getenv('APPDATA')[:-7] + \
        "Local\\Netease\\CloudMusic\\webdata\\file\\queue"
    if type == 1:
        playlist_path = os.getenv('APPDATA')[:-7] + \
            "Local\\Netease\\CloudMusic\\webdata\\file\\history"
    playlist_raw_json = ""
    tid_list = []
    with open(playlist_path, 'rb') as playlist_text:
        playlist_raw_json = playlist_text.read().decode("utf-8")
    for item in json.loads(playlist_raw_json):
        tid_list.append(item['track']['id'])
    return tid_list


def write_to_m3u(type=0, absPath=None):
    playlistName = "当前播放列表"
    if type == 1:
        playlistName = "历史播放列表"
    file = codecs.open(playlistName + ".m3u", "w", "utf-8")
    count = 0
    try:
        file.writelines("#EXTM3U")
        musicIds = get_play_tid(type)
        for tid in musicIds:
            if tid is not None:
                detail = cp.getOfflineMusicDetail(tid, absPath)
                if detail is not None:
                    count=count + 1
                    file.writelines("\n#EXTINF:" + detail[0] + "\n" + detail[1])
    except Exception as e:
        raise
    else:
        pass
    finally:
        file.close()
        if count <= 0:
            os.remove(playlistName + ".m3u")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='NeteaseCloudMusicPlaylistConvert 0.1')
    parser.add_argument('-a', '--abs', help='M2U 中使用绝对路径')
    parser.add_argument('-p', '--path', help='网易云音乐下载目录绝对路径')
    useAbsPath = parser.parse_args().abs
    absPath = parser.parse_args().path
    if not absPath:
        absPath = os.getcwd()
    if not absPath.endswith('\\'):
        absPath += '\\'
    if str(useAbsPath).upper() != "TRUE":
        absPath = None
    write_to_m3u(0, absPath)
    write_to_m3u(1, absPath)
    cp.main(absPath)