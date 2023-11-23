from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import ActionChains ##
from subprocess import CREATE_NO_WINDOW
import time
import re
import pyperclip

class automation:
    def __init__(self):
        self.driver = None

        FILE_PATH = f"user-data-dir=C:\\Users\\Lochana Minuwansala\\AppData\\Local\\WBS\\Loch Hutch"
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument(FILE_PATH)
        service = ChromeService("drv\chromedriver.exe")
        service.creation_flags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(options=options, service=service)

        url = 'https://web.whatsapp.com'
        self.driver.get(url)

        ## search bar
        with open('temp/xpath/searchBar.txt') as search:
            self.search_bar = search.read()
        ## msg box xpath
        with open('temp/xpath/msgBox.txt') as msg:
            self.msg_box_xpath = msg.read()
        ## attach button
        with open('temp/xpath/attBtn.txt') as att:
            self.att_btn_xpath = att.read()
        ## send button
        with open('temp/xpath/sendBtn.txt') as send:
                self.send_btn_xpath = send.read()
        ## image and video button
        with open('temp/xpath/imageBtn.txt') as img:
            self.image_xpath = img.read()
        ## document button
        with open('temp/xpath/docBtn.txt') as doc:
            self.document_xpath = doc.read()

        WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located(
                (By.XPATH, self.search_bar)))
    def message_sender(self, number,image_path, doc_path, attach_media_message):
        # Replace below path with the absolute path of the chromedriver in your system
        # Replace 'contact_name' with the name of your contact

        js = """
                                                        var [ num ] = [ arguments[0]];
                                                        function openChat (t) {
                                                            var e;
                                                            t&&((e=document.createElement("a")).setAttribute("href","whatsapp://send?phone="+t),document.body.appendChild(e),e.click(),e.outerHTML="",setTimeout(1,1e3))
        
                                                                  }
                                                        return openChat(num)
                                                    """
        self.driver.execute_script(js, number)
        time.sleep(5)
        try:
            # Replace below message with the message you want to send
            #message = open("test_msg.txt", "r", "utf-8").read()
            message = '''🤑(❁´◡`❁)Welcome to WBS Software - 2023(❁´◡`❁)🤑

📖(⌒▽⌒)📖Sipsala Education Institute.📖(⌒▽⌒)📖🧑‍🔬🧑‍⚕️👩‍🔬

Dear Isuru Buddika,

This is to remind that you have to pay class fee of 2500/= for February month. Please settele it before 21 of this month.
Otherwise you not be able to attend to classes☹️. 
If you have any difficulty related to money, contact us via Whatsapp Message. 🫤

Thank you for your Understanding🙏🙏🙏😊

📖(⌒▽⌒)📖Sipsala Educationn Institute.📖(⌒▽⌒)📖

Sent by WBS - 2023

🤑(❁´◡`❁)WBS මෘදුකාංගයට සාදරයෙන් පිළිගනිම - 2023(❁´◡`❁)🤑

📖(⌒▽⌒)📖සිප්සල අධ්‍යාපන ආයතනය.📖(⌒▽⌒)📖🧑‍🔬🧑‍⚕️👩‍🔬

හිතවත් Isuru Buddika,

මෙම පණිවිඩටය ඔබට February මස පන්ති ගාස්තුව වන රු.2500/= ක මදල ගෙවිය යතු බවට මතක් කිරීමටයි. කරුණාකර එය මෙම මස 21 ට පෙර ගෙවීමට කාරුනික වන්න.
නැතහොත් ඔබට පන්ති සදහා සහභාග වීමේදි අපහසතාවයන්ට මහන දීමට සිදු විය හැකි බවට දන්වා  සිටිම☹️. ඔබට මදල් සම්භන්ද යම් අපහසතාවයක් ඇතොත් ඒ බව වට්සැප් 
පණිවිඩයක් මගින් යොම කරන්ගේ අවබෝධයට ස්තූතියි🙏🙏🙏😊

📖(⌒▽⌒)📖සිප්සල අධ්‍යාපන ආයතනය.📖(⌒▽⌒)📖

Sent by WBS - 2023'''

            # Replace below path with the absolute path of the image file you want to send
            #image_path = "C:/Users/Lochana Minuwansala/PycharmProjects/pythonProject/pyqt5/img/wbs_logo.png"

            time.sleep(2)
            if attach_media_message:
                # Click on the attach button
                attach_btn = self.driver.find_element(By.CSS_SELECTOR, self.att_btn_xpath)
                attach_btn.click()

                time.sleep(1)

                # Click on the 'Photo/Video Library' option
                # when editing this get the input accept xpath
                if image_path is not None:
                    photo_video_btn = self.driver.find_element(By.CSS_SELECTOR, self.image_xpath)

                    time.sleep(2)
                    photo_video_btn.send_keys(image_path)

                    time.sleep(3)

                    # Click on the send button
                    '''send_btn = self.driver.find_element(By.XPATH, self.send_btn_xpath)
                    send_btn.click()'''

                    #time.sleep(5)
                else:
                    doc_btn = self.driver.find_element(By.XPATH, self.document_xpath)

                    time.sleep(2)
                    doc_btn.send_keys(doc_path)

                    time.sleep(3)

                    # Click on the send button
                    '''send_btn = self.driver.find_element(By.XPATH, self.send_btn_xpath)
                    send_btn.click()'''

                actions = ActionChains(self.driver)
                for line in message.split('\n'):
                    actions.send_keys(line)
                    actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                print("done")

                time.sleep(5)
            else:
                actions = ActionChains(self.driver)
                for line in message.split('\n'):
                    actions.send_keys(line)
                    actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
                actions.send_keys(Keys.ENTER)
                actions.perform()
                print("done")

            time.sleep(2)

            #self.driver.quit()
            x = input()
        except Exception as e:
            print(e)

    def find_grps(self):
        time.sleep(3)
        try:
            groups_elements = self.driver.find_elements(By.CLASS_NAME, '_21S-L')
            print(groups_elements)
            for group in groups_elements:
                print(group.text)
            input()
        except Exception as e:
            print(e)

    def extract_contacts(self, selected_grp):
        time.sleep(3)
        try:
            for j in range(1, 100):
                try:
                    grp_name = self.driver.find_element(By.XPATH,
                                                        f'//*[@id="pane-side"]/div[1]/div/div/div[{j}]/div/div/div/div[2]/div[1]/div[1]/span').text
                    grp_click = self.driver.find_element(By.XPATH,
                                                         f'//*[@id="pane-side"]/div[1]/div/div/div[{j}]/div/div/div/div[2]/div[1]/div[1]/span')
                except:
                    continue
                if grp_name == selected_grp:
                    grp_click.click()
                    print("clicked")
                    time.sleep(4)

                    numbers = self.driver.find_element(By.XPATH,
                                                       '//*[@id="main"]/header/div[2]/div[2]/span').text
                    print(numbers)
                    numbers = numbers.split(', ')

                    for number in numbers:
                        if (bool(re.match('^[a-zA-Z]*$', number)) == True):
                            pass
                        else:
                            print(number)
                    break
            input()
        except Exception as e:
            print("extract : " + str(e))
new = automation()
new.message_sender(713120291,"C:/Users/Lochana Minuwansala/PycharmProjects/pythonProject/pyqt5/img/wbs_logo.png",None, False)
#new.find_grps()
#new.extract_contacts("nkn heduwe")