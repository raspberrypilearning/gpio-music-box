## Converting your samples

- Python has difficulty playing `.flac` files, so you need to convert them all to `.wav` format.

- Have a look at the sections below to see how to convert audio files and how to batch-process files. See if you can convert all of your `.flac` samples in one batch using **bash**.

[[[nix-bash-convert-media-files]]]

[[[nix-bash-batch-operations-on-files]]]

- The basic idea is the following: `for` each file, use that file as input for the `avconv` command, and then use the file's name, ending in `.wav` instead of `.flac`, as the name of the output file.

- Have a look at the hints below if you need help figuring out how to do this.

--- hints --- --- hint ---
Your bash command should follow the following format:
1. `for` each file with a `.flac` ending
1. convert it using `avconv`
1. name the output with the file's original, but change the `.flac` to `.wav`
--- /hint --- --- hint ---
Your bash command should look like this:
```bash
for f in *.flac; do avconv -i "$f" "${f%.flac}.wav"; done
```
You need to make sure you are in the `samples` directory when you run the command. You can get to your `samples` directory with this command:
```bash
cd /home/pi/gpio-music-box/samples
```
--- /hint --- --- hint ---
Here's an animation showing how the operation can be achieved, along with the output:
<video width="560" height="315" controls>
<source src="images/gpio-music-box-3.webm" type="video/webm">
Try using Firefox or Chrome for WebM support.
--- /hint --- --- /hints ---
