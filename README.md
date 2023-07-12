### Small projects for learning Python by following the Udemy course [Complete Python Developer in 2023: Zero to Mastery](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/)

Some simple projects created using `Python3`.

| No. | Project                                                     | Created by using                                                   |
| --- | ----------------------------------------------------------- | ------------------------------------------------------------------ |
| 1   | [Converter JPG images to PNG](#converter-jpg-images-to-png) | `Pillow Imaging Library`                                           |
| 2   | [Password checker](#password-checker)                       | `Haveibeenpwned API`                                               |
| 3   | [PDF merger](#pdf-merger)                                   | `PyPDF2`                                                           |
| 4   | [Sending emails](#sending-emails)                           | `smtplib`                                                          |
| 5   | [Sending SMS](#sending-sms)                                 | `Twilio Library`                                                   |
| 6   | [Twitter bot](#twitter-bot)                                 | `Tweepy Library`                                                   |
| 7   | [Web scrapping](#web-scrapping)                             | `BeautifulSoup Library`                                            |
| 8   | [Really smart brain - ML](#really-smart-brain)              | `ImageAI`, `TensorFlow`                                            |
| 9   | [Soccer Data Analysis](#soccer-data-analysis)               | `Kaggle Dataset`, `Jupyter notebook`, `pandas`, `seaborn`, `bokeh` |
| 10  | [Iris Data Analysis](#iris-data-analysis)                   | `Jupyter notebook`, `sklearn`, `joblib`                            |
| 11  | [Generate QR](#generate-qr)                                 | `Pillow Imaging Library`, `QR Code`                                |
| 12  | [Port scanner](#port-scanner)                               | `Socket Library`                                                   |
| 13  | [Anonymous FTP Scanner](#anonymous-FTP-Scanner)             | `ftplib`                                                           |

1. ### Converter JPG images to PNG

   The project uses [`Pillow Imaging Library`](https://pillow.readthedocs.io/en/stable/) for manipulating images. <br>
   To run the project go to the `JpgPngPokedexConverter` folder and use the below command: <br>

   ```console
   narcisabadea:~$ python3 JpgPngPokedexConverter.py Pokedex/ New/
   ```

   It will loop through the imagines from the `Pokedex` folder, convert them to PNG format and save them to a `New` folder.

   **[⬆ Back to Top](#small-python-projects)**

2. ### Password checker

   The project uses [`Haveibeenpwned API`](https://haveibeenpwned.com/API/v3) which allows the list of pwned accounts (email addresses and usernames) to be quickly searched via a RESTful service. <br>
   To run the project go to the `PasswordChecker` folder and use `python3 check_my_pass.py passwordToCheck`. <br>
   It will do a request to the API and return the number of times it was found. <br>

   ```console
   narcisabadea:~$ python3 check_my_pass.py password123
   Password password123 was found 250052 times. You should probably change your password
   Done
   ```

   **[⬆ Back to Top](#small-python-projects)**

3. ### PDF merger

   The project uses [`PyPDF2 Library`](https://pillow.readthedocs.io/en/stable/) for manipulating PDF files. <br>
   To run the project go to the `PdfMerger` folder. <br>

   It can merge multiple PDFs into the `merged.pdf` file as following:

   ```console
   narcisabadea:~$ python3 pdfmerger.py dummy.pdf twopage.pdf tilt.pdf
   ```

   It can also add a watermark to a PDF:

   ```console
   narcisabadea:~$ python3 watermark.py
   ```

   **[⬆ Back to Top](#small-python-projects)**

4. ### Sending emails

   By using the `smtplib module` we define an SMTP client session object that can be used to send mail to any internet machine with an SMTP.

   To run the project:

   - go to the `SendingEmail` folder
   - update `smtp.login` with your email and password from which you are sending the email
   - update the `from`, `to` and `subject` information
   - run the following command: <br>

   ```console
   narcisabadea:~$ python3 email_sender.py
   ```

   The receiver can now check for the email.

   **[⬆ Back to Top](#small-python-projects)**

5. ### Sending SMS

   The project uses [`Twilio Library`](https://www.twilio.com/) <br>
   To run the project go to the `SmsPython` folder and run the following command: <br>

   ```console
   narcisabadea:~$ python3 email_sender.py
   ```

   **[⬆ Back to Top](#small-python-projects)**

6. ### Twitter bot

   The project uses [`Tweepy Library`](https://www.tweepy.org/) <br>
   To run the project go to the `TwitterBot` folder. <br>

   ```console
   narcisabadea:~$ python3 tweettweet.py
   ```

   **[⬆ Back to Top](#small-python-projects)**

7. ### Web scrapping

   The project uses [`BeautifulSoup Library`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for pulling data out of HTML and XML files. <br>
   To run the project go to the `WebScrapping` folder. <br>
   It will do a request to the `https://news.ycombinator.com/news`.

   ```console
   narcisabadea:~$ python3 scrape.py
   ```

   **[⬆ Back to Top](#small-python-projects)**

8. ### Really smart brain

   The project uses [`ImageAI Library`](https://github.com/OlafenwaMoses/ImageAI) which supports a list of state-of-the-art Machine Learning algorithms for image prediction, custom image prediction, object detection, video detection, video object tracking and image predictions trainings, and also [`TensorFlow`](https://www.tensorflow.org/) <br>
   To run the project go to the `ReallySmartBrain` folder. <br>

   The image can be changed from "house.jpg" to any other picture.
   The modelPath can also be changed according to the 4 different algorithms and model types to perform image prediction provided by ImageAI: MobileNetV2, ResNet50, InceptionV3, DenseNet121.
   After running the command below we will receive each object in the predictions array with the corresponding percentage probability.

   ```console
   narcisabadea:~$ python3 brain.py
   church: 49.8652458190918
   boathouse: 31.82643353930564
   castle: 14.124444127082825
   beacon: 1.6986381262540817
   lakeside: 0.5432001315057278
   ```

   **[⬆ Back to Top](#small-python-projects)**

9. ### Soccer Data Analysis

   The project uses [`Kaggle Dataset`](https://www.kaggle.com/) and it's analysed in `Jupyter notebook` by using `pandas`, `seaborn` and `bokeh` <br>
   The `Jupyter notebook .ipynb` file can be seen [`Here`](https://github.com/narcisabadea/Small-python-projects/blob/main/SoccerAnalysis/Soccer.ipynb)

   **[⬆ Back to Top](#small-python-projects)**

10. ### Iris Data Analysis

    The project uses [`Sklearn`](https://scikit-learn.org/stable/) and it's analysed in `Jupyter notebook` by using `datasets`, `model_selection`, `neighbors`, `metrics` from `sklearn`, along with `joblib` <br>
    The `Jupyter notebook .ipynb` file can be seen [`Here`](https://github.com/narcisabadea/Small-python-projects/blob/main/IrisAnalysis/Iris.ipynb)

    **[⬆ Back to Top](#small-python-projects)**

11. ### Generate QR

    The project uses [`QR Code`](https://pypi.org/project/qrcode/). <br>
    To run the project go to the `GenerateQr` folder and run the following command: <br>

    ```console
    narcisabadea:~$ python3 qr_code.py
    ```

      <!-- Source: https://www.codedex.io/projects/generate-a-qr-code-with-python -->

    **[⬆ Back to Top](#small-python-projects)**

12. ### Port scanner

    The project uses [`Socket Python Library`](https://pypi.org/project/qrcode/). <br>
    To run the project go to the `PortScanner` folder and run the following command: <br>

    ```console
    narcisabadea:~$ python3 portscanner.py
    ```

      <!-- Source: https://medium.com/vinsloev-academy/python-cybersecurity-build-a-port-scanner-13b798a1b654 -->

    **[⬆ Back to Top](#small-python-projects)**

13. ### Anonymous FTP Scanner

    The project uses [`Socket Python Library`](https://pypi.org/project/qrcode/). <br>
    To run the project go to the `AnonymousFTPScanner` folder and run the following command: <br>

    ```console
    narcisabadea:~$ python3 anonymous_scanner.py
    ```

      <!-- Source: https://medium.com/vinsloev-academy/python-cybersecurity-for-beginners-build-anonymous-ftp-scanner-a62f0534fcf5 -->

    **[⬆ Back to Top](#small-python-projects)**
