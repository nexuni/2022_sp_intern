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
        self.total_light = 9 
        self.light_per_row = 3
        self.status = 0
        
        self.image_per_row = 4
        self.max_img_size = 40

        # Cards
        self.light_card = self.Light_card()
        self.image_card = self.Image_card()

        self.layout.addWidget(self.light_card, 0, 0)
        self.layout.addWidget(self.image_card, 1, 0)

        # Background Thread
        self.flash_thread = Famcy.FamcyBackgroundTask(self)
        self.init_thread = Famcy.FamcyBackgroundTask(self)

        # Init
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


   
StartPage.register("/startFamcy", Famcy.ClassicStyle(), permission_level=0, background_thread=True, background_freq=1 , init_cls=None)