#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
import string
import random
from pymailinator.wrapper import Inbox

API_KEY = 'mailinator-api-key-here'

class Throwaway_creator:
    def __init__(self, api_token):
        self.inbox = Inbox(api_token)
        self.box = ''

    def write_data(self, name, passwd, mail):
        self.username_text.delete('1.0', END)
        self.password_text.delete('1.0', END)
        self.email_text.delete('1.0', END)
        self.username_text.insert(END, name)
        self.password_text.insert(END, passwd)
        self.email_text.insert(END, mail)
        self.box = mail

    def random_str(self, size=9, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def create_id(self):
        # Randomize data
        username = self.random_str()
        password = self.random_str()
        email = self.random_str()
        # Draw data
        self.write_data(username, password, email + '@mailinator.com')
        # Draw copy buttons to frames
        self.user_copy.pack(in_=self.user_frame, side='right')
        self.password_copy.pack(in_=self.password_frame, side='right')
        self.email_copy.pack(in_=self.email_frame, side='right')

    def get_mail(self):
        mail_box = self.box
        self.inbox.get(mailbox=mail_box)
        count = self.inbox.count()
        if count > 0:
            mail = self.inbox.messages[count-1]
            mail.get_message()
            text = mail.body
            subj = mail.subject
        else:
            text = 'Box is empty'
            subj = ''
        self.message.delete('1.0', END)
        self.subject.delete('1.0', END)
        self.message.insert(END, text)
        self.subject.insert(END, subj)

    def cp_username(self):
        self.root.clipboard_clear()
        text = self.username_text.get(1.0,END)[:-1]
        self.root.clipboard_append(text)

    def cp_password(self):
        self.root.clipboard_clear()
        text = self.password_text.get(1.0,END)[:-1]
        self.root.clipboard_append(text)

    def cp_email(self):
        self.root.clipboard_clear()
        text = self.email_text.get(1.0,END)[:-1]
        self.root.clipboard_append(text)

    def create_window(self):
        # GUI stuff
        self.root = Tk()
        self.root.wm_title('Throwaway creator')
        self.root.resizable(0, 0)
        # Frames
        self.buttons = Frame(self.root)
        self.user_frame = Frame(self.root)
        self.password_frame = Frame(self.root)
        self.email_frame = Frame(self.root)
        # Buttons
        self.refresh = Button(self.root, text='New ID', width=15, command=self.create_id)
        self.mailbt = Button(self.root, text='Get mail', width=15, command=self.get_mail)
        self.user_copy = Button(self.root, text='Copy Username', width=10, command=self.cp_username)
        self.password_copy = Button(self.root, text='Copy Password', width=10, command=self.cp_password)
        self.email_copy = Button(self.root, text='Copy Email', width=10, command=self.cp_email)
        # Texts
        self.username_text = Text(self.root, height=1, width=30, highlightthickness=0, border=1)
        self.email_text = Text(self.root, height=1, width=30, highlightthickness=0, border=1)
        self.password_text = Text(self.root, height=1, width=30, highlightthickness=0, border=1)
        self.subject = Text(self.root, height=1, width=47, highlightthickness=0, border=1)
        self.message = Text(self.root, height=10, width=47, highlightthickness=0, border=1)

    def draw_window(self):
        # Main GUI
        self.user_frame.pack()
        self.password_frame.pack()
        self.email_frame.pack()
        self.subject.pack()
        self.message.pack()
        self.buttons.pack()
        # Add stuff to frames
        self.username_text.pack(in_=self.user_frame, side='left')
        self.password_text.pack(in_=self.password_frame, side='left')
        self.email_text.pack(in_=self.email_frame, side='left')
        self.refresh.pack(in_=self.buttons, side='left')
        self.mailbt.pack(in_=self.buttons, side='left')
        # Draw
        self.root.mainloop()

tac = Throwaway_creator(API_KEY)
tac.create_window()
tac.draw_window()
