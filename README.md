# gid
Download an icon with google-images-download

https://github.com/ellisbrown/google-images-download/tree/wrapperless is used as the original google-images-download python module from pip is currently broken

To build-install-create executable:

1.   Create a Pytnon venv and activate it. Continue next steps from inside the virtual environment
2.   Download or clone https://github.com/ellisbrown/google-images-download/tree/wrapperless. Extract inside the venv
3.   Download gid.py from this repository and place it inside the venv
4.   Install prerequisites (selenium, pyinstaller)
5.   Build, install following the instructions from the repository mentioned above
6.   Create an executable with pyinstaller --onefile gid.py
7.   Use Example: gid 'Debian Linux' png .
