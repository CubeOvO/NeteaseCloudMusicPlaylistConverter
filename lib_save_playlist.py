import sqlite3
import json
import codecs
import os


cx = sqlite3.connect(
    os.path.expanduser('~') + \
    "/AppData/Local/Netease/CloudMusic/Library/webdb.dat"
    )
cx.row_factory = sqlite3.Row

def getPlaylist():
    cu=cx.cursor()
    cu.execute("select * from web_playlist") 
    playlists=[]
    for item in cu.fetchall():
        playlist=(item["pid"],getPlaylistNameFromJson(item["playlist"]))
        playlists.append(playlist)
    return playlists

def getPlayListMusic(pid):
    cu=cx.cursor()
    cu.execute("select * from web_playlist_track where pid=?",[pid]) 
    musics=[]
    for item in cu.fetchall():
        musics.append(item["tid"]);
    return musics

def getOfflineMusicDetail(tid, absPath=None):
    cu=cx.cursor()
    cu.execute("select * from web_offline_track where track_id=?",[tid]) 
    music = cu.fetchone()
    if music is None:
        return None
    fullPath = music["relative_path"]
    if absPath:
        fullPath = absPath + fullPath
    detail = (getMusicNameFromJson(music["detail"]), fullPath)
    return detail

def writePlaylistToFile(pid, playlistName, absPath=None):
    file = codecs.open(playlistName + ".m3u", "w", "utf-8")
    count = 0
    try:
        file.writelines("#EXTM3U")
        musicIds = getPlayListMusic(pid)
        for tid in musicIds:
            if tid is not None:
                detail=getOfflineMusicDetail(tid, absPath)
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

def getPlaylistNameFromJson(jsonStr):
    playlistDetail = json.loads(jsonStr)
    return playlistDetail["name"]

def getMusicNameFromJson(jsonStr):
    musicDetail = json.loads(jsonStr)
    return musicDetail["name"]

def main(absPath=None):
    playlists = getPlaylist()
    for item in playlists:
        writePlaylistToFile(item[0], item[1], absPath)
