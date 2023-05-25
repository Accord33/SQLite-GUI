import tkinter
from tkinter import filedialog
import time
import sqlite3

class App:
    def __init__(self):
        self.frm = tkinter.Tk()
        self.frm.geometry("600x600")
        self.frm.resizable(width=0, height=0)
        self.frm.title("SQLite3操作パネル")

        self.create()

    # UIの作成
    def create(self):
        header = tkinter.Frame(aself.frm)å
        header.pack(fill="x", anchor=tkinter.SW)
        execute_btn = tkinter.Button(header, text="実行", command=self.execute)
        execute_btn.pack(side="left")
        tkinter.Label(header, text="DB Address:").pack(side="left", padx=10)
        self.db_address = tkinter.Entry(header)
        self.db_address.pack(side="left")
        tkinter.Button(header, text="ファイル参照",command=self.file_get).pack(side="left")

        self.input_box = tkinter.Text(height=15)
        self.input_box.pack(fill="x")
        self.output_box = tkinter.Text(height=13)
        self.output_box.pack(fill="x")

        bottom = tkinter.Frame(self.frm, relief="sunken")
        bottom.pack(fill="x")
        self.result_label = tkinter.Label(bottom, text="")
        self.result_label.pack(side="left")
        self.exe_time = tkinter.Label(bottom, text="0:00:00")
        self.exe_time.pack(side="right")
        tkinter.Label(bottom, text="実行時間：").pack(side="right")

    # ファイルパスの取得
    def file_get(self):
        self.db_address.insert(tkinter.END,f"{filedialog.askopenfilename()}")

    # スクリプト実行
    def execute(self):
        text = self.input_box.get("1.0",tkinter.END)
        try:
            timer = time.time()
            conn = sqlite3.connect(self.db_address.get())
            if text != "":
                cur = conn.cursor()
                cur.execute(text)
                conn.commit()
                self.output_box.delete("1.0","end")
                for i in cur:
                    self.output_box.insert(tkinter.END,f"{i}\n")
            conn.close()
            self.output_box.insert(tkinter.END,"正常に終了しました")
            timer_get = time.time()-timer
            self.exe_time["text"] = f"{timer_get}"
        except BaseException as be:
            self.output_box.delete("1.0","end")
            self.output_box.insert(tkinter.END, be)

    def main(self):
        self.frm.mainloop()

if __name__ == "__main__":
    app = App()
    app.main()