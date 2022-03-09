from turtle import down
import Famcy
import random
import os
import glob

class init(Famcy.FamcyPage):
    def __init__(self):
        super(init, self).__init__()

init_cls = init()
init.register("/init", Famcy.APIStyle(), init_cls=init_cls)

class StartPage(Famcy.FamcyPage):
    def __init__(self):
        super(StartPage, self).__init__()

        # Parameters
        self.color = ["red", "yellow", "green"]
        self.color_count = {c:0 for c in self.color}
        self.total_light = 1
        self.light_per_row = 3
        self.status = 0
        
        self.image_per_row = 1
        self.max_img_size = 40

        # Cards
        # self.light_card = self.Light_card()
        # self.image_card = self.Image_card()
        self.submit_card = self.Submit_card()
        self.first_prompt_card = self.First_Prompt_card()
        self.second_prompt_card = self.Second_Prompt_card()

        self.download_card = self.Download_card()

        self.input_card = self.Input_card()

        # self.layout.addWidget(self.light_card, 0, 0)
        # self.layout.addWidget(self.image_card, 1, 0)
        self.layout.addWidget(self.submit_card, 0, 0)
        self.layout.addWidget(self.download_card, 0, 1)
        self.layout.addWidget(self.input_card, 1, 0)


        self.layout.addStaticWidget(self.first_prompt_card)
        self.layout.addStaticWidget(self.second_prompt_card)

        # # Background Thread
        self.flash_thread = Famcy.FamcyBackgroundTask(self)
        self.init_thread = Famcy.FamcyBackgroundTask(self)

        # # Init
        init_cls.style.setAction(self.init_helper)
        init_cls.style.setReturnValue(indicator=True, message="Success")

    def background_thread_inner(self):

        '''
        self.<Famcy.FamcyBackgroundTask>.associate(
            self.<task_function(self, submission_obj, info_dict)>,
            info_dict={},
            target=<target>
        )
        '''

        self.flash_thread.associate(self.Light_flash, 
                                    info_dict = {
                                        "bit_mask": random.randint(0, 2**(self.total_light * len(self.color)) - 1)
                                    },
                                    target = self.light_card
        )
        Famcy.FamcyBackgroundQueue.add(self.flash_thread, Famcy.FamcyPriority.Standard)

    def Light_init(self, submission_obj, info_dict):
        self.Light_flash(
            submission_obj=submission_obj,
            info_dict={
                "bit_mask": 0
            }
        )

    def init_helper(self):
        self.init_thread.associate(self.Light_init, 
                                    info_dict={},
                                    target = self.light_card
        )
        Famcy.FamcyBackgroundQueue.add(self.init_thread, Famcy.FamcyPriority.Critical)

    def Light_flash(self, submission_obj, info_dict):

        self.color_count = {c:0 for c in self.color}
        bit_mask = info_dict["bit_mask"]

        for light in self.light_card.layout.content:
            temp_status = {}
            for c in self.color:
                if bit_mask & 1:
                    self.color_count[c]+=1
                    temp_status[c] = f"bulb_{c}"
                else:
                    temp_status[c] = ""
                bit_mask = bit_mask >> 1
            # print(temp_status)
            light[0].update({
                "status": temp_status,
                "light_size": "100%",
            })


        title = ""
        for k,v in self.color_count.items():
            title+= f"{k}: {v} "

        self.light_card.title = title

    def Light_card(self):
        card = Famcy.FamcyCard()
        title = ""
        for k,v in self.color_count.items():
            title+= f"{k}: {v} "
        card.title = title

        # Build lights
        display_light_list = [ Famcy.displayLight() for _ in range(self.total_light) ]
        for i, display_light in enumerate(display_light_list):
            display_light.update({
                "status": {"red": "", "yellow": "", "green": ""}, 
                "light_size": "100%",
            })
            card.layout.addWidget(display_light, i // self.light_per_row, i % self.light_per_row)

        return card

    def Image_card(self):
        card = Famcy.FamcyCard()

        images = glob.glob(os.path.join("static", "image", "*"))
        step = self.max_img_size // self.image_per_row
        img_size = [f"{self.max_img_size - i * step}%" for i in range(self.image_per_row)]
        display_image_list = [ Famcy.displayImage() for _ in range(len(images))]

        for i, (image, display_image) in enumerate(zip(images, display_image_list)):
            display_image.update({
                "title": "displayImage",
                "img_name": [image for _ in range(self.image_per_row)],
                "img_size": img_size,
                "border_radius": None
            })
            card.layout.addWidget(display_image, i, 0)

        return card


    def Submit_card(self):
        card = Famcy.FamcyCard()
        card.title = "Submit & Prompt example"
        input_form = Famcy.input_form()

        submitBtn = Famcy.submitBtn()
        submitBtn.update({
            "title": "Submit"
        })

        submitBtn.connect(self.btn_callback) # 所有東西都可以 connect, 但是要放在 input_form 裡面

        input_form.layout.addWidget(submitBtn, 0, 0)

        card.layout.addWidget(input_form, 0, 0)

        return card

    def First_Prompt_card(self):
        card = Famcy.FamcyCard()
        input_form = Famcy.input_form()

        displayParagraph = Famcy.displayParagraph()
        displayParagraph.update({
            "title": "",
            "content":  "Are you sure to submit?"
        })

        cancelBtn = Famcy.submitBtn()
        cancelBtn.update({
            "title": "cancel"
        })
        submitBtn = Famcy.submitBtn()
        submitBtn.update({
            "title": "submit"
        })
        cancelBtn.connect(self.remove_card) # 所有東西都可以 connect, 但是要放在 input_form 裡面
        submitBtn.connect(self.remove_and_prompt_card) # 所有東西都可以 connect, 但是要放在 input_form 裡面

        input_form.layout.addWidget(submitBtn, 0, 0)
        input_form.layout.addWidget(cancelBtn, 1, 0)

        card.layout.addWidget(displayParagraph, 0, 0)
        card.layout.addWidget(input_form, 1, 0)

        return card

    def Second_Prompt_card(self):
        card = Famcy.FamcyCard()
        input_form = Famcy.input_form()

        displayParagraph = Famcy.displayParagraph()
        displayParagraph.update({
            "title": "",
            "content":  "Submitted successfully"
        })

        cancelBtn = Famcy.submitBtn()
        cancelBtn.update({
            "title": "cancel"
        })

        cancelBtn.connect(self.remove_card) # 所有東西都可以 connect, 但是要放在 input_form 裡面

        input_form.layout.addWidget(cancelBtn, 0, 0)

        card.layout.addWidget(displayParagraph, 0, 0)
        card.layout.addWidget(input_form, 1, 0)

        return card

    def btn_callback(self, submission_obj, info):
        return Famcy.UpdatePrompt(target=self.first_prompt_card)
    
    def remove_and_prompt_card(self, submission_obj, info):
        return [
            Famcy.UpdateRemoveElement(prompt_flag=True),
            Famcy.UpdatePrompt(target=self.second_prompt_card)
            ]

    def remove_card(self, submission_obj, info):
        return Famcy.UpdateRemoveElement(prompt_flag=True)

    def Download_card(self):
        card = Famcy.FamcyCard()
        card.title = "Download file example"

        input_form = Famcy.input_form()

        download_link = Famcy.downloadFile()
        download_link.update({
            "title": "download_link title",
            "file_path": "http://127.0.0.1:8888/asset/image/test.png",
            "file_name": "download"
        })
        download_link.body.children[0]["style"] = "visibility: hidden;"
        

        displayImage = Famcy.displayImage()
        displayImage.update({
                "title": "image title",
                "img_name": ["asset/image/test.png"],
                "img_size": ["25%"],
                "border_radius": None
            })

        downloadBtn = Famcy.submitBtn()
        downloadBtn.update({
            "title": "Download file"
        })

        downloadBtn.connect(self.download_file) # 所有東西都可以 connect, 但是要放在 input_form 裡面

        input_form.layout.addWidget(downloadBtn, 0, 0)
        input_form.layout.addWidget(download_link, 1, 0)

        card.layout.addWidget(input_form, 0, 0)
        card.layout.addWidget(displayImage, 1, 0)

        return card

    def download_file(self, submission_obj, info):
        extra_script = "document.getElementById('" +\
                        self.download_card.layout.content[0][0].layout.content[1][0].id +\
                        "_input').click();"        
        return Famcy.UpdateAlert(alert_message="alert: download", extra_script=extra_script)


    def Input_card(self):
        card = Famcy.FamcyCard()
        card.title = "Update html & alert example"

        input_form = Famcy.input_form()

        pureInput = Famcy.pureInput()
        pureInput.update({
                "title": "pureInput title",
                "desc": "pureInput desc",
                "defaultValue": "pureInput defaultValue",
                "input_type": "text",
                "num_range": None,
                "placeholder": "",
                "mandatory": True,
                "action_after_post": "save",
            })
        pureInput.set_submit_value_name("pureInput")

        inputPassword = Famcy.inputPassword()
        inputPassword.update({
                "title": "inputPassword title",
                "desc": "inputPassword desc",
                "mandatory": True,
                "action_after_post": "clean",
            })
        inputPassword.set_submit_value_name("inputPassword")
        

        inputList = Famcy.inputList()
        inputList.update({
                "title": "inputList title",
                "desc": "inputList desc",
                "value": [str(i) for i in range(5)],
                "defaultValue": None,
                "mandatory": True,
                "action_after_post": "save"
            })
        inputList.set_submit_value_name("inputList")
        

        inputParagraph = Famcy.inputParagraph()
        inputParagraph.update({
                "title": "inputParagraph title",
                "desc": "inputParagraph desc",
                "height": "10vh",
                "placeholder": "inputParagraph placeholder",
                "mandatory": True,
                "action_after_post": "save",
            })

        displayParagraph = Famcy.displayParagraph()
        displayParagraph.update({
                "title": "displayParagraph title",
                "content": "displayParagraph desc",
            })


        submitBtn = Famcy.submitBtn()
        submitBtn.update({
            "title": "Submit"
        })

        input_form.layout.addWidget(pureInput, 0, 0)
        input_form.layout.addWidget(inputPassword, 1, 0)
        input_form.layout.addWidget(inputList, 2, 0)
        input_form.layout.addWidget(inputParagraph, 3, 0)
        input_form.layout.addWidget(submitBtn, 4, 0)

        submitBtn.connect(self.update_block_callback) # 所有東西都可以 connect, 但是要放在 input_form 裡面

        card.layout.addWidget(input_form, 0, 0)
        card.layout.addWidget(displayParagraph, 1, 0)

        return card

    def update_block_callback(self, submission_obj, info):
        # print(f"'\033[91m'{info}'\033[0m'")

        content = f"pureInput: {info[0][0]}<br>inputPassword: {info[1][0]}<br>inputList: {info[2][0]}<br>inputParagraph: {info[3][0]}"

        self.input_card.layout.content[1][0].update({
            "content": content
        })
        return [
            Famcy.UpdateBlockHtml(target=self.input_card), 
            Famcy.UpdateAlert(target=self.input_card, alert_message="ALERT")
            ]
   
StartPage.register("/startFamcy", Famcy.ClassicStyle(), permission_level=0, background_thread=True, background_freq=1 , init_cls=None)