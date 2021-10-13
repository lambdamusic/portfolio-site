---
title: "World date from the terminal"
date: "2021-09-07"
review: false
---

A little Bash script to show information about world time zones. Because I love my colleagues abroad, but I constantly struggle to remember how many hours ahead (or behind?) they are.

It basically scans the `zoneinfo` data already existing on your Mac and return the rows matching an input string.

<script src="https://gist.github.com/lambdamusic/4a5b852c8f9051b1f29033619cd38e36.js"></script>


NOTE On my Mac I found the `zoneinfo` data in this location:

`/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/pytz/zoneinfo/`

That path is needed for the script to work. You can customise it of course, see below how to do it. 


## Set up

Save the file above eg as `wdate` and then make it executable

```bash
chmod +x wdate
```

Then you can run it eg

```bash
$ wdate australia
/Australia/Melbourne               Tue 2021-10-12 20:47:48
/Australia/Queensland              Tue 2021-10-12 19:47:48
/Australia/North                   Tue 2021-10-12 19:17:48
/Australia/Lord_Howe               Tue 2021-10-12 20:47:48
/Australia/Adelaide                Tue 2021-10-12 20:17:48
/Australia/Yancowinna              Tue 2021-10-12 20:17:48
/Australia/Victoria                Tue 2021-10-12 20:47:48
/Australia/Canberra                Tue 2021-10-12 20:47:48
/Australia/Sydney                  Tue 2021-10-12 20:47:48
/Australia/ACT                     Tue 2021-10-12 20:47:48
/Australia/Eucla                   Tue 2021-10-12 18:32:48
/Australia/Brisbane                Tue 2021-10-12 19:47:48
/Australia/Tasmania                Tue 2021-10-12 20:47:48
/Australia/Hobart                  Tue 2021-10-12 20:47:48
/Australia/Perth                   Tue 2021-10-12 17:47:48
/Australia/South                   Tue 2021-10-12 20:17:48
/Australia/Lindeman                Tue 2021-10-12 19:47:48
/Australia/Darwin                  Tue 2021-10-12 19:17:48
/Australia/West                    Tue 2021-10-12 17:47:48
/Australia/LHI                     Tue 2021-10-12 20:47:48
/Australia/NSW                     Tue 2021-10-12 20:47:48
/Australia/Broken_Hill             Tue 2021-10-12 20:17:48
/Australia/Currie                  Tue 2021-10-12 20:47:48
```

## Troubleshoot 

If you don't know where to find `zoneinfo` data on your computer, just search for it. Eg on a Mac: 

```
mdfind -name zoneinfo
```

That'll give you a list of possible candidates. 



## See also  

* The inspiration for this post: https://stackoverflow.com/questions/26802201/bash-get-date-and-time-from-another-time-zone
* Menu World Time - a [menu bar app](https://apps.apple.com/us/app/menu-world-time/id1446377255)
* Getting timezones in Python: https://stackoverflow.com/questions/16505501/get-timezone-from-city-in-python-django