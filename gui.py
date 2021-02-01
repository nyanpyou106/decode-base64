import PySimpleGUI as sg
import base64decode

sg.theme("DarkAmber")

layout = [  [sg.Text("デコードしたい文章")],
            [sg.Multiline(size=(80,10), key="-INPUT-")],
            [sg.Button("実行", key="-DECODE-")],
            [sg.Text("デコード結果")],
            [sg.Multiline(size=(80,14), key="-OUTPUT-")] ]

window = sg.Window("base64の文字列をデコードするやつ", layout, font=("Adobe Gothic Std B", 15), location=(0,0))

while True:
    event, values = window.read()
    if event == "-DECODE-":
        input_str = values["-INPUT-"]
        if input_str == "\n":
            #何も入力されていない時は何もしない
            pass
        else:
            oneline_input_str = input_str.replace("\n", "")
            output_str = base64decode.base64decode(oneline_input_str)
            window["-OUTPUT-"].update(output_str)
    if event == sg.WIN_CLOSED:
        break

window.close()