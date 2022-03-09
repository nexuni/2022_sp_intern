import Famcy
import os
import json
import requests
import urllib
import time

class Week2Page(Famcy.FamcyPage):
    def __init__(self):
        super(Week2Page, self).__init__()

        # for declaration
        # ===============
        self.pcard_1 = self.pcard1()
        self.pcard_2 = self.pcard2()
        self.pcard_3 = self.pcard3()

        self.layout.addStaticWidget(self.pcard_1)
        self.layout.addStaticWidget(self.pcard_2)
        self.layout.addStaticWidget(self.pcard_3)

        self.card_1 = self.card1()
        self.card_2 = self.card2()
        self.card_3 = self.card3()

        self.layout.addWidget(self.card_1, 0, 0)
        self.layout.addWidget(self.card_2, 0, 1)
        self.layout.addWidget(self.card_3, 0, 2)
        
    # background task function 
    # ====================================================
    # ====================================================
    # ====================================================


    # card
    # ====================================================
    def card1(self):
        card1 = Famcy.FamcyCard()
        card1.fit_content = True
        card1.title = "This is an example of UpdatePrompt response"

        _input_form = Famcy.input_form()

        _inputBlockSec = Famcy.inputBlockSec()
        _inputBlockSec.update({
                "title": "Title of inputBlockSec",
                "content": "Display image on prompt card",
                "img_src": "static/image/famcydark.png",
                "btn_name": "Submit inputBlockSec",
            })
        _inputBlockSec.connect(self.inputBlockSec_submit)

        _inputBtn = Famcy.inputBtn()
        _inputBtn.update({
                "title": "Title of inputBtn",
                "desc": "Display input value on prompt card",
                "input_type": "text",
                "num_range": None,
                "placeholder": "This is an example of placeholder",
                "button_name": "Submit",
                "mandatory": False,
                "action_after_post": "clean"
            })
        _inputBtn.set_submit_value_name("inputBtn_submit")
        _inputBtn.connect(self.inputBtn_submit)

        _urlBtn = Famcy.urlBtn()
        _urlBtn.update({
                "title": "Title of urlBtn",
                "style": "link_style",
                "url": "https://github.com/nexuni/Famcy",
                "desc": "This is an example",
                "button_name": "Redirect to Famcy github"
            })

        _submitBtn = Famcy.submitBtn()
        _submitBtn.update({
                "title": "download_file",
            })
        _submitBtn.connect(self.download_file)

        download_link = Famcy.downloadFile()
        download_link.update({"title": "","file_path": 'http://127.0.0.1:8888/static/image/famcydark.png',"file_name": 'download'})
        download_link.body.children[0]["style"] = "visibility: hidden;"

        _input_form.layout.addWidget(_inputBlockSec, 0, 0)
        _input_form.layout.addWidget(_inputBtn, 1, 0)
        _input_form.layout.addWidget(_urlBtn, 2, 0)
        _input_form.layout.addWidget(_submitBtn, 3, 0)
        _input_form.layout.addWidget(download_link, 4, 0)

        card1.layout.addWidget(_input_form, 0, 0)

        return card1 

    def card2(self):
        card2 = Famcy.FamcyCard()
        card2.fit_content = True
        card2.title = "This is an example of UpdateBlockHtml response"

        _input_form = Famcy.input_form()

        _pureInput = Famcy.pureInput()
        _pureInput.update({
                "title": "Title of pureInput",
                "desc": "This is an example",
                "defaultValue": "This is default input",
                "input_type": "text",
                "num_range": None,
                "placeholder": "",
                "mandatory": True,
                "action_after_post": "save",
            })

        _inputPassword = Famcy.inputPassword()
        _inputPassword.update({
                "title": "Title of inputPassword",
                "desc": "This is an example",
                "mandatory": True,
                "action_after_post": "clean",
            })

        _inputList = Famcy.inputList()
        _inputList.update({
                "title": "Title of inputList",
                "desc": "This is an example",
                "value": ["Option 1", "Option 2", "Option 3"],
                "defaultValue": None,
                "mandatory": True,
                "action_after_post": "save"
            })

        _inputParagraph = Famcy.inputParagraph()
        _inputParagraph.update({
                "title": "Title of inputParagraph",
                "desc": "This is an example",
                "height": "10vh",
                "placeholder": "This is an example of placeholder",
                "mandatory": True,
                "action_after_post": "save",
            })

        _submitBtn = Famcy.submitBtn()
        _submitBtn.update({
                "title": "Submit all info",
            })
        _submitBtn.connect(self.inputInfo_submit)

        _displayParagraph = Famcy.displayParagraph()
        _displayParagraph.update({
                "title": "",
                "content": ""
            })

        _input_form.layout.addWidget(_pureInput, 0, 0)
        _input_form.layout.addWidget(_inputPassword, 1, 0)
        _input_form.layout.addWidget(_inputList, 2, 0)
        _input_form.layout.addWidget(_inputParagraph, 3, 0)
        _input_form.layout.addWidget(_submitBtn, 4, 0)

        card2.layout.addWidget(_input_form, 0, 0)
        card2.layout.addWidget(_displayParagraph, 1, 0)

        return card2
    

    def card3(self):
        card3 = Famcy.FamcyCard()
        card3.fit_content = True
        card3.title = "This is an example of UpdateAlert response"

        _input_form = Famcy.input_form()

        _singleChoiceRadioInput = Famcy.singleChoiceRadioInput()
        _singleChoiceRadioInput.update({
                "title": "Title of singleChoiceRadioInput",
                "desc": "Please select the number that you want to sum up",
                "mandatory": False,
                "value": ["1", "2", "3"],
                "action_after_post": "clean",
            })
        _singleChoiceRadioInput.set_submit_value_name("singleChoiceRadioInput_submit")

        _multipleChoicesRadioInput = Famcy.multipleChoicesRadioInput()
        _multipleChoicesRadioInput.update({
                "title": "Title of multipleChoicesRadioInput",
                "desc": "Please select the number that you want to sum up",
                "mandatory": False,
                "value": ["1", "2", "3"],
                "action_after_post": "clean",
            })
        _multipleChoicesRadioInput.set_submit_value_name("multipleChoicesRadioInput_submit")

        _submitBtn = Famcy.submitBtn()
        _submitBtn.update({
                "title": "Sum up all numbers"
            })
        _submitBtn.connect(self.sum_up_selected_value)

        _input_form.layout.addWidget(_singleChoiceRadioInput, 0, 0)
        _input_form.layout.addWidget(_multipleChoicesRadioInput, 1, 0)
        _input_form.layout.addWidget(_submitBtn, 2, 0)

        card3.layout.addWidget(_input_form, 0, 0)

        return card3
    # ====================================================
    # ====================================================


    # prompt card
    # ====================================================
    def pcard1(self):
        pcard1 = Famcy.FPromptCard()

        _displayParagraph = Famcy.displayParagraph()
        _displayParagraph.update({
                "title": "The value that you entered",
                "content":  "None"
            })

        _input_form = Famcy.input_form()

        _submitBtn_prompt = Famcy.submitBtn()
        _submitBtn_prompt.update({
                "title": "Sumbit prompt card"
            })
        _submitBtn_prompt.connect(self.submit_pcard)

        _submitBtn = Famcy.submitBtn()
        _submitBtn.update({
                "title": "Close prompt card"
            })
        _submitBtn.connect(self.remove_pcard)

        _input_form.layout.addWidget(_submitBtn, 0, 0)
        _input_form.layout.addWidget(_submitBtn_prompt, 0, 1)

        pcard1.layout.addWidget(_displayParagraph, 0, 0)
        pcard1.layout.addWidget(_input_form, 1, 0)

        return pcard1

    def pcard2(self):
        pcard2 = Famcy.FPromptCard()

        _displayImage = Famcy.displayImage()
        _displayImage.update({
                "title": "This is an example",
                "img_name": ["static/image/famcylogo.png"],
                "img_size": ["50%"],
                "border_radius": None
            })

        _input_form = Famcy.input_form()

        _submitBtn = Famcy.submitBtn()
        _submitBtn.update({
                "title": "Close prompt card"
            })
        _submitBtn.connect(self.remove_pcard)

        _input_form.layout.addWidget(_submitBtn, 0, 0)

        pcard2.layout.addWidget(_displayImage, 0, 0)
        pcard2.layout.addWidget(_input_form, 1, 0)
        return pcard2

    def pcard3(self):
        pcard3 = Famcy.FPromptCard()

        _input_form = Famcy.input_form()

        _submitBtn = Famcy.submitBtn()
        _submitBtn.update({
                "title": "Close prompt card"
            })
        _submitBtn.connect(self.remove_pcard)

        _input_form.layout.addWidget(_submitBtn, 0, 0)

        pcard3.layout.addWidget(_input_form, 0, 0)
        return pcard3
    # ====================================================
    # ====================================================


    # submission function
    # ====================================================
    def submit_pcard(self, submission_obj, info_list):
        return [Famcy.UpdateRemoveElement(prompt_flag=True), Famcy.UpdatePrompt(target=self.pcard_3)]

    def remove_pcard(self, submission_obj, info_list):
        return Famcy.UpdateRemoveElement(prompt_flag=True)

    def inputBtn_submit(self, submission_obj, info_list):
        self.pcard_1.layout.content[0][0].update({
                "content":  "Return value in list: " + str(info_list[0][0]) + "; Return value in dict: " + str(info_list["inputBtn_submit"])
            })

        return Famcy.UpdatePrompt(target=self.pcard_1)

    def inputBlockSec_submit(self, submission_obj, info_list):
        return Famcy.UpdatePrompt(target=self.pcard_2)

    def inputInfo_submit(self, submission_obj, info_list):
        self.card_2.layout.content[1][0].update({
                "title": "Input information",
                "content": "pureInput: " + info_list[0][0] + "</br>inputPassword: " + info_list[1][0] + "</br>inputList: " + info_list[2][0] + "</br>inputParagraph: " + info_list[3][0]
            })
        return Famcy.UpdateBlockHtml(target=self.card_2)

    def sum_up_selected_value(self, submission_obj, info_list):
        s_submit_value = info_list["singleChoiceRadioInput_submit"] if info_list["singleChoiceRadioInput_submit"] else 0
        m_submit_value = info_list["multipleChoicesRadioInput_submit"] if info_list["multipleChoicesRadioInput_submit"] else []
        submit_sum = int(s_submit_value) + sum([int(val) for val in m_submit_value])
        msg = "The sum of values that you selected is " + str(submit_sum)
        return Famcy.UpdateAlert(target=self.card_3, alert_message=msg)

    def download_file(self, submission_obj, info_list):
        extra_script = "document.getElementById('" + self.card_1.layout.content[0][0].layout.content[4][0].id + "_input').click();"
        return Famcy.UpdateAlert(target=self.card_1, alert_message="succeed!", extra_script=extra_script)
    # ====================================================
    # ====================================================
        

    # http request function
    # ====================================================
    # ====================================================
    # ====================================================


    # utils
    # ====================================================
    # ====================================================
    # ====================================================

   
Week2Page.register("/Week2Example", Famcy.ClassicStyle(), permission_level=0, background_thread=False)

# import Famcy
# import os
# import json
# import requests
# import urllib
# import time

# class testPage(Famcy.FamcyPage):
#     def __init__(self):
#         super(testPage, self).__init__()

#         # for declaration
#         # ===============
#         self.pcard_1 = self.pcard1()
#         self.layout.addStaticWidget(self.pcard_1, 10)

#         self.card_1 = self.card1()
#         self.card_2 = self.card2()
#         self.layout.addWidget(self.card_1, 0, 0)
#         self.layout.addWidget(self.card_2, 1, 0)
        
#     # background task function 
#     # ====================================================
#     # ====================================================
#     # ====================================================


#     # card
#     # ====================================================
#     def card1(self):
#         _card1 = Famcy.FamcyCard()

#         _input_form = Famcy.input_form()
#         _input_form.loader = False

#         _pureInput = Famcy.pureInput()
#         _pureInput.update({
#                 "title": "Title of pureInput",
#                 "desc": "This is an example",
#                 "defaultValue": "This is default input",
#                 "input_type": "text",
#                 "num_range": None,
#                 "placeholder": "",
#                 "mandatory": True,
#                 "action_after_post": "save",
#             })
#         _pureInput.set_submit_value_name("input_submit")

#         _submitBtn = Famcy.submitBtn()
#         _submitBtn.update({
#                 "title": "hello"
#             })
#         _submitBtn.connect(self.download_file)

#         download_link = Famcy.downloadFile()
#         download_link.update({
#             "title": "",
#             "file_path": 'http://127.0.0.1:8888/asset/image/nexuni.png',
#             "file_name": 'download'})
#         download_link.body.children[0]["style"] = "visibility: hidden;"

#         _displayParagraph = Famcy.displayParagraph()
#         _displayParagraph.update({
#                 "title": "bye",
#                 "content": "hellllllo"
#             })

#         _input_form.layout.addWidget(_pureInput, 0, 0)
#         _input_form.layout.addWidget(_submitBtn, 1, 0)
#         _input_form.layout.addWidget(download_link, 2, 0)

#         _card1.layout.addWidget(_input_form, 0, 0)
#         _card1.layout.addWidget(_displayParagraph, 1, 0)

#         return _card1

#     def card2(self):
#         _card2 = Famcy.FamcyCard()

#         _displayImage = Famcy.displayImage()
#         _displayImage.update({
#                 "title": "displayImage",
#                 "img_name": ["/asset/image/nexuni.png"],
#                 "img_size": ["40%"],
#                 "border_radius": None
#             })

#         _card2.layout.addWidget(_displayImage, 0, 0)

#         return _card2
#     # ====================================================
#     # ====================================================


#     # prompt card
#     # ====================================================
#     def pcard1(self):
#         _pcard1 = Famcy.FamcyCard()

#         _input_form = Famcy.input_form()
#         _input_form.loader = False

#         _submitBtn = Famcy.submitBtn()
#         _submitBtn.update({
#                 "title": "close"
#             })
#         _submitBtn.connect(self.remove_pcard)

#         _input_form.layout.addWidget(_submitBtn, 0, 0)

#         _pcard1.layout.addWidget(_input_form, 0, 0)

#         return _pcard1
#     # ====================================================
#     # ====================================================


#     # submission function
#     # ====================================================
#     def btn_callback(self, submission_obj, info):
#         return Famcy.UpdatePrompt(target=self.pcard_1)

#     def remove_pcard(self, submission_obj, info):
#         return Famcy.UpdateRemoveElement(prompt_flag=True)

#     def update_block_callback(self, submission_obj, info):
#         self.card_1.layout.content[1][0].update({
#                 "title": info[0][0] + info["input_submit"] + str(info.info_list) + str(info.info_dict)
#             })
#         return [Famcy.UpdateBlockHtml(target=self.card_1), Famcy.UpdateAlert(target=self.card_1, alert_message="update alert")]

#     def download_file(self, submission_obj, info):
#         extra_script = "document.getElementById('" + self.card_1.layout.content[0][0].layout.content[2][0].id + "_input').click();"
#         return Famcy.UpdateAlert(alert_message="succeed", extra_script=extra_script)
#     # ====================================================
#     # ====================================================
        

#     # http request function
#     # ====================================================
#     # ====================================================
#     # ====================================================


#     # utils
#     # ====================================================
#     # ====================================================
#     # ====================================================

# testPage.register("/testExample", Famcy.ClassicStyle(), permission_level=0, background_thread=False)



