"""
Just a note you might need to change the #! python path. Firstly this was made
for Python 3, so I don't know if that's your thing, but changing to Python 2.X
might break tkinter, but you probably know what you are doing better than I do.
The path is also suitable only for OSX, so Linux folk need to adapt it. If you
don't know what's going on just do "which python" and you'll get the path.

Created by Topi Tuulensuu 2016. No licenses. Use it anyway you want, but only
for good and junk. And if you get into trouble, it's not my fault.
"""

#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
import string
import random
from pymailinator.wrapper import Inbox

API_KEY = 'mailinator-api-key-here'

class Throwaway_creator:
    def __init__(self, api_token):
        """Initialize Throwaway Creator

        Initializes Mailinator API and box variable which will store the
        randomly generated email address for Mailbox API
        """
        self.inbox = Inbox(api_token)
        self.box = ''

    def write_data(self, name, passwd, mail):
        """Write given data into fields.

        Clears name, password, and email fields. Writes given name, password,
        and email into their respective fields. And initializes self.box as
        given email address.

        Args:
            name: A string to be written in username field.
            passwd: A string to be written in password field.
            mail: An email address as string to be written in email field
                and to be used as current email box

        TODO:
            Checks for string lengths and email validation.
        """
        self.username_text.delete('1.0', END)
        self.password_text.delete('1.0', END)
        self.email_text.delete('1.0', END)
        self.username_text.insert(END, name)
        self.password_text.insert(END, passwd)
        self.email_text.insert(END, mail)
        self.box = mail

    def random_str(self, size=9, chars=string.ascii_letters + string.digits):
        """Random string generator

        By default generates a random string of defined length using alphabet
        and numbers. These strings are used for random usernames and passwords.

        Args:
            size: An integer of how many characters long string is wanted.
            chars: A character set that is used as material for random string.
                Default: alphabet (a-zA-Z) and numbers (0-9)

        Returns:
            A given length string randomized from given character set.

            example: nik2tMGUK

        TODO:
            Better randomization options.
            Maybe some input checks.
        """
        return ''.join(random.choice(chars) for _ in range(size))

    def create_id(self):
        """New ID generator

		Main method of the class. Uses random string generator to genrate
		"unique" username, password, and email address (email will always
		end with 'mailinator.com'). Calls write_data method with generated
		strings to draw them on screen. Adds buttons on screen for easier
		copying of randomized data.
        """
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
		"""Mail fetcher

		Fetches mail from email address stored in self.box variable. Method
		checks if box has mail or not. If email is found latest email will
		be shown on the screen, otherwise text "Box is empty" is shown.

		This is necessary functionality since some forums, websites, etc
		require email verification inorder to activate your new account.
		With this functionality you there is no need to open mailinator's
		webmail for activation link.
		"""
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

		"""
		TODO: These copy methods should probably just be one method instead of
		three separate ones
		"""
    def cp_username(self):
		"""Copies username from username field into clipboard"""
        self.root.clipboard_clear()
        text = self.username_text.get(1.0,END)[:-1]
        self.root.clipboard_append(text)

    def cp_password(self):
		"""Copies password from username field into clipboard"""
        self.root.clipboard_clear()
        text = self.password_text.get(1.0,END)[:-1]
        self.root.clipboard_append(text)

    def cp_email(self):
		"""Copies email from username field into clipboard"""
        self.root.clipboard_clear()
        text = self.email_text.get(1.0,END)[:-1]
        self.root.clipboard_append(text)

    def create_window(self):
		"""Window generator

		This method creates the actual Tkinter window. I don't know what to say
		it creates few frames and bunch of buttons and junk. Tkinter's docs
		are probably necessary to understand this unless you are l33t h4x0r.

		Docs:
			https://docs.python.org/3/library/tk.html

		There you go, enjoy. Sorry.
		"""
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
		"""Draw window

		This method draws the window created in the above window generator.
		Again pretty basic Tkinter stuff.
		"""
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

"""This makes the script executable from CLI or by app creator. I use py2app to
run this as "real executable". It's nothing fancy, just normal py2app, so I'm
not going to commit that since first Google result will probably be better.

Anyways this creates Throwaway Creator with given API KEY and then creates  &
draws the main window.
"""
tac = Throwaway_creator(API_KEY)
tac.create_window()
tac.draw_window()
