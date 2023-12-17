# 20th-Century-Fox

Test project for 20th-Century-Fox team

# Project

Implement personal contacts terminal bot.

# Requirements

11. Sort files in the specified folder by category (images, documents, videos, etc.).

# Trello Task

20thFox_Ticket8 - Sorting File

# Description

This module:

1. Sorts files by category:

   'Images': ['JPEG', 'PNG', 'JPG', 'SVG', 'TIFF', 'TIF', 'GIF'],
   'Video': ['AVI', 'MP4', 'MOV', 'MKV'],
   'Documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'CSV', 'LOG', 'JSON', 'XML', 'YAML'],
   'Audio': ['MP3', 'OGG', 'WAV', 'AMR', 'FLAC', 'AAC'],
   'Presentations': ['PPT', 'PPTX'],
   'Computer graphics': ['PSD', 'AI', 'SVG', 'EPS'],
   'Databases': ['DB', 'SQLITE', 'DBF', 'MDB'],
   'Executable scripts': ['PY', 'JS', 'SH', 'BAT'],
   'Archives': ['ZIP', 'GZ', 'TAR'],
   'Books' : ['FB2', 'EPUB', 'MOBI'],
   '3D models': ['3DS', 'STEP', 'STP', 'OBJ', 'FBX', 'IGS', 'MB', 'MAX', 'C4D']

You can expand dictionary by own categories.

2. Normalizes file names:

   Transliteration Cyrillic to Latin
   Replaces a character that is not contained in the [a-zA-Z0-9_] list with an underscore character '\_'
   Checks if after normalization file name is exist and then add next sequence number for the file

3. Unpacks archives

4. Checks if folder 'Sorted' already exist and close the program

5. Creates a folder 'Sorted' in the directory and copy files there
