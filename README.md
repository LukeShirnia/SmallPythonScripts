# SmallPythonScripts


<br />


# IPs
The following script can be used to convert CIDR noted IPs to dotted decimal. 


### Method 1
```
curl -s https://raw.githubusercontent.com/LukeShirnia/IPs/master/CIDR_to_dotted-decimal.py  | python - filename
```

Example File:

```
123.456.789.123/21
123.213.342.523/31
123.764.34.234/12
```


Example Output:

```
123.456.789.123 255.255.248.0
123.213.342.523 255.255.255.254
123.764.34.234 255.240.0.0
```

<br />

### Method 2
```
curl -s https://raw.githubusercontent.com/LukeShirnia/SmallPythonScripts/master/slash-notation_to_dotted-decimal.py  | python - --ip x.x.x.x/xx
```

Example:

```
curl -s https://raw.githubusercontent.com/LukeShirnia/SmallPythonScripts/master/slash-notation_to_dotted-decimal.py  | python -ip 123.123.12.12/22
```

Example Output:

```
123.123.12.12 255.255.252.0
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


### Count Files in a directory
Replace `"/var/www"` with the directory you wish to count the files in. 

`curl -s https://raw.githubusercontent.com/LukeShirnia/SmallPythonScripts/master/count_files.py | python - "/var/www"`

Example Output:

```
/var/www
65,472 files, 27,003 folders
```
<br />

<br />

<br />

### Find PID of a Service

Replace `sshd` with the service name you wish to find the pids for:
 
`curl -s https://raw.githubusercontent.com/LukeShirnia/SmallPythonScripts/master/find_process.py | python - sshd`

Example output:

```
/usr/sbin/sshd 1069
/usr/sbin/sshd 3245
```


<br />

<br />

<br />

### Check time, and time mins 10 and 80 mins and 24 hours ago

`curl -s https://raw.githubusercontent.com/LukeShirnia/SmallPythonScripts/master/get_time_examples.py | python`


Example output:

```
Current time                Apr 05 06:18
Minus 10:                   Apr 05 06:08
Minus 1 hour 20 mins        Apr 05 04:58
Minus 24 hours (1440 mins)  Apr  4 06:18 # replace leading 0 in single digit dates
```
