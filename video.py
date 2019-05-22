from config import RTMP_INDEX_FILE, RTMP_TEMPLATE_FILE, RTMP_PLAYER_ADDRESS, RTMP_ADDRESS_TEMPLATES
import webbrowser


class Video():
    def __init__(self):
        self.index_file = RTMP_INDEX_FILE
        self.template_file = RTMP_TEMPLATE_FILE
        self.player_address = RTMP_PLAYER_ADDRESS

    def open_rtmp(self, address):
        with open(self.template_file, 'r', encoding='utf-8') as f:
            html = f.read()
        html = html.replace('>>>path<<<', address)
        with open(self.index_file, 'w', encoding='utf-8') as f2:
            f2.write(html)
        webbrowser.open(self.player_address)
    
    @staticmethod
    def create_address(idx, ip):
        return RTMP_ADDRESS_TEMPLATES[idx].format(ip)
