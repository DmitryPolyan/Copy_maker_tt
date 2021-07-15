Usage example:

.../Problem_1/problem_1$ python copy_maker.py config.xml

for help:

.../Problem_1/problem_1$ python copy_maker.py -h

for running pytest:

.../Problem_1$ pytest

logs are saved in a folder:

.../Problem_1/problem_1/logs


Problem 1
Implement a problem that copies files according to the provided configuration file. Configuration file must be in XML
format. Each entry in the configuration file should contain file name, source path and destination path parameters.
File with specified name must be copied from source to destination.

Example
Configuration file:

<config>
    <file
            source_path="C:\\Windows\\system32"
            destination_path="C:\\Program files"
            file_name="kernel32.dll"
    />
    <file
            source_path="/var/log"
            destination_path="/etc"
            file_name="server.log"
    />
</config>
