### convert.py

If you want to convert azw3 or mobi format to epub format. You should try this code.


##### How it works

###### First

Install carlibre to your system.(forgive me, I haven't test this code in Linux and Windows)


```
brew cask install calibre
```


###### Second

Add calibre's commands to the system environment.


```
export PATH="$PATH:/Applications/calibre.app/Contents/MacOS"
```

```
source ~/.zshrc
```


###### Third


```
python convert.py ~/Books
```

And now you can covert all azw3 or mobi format files to epub format in this directory.