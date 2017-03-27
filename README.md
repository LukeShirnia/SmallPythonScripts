# SmallPythonScripts



### Supported OS check


`curl -s https://raw.githubusercontent.com/LukeShirnia/SmallPythonScripts/master/os_check.py | python`


Example Output:
```
CentOS
Supported RedHat/CentOS
7.3.1611
```
<br />

<br />

<br />

### Check time, and time mins 10 and 80 mins

`curl -s https://raw.githubusercontent.com/LukeShirnia/SmallPythonScripts/master/get_time_examples.py | python`


Example output:

```
Current time            Mar 21 13:54
Minus 10:               Mar 21 13:44
Minus 1 hour 20 mins    Mar 21 12:34
```
<br />

<br />

<br />

### Get UUIDs From a File

The following command takes 1 argument. Replace `file` with the path to a file you wish to extract UUIDs from

`curl -s https://raw.githubusercontent.com/LukeShirnia/SmallPythonScripts/master/get_uuids | python - file`

Example output:

```
13d4d403-920a-4a95-ad97-93f38501da8d
faea7607-4f4e-4b05-a0b2-995510a15327
90694e50-658c-4eee-af4c-e29bdb05ab6a
54a4beaf-4b0a-473d-82e3-9a3cc371d879
cd88c08e-ae5b-4ac4-b84d-4c79102402ad
```
<br />

<br />

<br />


### Count Files in a directory
Replace "/var/www" with the directory you wish to count the files in. 

`curl -s https://raw.githubusercontent.com/LukeShirnia/SmallPythonScripts/master/count_files.py | python - "/var/www"`

Example Output:

```
/var/www
65,472 files, 27,003 folders
```
