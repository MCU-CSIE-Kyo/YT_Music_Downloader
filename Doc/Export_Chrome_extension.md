# Export_Chrome_extensions

## Step 1 : Add the ADB extension into Chrome

- [AdGuard](https://chrome.google.com/webstore/detail/bgnkhhnnamicmpeenaelnjfhikgbkllg)

## Step 2 : Chrome extension

<img src=".\Image\chrome_extensions.png" alt="Chrome_extensions" style="zoom:50%;" />

## Step 3 : Open developer mode and get the extension file name

![Get_extension_ID](.\Image\Get_extension_ID.png)

## Step 4 : Find the local path of extensions 

C:\Users\\***xxx***\AppData\Local\Google\Chrome\User Data\Default\Extensions\

- ***xxx*** : Your username

You will find the folder that the name is same as [AdGuard ID](#Step 3 : Open developer mode and get the extension file name).

## Step 5 : Pack the extension

![Pack_extension](.\Image\Pack_extension.png)

C:\Users\\***xxx***\AppData\Local\Google\Chrome\User Data\Default\Extensions\\***yyy***\\***version***

- ***xxx*** : Your username
- ***yyy*** : [AdGuard ID](#Step 3 : Open developer mode and get the extension file name)
- ***version*** : Extension version. E.g. 4.3.31_0

And press the ***Pack extension***

## Step 6 : Get the extension be packed

C:\Users\\***xxx***\AppData\Local\Google\Chrome\User Data\Default\Extensions\\***yyy***\

- ***xxx*** : Your username
- ***yyy*** : [AdGuard ID](#Step 3 : Open developer mode and get the extension file name)

You will find the ***crx*** file at the path.
