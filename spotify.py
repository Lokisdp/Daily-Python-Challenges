import subprocess
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ----------------- CONFIG -----------------
BLUETOOTH_NAME = "KILBURN II"  # Speaker name
SPOTIFY_PLAYLIST_URI = "spotify:playlist:43dHkQjcDhixfoNO4e4Rme"
CLIENT_ID = "07d96da1afb145fead4ff96131b0afc2"
CLIENT_SECRET = "581893f9a5644c298a53cc867c65cbf6"
REDIRECT_URI = "http://127.0.0.1:8888/callback"
SCOPE = "user-modify-playback-state user-read-playback-state user-read-currently-playing"
CHECK_INTERVAL = 15  # seconds
# ------------------------------------------

# Setup Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

def connect_speaker():
    """Connects to Bluetooth speaker using BluetoothCL"""
    print(f"Connecting to {BLUETOOTH_NAME}...")
    subprocess.run([r"L:\bluetoothcl\BluetoothCL.exe", "/connect", BLUETOOTH_NAME])

def is_speaker_active():
    """Checks if the speaker is detected as an active device by Spotify"""
    try:
        devices = sp.devices()["devices"]
        for d in devices:
            if d["name"] == BLUETOOTH_NAME and d["is_active"]:
                return True
        return False
    except:
        return False

def start_playlist():
    """Start playing the playlist on the speaker"""
    try:
        sp.start_playback(device_id=None, context_uri=SPOTIFY_PLAYLIST_URI)
        print(f"Playlist started on {BLUETOOTH_NAME}")
    except Exception as e:
        print(f"Error starting playback: {e}")

def wait_for_speaker_and_play():
    while True:
        devices = sp.devices()["devices"]
        speaker_connected = any(d["name"] == BLUETOOTH_NAME for d in devices)

        if not speaker_connected:
            print(f"{BLUETOOTH_NAME} not connected or not detected by Spotify. Reconnecting...")
            connect_speaker()
        else:
            if is_speaker_active():
                print(f"{BLUETOOTH_NAME} is active. Starting playlist...")
                start_playlist()
                break
            else:
                print(f"{BLUETOOTH_NAME} connected but not active. Waiting for Spotify to recognize it...")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print("Spotify Auto-play Automation Running...")
    wait_for_speaker_and_play()
