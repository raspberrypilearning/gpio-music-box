## Setting up your project

You're going to need some sample sounds for this project. There are lots of sound files on Raspbian, but they are a little tricky to play using Python. However, it's easy enough to convert the sound files to a different file format that can be used by Python in a straight-forward way.

- The first thing you need to do is create a new directory in which to store all your files for the project. Create a directory called `gpio-music-box` in your `home` directory.

	[[[rpi-gui-creating-directories]]]

### Copying the sample sounds

- Using the same method as before, create a new directory called `samples` inside your `gpio-music-box` directory.

- There are lots of sample sounds stored in `/opt/sonic-pi/etc/samples`. Copy all the sample sounds into your `gpio-music-box/samples` directory.

[[[rpi-gui-copying-files]]]

- When you are done, you should be able to see all the `.flac` sound files in the `samples` directory.

--- hints --- --- hint ---
You can use the `cp` command in the terminal to copy all the files from `/opt/sonic-pi/etc/samples` to `/home/pi/gpio-music-box/samples`.
Alternatively, you could copy and paste them using the GUI file manager.
![file-manager](images/file-manager.png)
--- /hint --- --- hint ---
Using the terminal, you can choose all the files in a directory by using the **wildcard** character: `*`. To ensure that each copied file has the same name as its original, you can use a **period** character `.` after the destination directory. So to copy all the samples, you would type:
```bash
cp /opt/sonic-pi/etc/samples/* /home/pi/gpio-music-box/samples/.
```
--- /hint --- --- hint ---
Here are videos of the terminal and GUI methods.
#### GUI method
<video width="560" height="315" controls>
<source src="images/gpio-music-box-1.webm" type="video/webm">
Try using Firefox or Chrome for WebM support
</video>

#### Terminal method
<video width="560" height="315" controls>
<source src="images/gpio-music-box-2.webm" type="video/webm">
Try using Firefox or Chrome for WebM support
</video>

--- /hint --- --- /hints ---



