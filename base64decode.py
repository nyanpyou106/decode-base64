import base64

def base64decode(input_str):
    #base64の文字列をバイナリに変換してからデコードしていく
    utf8_binary = base64.b64decode(input_str.encode("ascii"))
    return utf8_binary.decode("utf-8")