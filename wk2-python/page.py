import Famcy
import datetime



class ProjectPage(Famcy.FamcyPage):
    def __init__(self):
        super(ProjectPage, self).__init__()

        # for declaration
        # ===============
        self.table_info = []
        self.used_password = []

        self.card1 = self.card1()
        self.card2 = self.card2()


        self.layout.addWidget(self.card1, 0, 0)
        self.layout.addWidget(self.card2, 3, 0)

        self.pcard1 = self.pcard1()
        self.p_update_card = self.p_update_card()

        self.layout.addStaticWidget(self.p_update_card)
        self.layout.addStaticWidget(self.pcard1)

        


        # ===============

        
    # background task function 
    # ====================================================
    

    # ====================================================
    # ====================================================


    # card
    # ====================================================
    def card1(self):
        card1 = Famcy.FamcyCard()
        card1.fit_content = True

        input_form = Famcy.input_form()

        input_id = Famcy.pureInput()
        input_id.update({"title": "輸入使用者帳號"})

        input_password = Famcy.inputPassword()
        input_password.update({
                "title": "輸入使用者密碼",
                "desc": "",
                "mandatory": False,
                "action_after_post": "clean",
            })


        search_btn = Famcy.submitBtn()
        search_btn.update({"title": "查詢使用者資料"})
        search_btn.connect(self.inputInfo_submit, target=card1)

        insert_btn = Famcy.submitBtn()
        insert_btn.update({"title": "新增使用者資料"})
        insert_btn.connect(self.inputBtn_submit)

        _displayParagraph = Famcy.displayParagraph()
        _displayParagraph.update({
                "title": "",
                "content": ""
            })

        input_form.layout.addWidget(input_id, 0, 0, 2, 1)
        input_form.layout.addWidget(input_password, 0, 1, 2, 1)

        input_form.layout.addWidget(search_btn, 0, 4)
        input_form.layout.addWidget(insert_btn, 1, 4)


        card1.layout.addWidget(input_form, 0, 0)
        card1.layout.addWidget(_displayParagraph, 1, 0)

        return card1
    def card2(self):
        card2 = Famcy.FamcyCard()
        card2.fit_content = True

        input_form = Famcy.input_form()
        # input_form.body.style["word-break"] = "break-all !important"


        # self.table_info = self.make_time_readable(self.table_info,["validstart","validend"])
        # print("self.table_info===========",self.table_info)

        table_content = Famcy.table_block()
        table_content.update({
                "toolbar": False,
                "input_button": "radio",
                "input_value_col_field": "id",
                "page_detail": False,
                "page_detail_content": ["<div style='display: flex;'><p style='width: 50%;'>交易紀錄: </p><p style='width: 50%;text-align: right;'>一些紀錄</p></div>", "<div style='display: flex;'><p style='width: 50%;'>交易紀錄: </p><p style='width: 50%;text-align: right;'>一些紀錄</p></div>", "<div style='display: flex;'><p style='width: 50%;'>交易紀錄: </p><p style='width: 50%;text-align: right;'>一些紀錄</p></div>"],
                "page_footer": True,
                "page_footer_detail": {
                    "page_size": 15,
                    "page_list": [15, "all"]
                },
                "column": [[
                    {
                        "title": '使用者帳號',
                        "field": '_id',
                        "rowspan": 1,
                        "align": 'center',
                        "valign": 'middle',
                        "sortable": True
                    },
                    {
                        "title": '當前密碼',
                        "field": '_password',
                        "rowspan": 1,
                        "align": 'center',
                        "valign": 'middle',
                        "sortable": True
                    },
                    {
                        "title": '輸入錯誤次數',
                        "field": '_error_number',
                        "rowspan": 1,
                        "align": 'center',
                        "valign": 'middle',
                        "sortable": True
                    },
                    {
                        "title": '最近修改密碼時間',
                        "field": '_change_pw_time',
                        "rowspan": 1,
                        "align": 'center',
                        "valign": 'middle',
                        "sortable": True
                    },
                ]],
                "data": self.table_info
          })

        # self.table_info = self.make_time_readable_reverse(self.table_info,["validstart","validend"])

        new_btn = Famcy.submitBtn()
        new_btn.update({"title": "修改使用者資料"})
        new_btn.connect(self.update_info)

        cancel_btn = Famcy.submitBtn()
        cancel_btn.update({"title": "刪除使用者資料"})
        # cancel_btn.connect(self.delete_info, target=self.p_del_card)

        input_form.layout.addWidget(table_content, 0, 0, 1, 2)
        input_form.layout.addWidget(new_btn, 1, 0)
        input_form.layout.addWidget(cancel_btn, 1, 1)

        card2.layout.addWidget(input_form, 0, 0)

        return card2

    # ====================================================
    # ====================================================


    # prompt card
    # ====================================================
    def pcard1(self):
        pcard1 = Famcy.Famcy.FamcyPromptCard()

        input_form = Famcy.input_form()

        input_id = Famcy.pureInput()
        input_id.update({"title": "輸入使用者帳號"})

        input_password = Famcy.inputPassword()
        input_password.update({
                "title": "輸入使用者密碼",
                "desc": "",
                "mandatory": False,
                "action_after_post": "clean",
            })
        
        _submitBtn_prompt = Famcy.submitBtn()
        _submitBtn_prompt.update({
                "title": "送出"
            })
        _submitBtn_prompt.connect(self.insert_info,target=pcard1)

        _closeBtn_prompt = Famcy.submitBtn()
        _closeBtn_prompt.update({
                "title": "離開"
            })
        _closeBtn_prompt.connect(self.remove_pcard)

        
        input_form.layout.addWidget(input_id, 0, 0, 2, 2)
        input_form.layout.addWidget(input_password, 2, 0, 2, 2)
        input_form.layout.addWidget(_closeBtn_prompt, 4, 0, 1, 1)
        input_form.layout.addWidget(_submitBtn_prompt, 4, 1, 1, 1)

        pcard1.layout.addWidget(input_form, 0, 0)

        return pcard1
    
    def p_update_card(self):
        p_card = Famcy.FamcyPromptCard()

        input_form = Famcy.input_form()

        input_id = Famcy.pureInput()
        input_id.update({"title": "輸入原先帳號"})

        input_password1 = Famcy.inputPassword()
        input_password1.update({
                "title": "輸入原先密碼",
                "desc": "",
                "mandatory": False,
                "action_after_post": "clean",
            })

        input_password2 = Famcy.inputPassword()
        input_password2.update({
                "title": "輸入新密碼",
                "desc": "",
                "mandatory": False,
                "action_after_post": "clean",
            })

        submit_btn = Famcy.submitBtn()
        submit_btn.update({"title":"確認"})
        submit_btn.connect(self.update_modify, target=p_card)

        cancel_btn = Famcy.submitBtn()
        cancel_btn.update({"title":"返回"})
        cancel_btn.connect(self.remove_pcard)

        input_form.layout.addWidget(input_id, 0, 0, 1, 2)
        input_form.layout.addWidget(input_password1, 1, 0, 1, 2)
        input_form.layout.addWidget(input_password2, 2, 0)

        input_form.layout.addWidget(submit_btn, 4, 0, 1, 1)
        input_form.layout.addWidget(cancel_btn, 4, 1, 1, 1)
  

        p_card.layout.addWidget(input_form, 0, 0)

        return p_card
    
    # def p_card_delete(self):
    #     pcard = Famcy.FamcyPromptCard()

    #     input_form = Famcy.input_form()

    #     text_msg = Famcy.displayParagraph()
    #     text_msg.update({"title": "確認是否執行?", "content": ""})

    #     confirm_btn = Famcy.submitBtn()
    #     confirm_btn.update({"title":"確認"})
    #     confirm_btn.connect(self.delete_info)

    #     cancel_btn = Famcy.submitBtn()
    #     cancel_btn.update({"title":"取消"})
    #     cancel_btn.connect(self.prompt_remove_input)

    #     input_form.layout.addWidget(text_msg, 0, 0, 1, 2)
    #     input_form.layout.addWidget(confirm_btn, 1, 0)
    #     input_form.layout.addWidget(cancel_btn, 1, 1)

    #     pcard.layout.addWidget(input_form, 0, 0)

    #     return pcard
    # ====================================================
    # ====================================================


    # submission function
    # ====================================================
    
    def inputInfo_submit(self, submission_obj, info_list):
        msg = "資料填寫有誤"
        flag = True
         
        if info_list[0][0] == [] or info_list[1][0] == []:
            flag = False
        elif self.table_info == []:
            msg = "目前資料庫沒有資料"
            flag = True

        if flag :
            for i in range(0,len(self.table_info)) :
                if str(info_list[0][0]) == self.table_info[i]["_id"]:
                    if str(info_list[1][0]) == self.table_info[i]["_password"]:
                        msg = "查詢成功"
                        self.card1.layout.content[1][0].update({
                            "title": "查詢結果",
                            "content": "使用者帳號: " + self.table_info[i]["_id"] + "</br>當前密碼: " + self.table_info[i]["_password"] + "</br>輸入錯誤次數: " + str(self.table_info[i]["_error_number"]) +"</br>最近修改密碼時間: "+ self.table_info[i]["_change_pw_time"]
                        })
                    else:
                        self.table_info[i]["_error_number"] +=1
                        msg = "密碼錯誤"
        return [Famcy.UpdateAlert(alert_message=msg), Famcy.UpdateBlockHtml(target=self.card1),Famcy.UpdateBlockHtml(target=self.card2)]
    
    # def submit_pcard(self, submission_obj, info_list):
    #     return Famcy.UpdatePrompt(target=self.pcard1)

    def remove_pcard(self, submission_obj, info_list):
        return Famcy.UpdateRemoveElement(prompt_flag=True)
    
    def inputBtn_submit(self, submission_obj, info_list):
        return Famcy.UpdatePrompt(target=self.pcard1)
    
    def update_info(self, submission_obj, info_list):
        return Famcy.UpdatePrompt(target=self.p_update_card)

    def insert_info(self, submission_obj, info_list):
        msg = "資料填寫有誤"
        flag = True
        for _ in info_list.info_list:
            if not len(_) > 0:
                flag = False
                break
        if self.table_info != []:
            for i in range(0,len(self.table_info)) :
                if str(info_list[0][0]) == self.table_info[i]["_id"]:
                    flag = False
                    msg = "此使用者帳號已註冊"
                    break
        if flag:
            self.table_info.append({"_id": str(info_list[0][0]),
                        "_password": str(info_list[1][0]),
                        "_error_number": 0,
                        "_change_pw_time": str(datetime.datetime.now())
                        })
            self.used_password.append(str(info_list[1][0]))
            msg = "成功加入資料"
            self.card2.layout.content[0][0].layout.content[0][0].update({
                        "data": self.table_info
                        })
        return [Famcy.UpdateAlert(alert_message=msg), Famcy.UpdateBlockHtml(target=self.card2)]
    
    def update_modify(self, submission_obj, info_list):
        msg = "資料填寫有誤"
        flag = True
         
        if info_list[0][0] == [] or info_list[1][0] == []:
            flag = False
        elif self.table_info == []:
            msg = "目前資料庫沒有資料"
            flag = True

        if flag :
            for i in range(0,len(self.table_info)) :
                if str(info_list[0][0]) == self.table_info[i]["_id"]:
                    if str(info_list[1][0]) == self.table_info[i]["_password"]:
                        msg = "修改成功"
                        self.table_info[i]["_password"] = str(info_list[2][0])
                        self.table_info[i]["_change_pw_time"] = str(datetime.datetime.now())
                        self.used_password.append(str(info_list[2][0]))
                    else:
                        self.table_info[i]["_error_number"] +=1
                        msg = "密碼錯誤"
        return [Famcy.UpdateAlert(alert_message=msg), Famcy.UpdateBlockHtml(target=self.card2)]

    # def delete_info(self, submission_obj, info_list):
    #     return Famcy.UpdatePrompt(target=self.p_card_delete)

    # def update_delete(self, submission_obj, info_list):
    #     _info_list = submission_obj.origin.find_parent(submission_obj.origin, "FPromptCard").last_card["info_list"]
    #     print("_info_list",_info_list)
    #     print(_info_list.info_list)
    #     msg = "資料填寫有誤"
    #     if len(_info_list.info_list) > 0 and len(_info_list[0]) > 0:
    #         _id = _info_list[0][0]
    #         license_num = "XXXXXX"

    #         if self.post_modify(_id, license_num):
    #             self.get_season_data()
    #             msg = "成功刪除資料"

    #         return [Famcy.UpdateRemoveElement(prompt_flag=True), Famcy.UpdateBlockHtml(target=self.card_2), Famcy.UpdateAlert(alert_message=msg, target=self.card_2)]
    #     return Famcy.UpdateAlert(alert_message=msg, target=self.p_del_card)
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

   
ProjectPage.register("/ProjectPage", Famcy.ClassicStyle(), permission_level=0, background_thread=True)