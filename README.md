# NAME
&nbsp;&nbsp;&nbsp;**ting56-dl** - Batch download audio file from **[ting56.com](http://www.ting56.com)**.                
          
# SYNOPSIS            
&nbsp;&nbsp;&nbsp;**ting56-dl** *<u>url</u>*                


# DESCRIPTION           
&nbsp;&nbsp;&nbsp;**ting56-dl** used to batch download audio file from **[ting56.com](http://www.ting56.com)**.For example, suppose you want to download **[鬼吹灯第二部第一卷](http://www.ting56.com/mp3/4704.html)** from **ting56.com**, you should copy the URL of webpage that contain the list of **鬼吹灯第二部第一卷**， and pass the URL to **ting56-dl**. The following is the screenshot:                  

<br /><img src="https://farm2.staticflickr.com/1595/26030453640_5e5e9982eb_z.jpg" width="640" height="442" alt="ting56-dl"></img><br />

In this example, you should run the following command in you terminal:                 
           
```bash
$ ./ting56-dl http://www.ting56.com/mp3/4704.html
```             
Then the audio file will download to directory `Downloads`   
               
# Note
In order to run **ting56-dl** on you system, you should install **[Selenium](https://pypi.python.org/pypi/selenium)**, **[BeautifualSoup](https://pypi.python.org/pypi/beautifulsoup4)**, **[PhantomJS](http://phantomjs.org/download.html)** and **[Python3.4](https://www.python.org/downloads/release/python-340/)** beforehand.
