# Shiny_gpt-4o
This project is to use Shiny for python and implament OpenAI's gpt-4o functionality in making a web app that is able to generate images based off of what the user took a picture/recording of.

The way I built this was through a livestream. The link to that can be found here: https://www.youtube.com/watch?v=OLTgI6DAQ_A&t 

Requirements for this will be listed in the requirements.txt file but you will also have to install FFmpeg seperately if you want to run this locally. You will also need to make sure that you make a PATH for it in the System Properties > Environment Variables...

in order to run the app, run the following command in your terminal:
shiny run app.py --port 0 --launch-browser

after looking back at the code in the following repo(or the repo shared in the livestream): https://github.com/jcheng5/multimodal-livestream , I was able to trouble shoot most errors and get something working so that gpt-4o says something to me!